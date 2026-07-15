#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Генерация Рис. 4 (тепловая карта) и Рис. 5 (эшелонированность) из единого источника.
Источник данных: _gen_matrix.py (поля ROWS) + 10-methods/*.md (frontmatter).
Оба рисунка выводятся из одной таблицы сценариев и согласованы по построению.
Запуск:  python _gen_figures.py   (пишет Статья/img/ris4_heatmap.png, ris5_echelon.png)
"""
import os, re, importlib.util
from collections import Counter, defaultdict
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.abspath(__file__))

def load_gen():
    spec = importlib.util.spec_from_file_location("gm", os.path.join(ROOT, "_gen_matrix.py"))
    gm = importlib.util.module_from_spec(spec); spec.loader.exec_module(gm); return gm

def load_meta():
    meta = {}
    mdir = os.path.join(ROOT, "10-methods")
    for fn in os.listdir(mdir):
        m = re.match(r"(\d+)-", fn)
        if not m: continue
        txt = open(os.path.join(mdir, fn), encoding="utf-8").read()
        fm = txt.split("---")[1] if txt.startswith("---") else ""
        d = {}
        for line in fm.splitlines():
            if ":" in line:
                k, v = line.split(":", 1); d[k.strip()] = v.strip()
        meta[int(m.group(1))] = d
    return meta

# --- 6 архитектурных уровней (воспроизводит счёт §4.1: 10/14/5/8/7/2) ---
LEVEL_OF = {}
for i in range(1, 11):  LEVEL_OF[i] = "Текст"
for i in list(range(11, 23)) + [42, 43]: LEVEL_OF[i] = "Действие"
for i in [23, 24, 33, 34, 35]: LEVEL_OF[i] = "Сеть/инфра"
for i in [25, 26, 27, 28, 29, 30, 31, 32]: LEVEL_OF[i] = "Цепочка"
for i in [36, 37, 38, 39, 40, 41, 46]: LEVEL_OF[i] = "Подлин./аудит"
for i in [44, 45]: LEVEL_OF[i] = "Измерение"

ASI = [f"ASI{i:02d}" for i in range(1, 11)]
ASI_NAMES = {"ASI01":"Захват цели агента","ASI02":"Опасный вызов инструмента",
    "ASI03":"Эскалация привилегий","ASI04":"Отравление цепочки поставок",
    "ASI05":"Побег из песочницы","ASI06":"Отравление памяти",
    "ASI07":"Небезопасная связь агентов","ASI08":"Каскадные сбои / DoS",
    "ASI09":"Обман оператора","ASI10":"Rogue-агент"}

def echelon_tables(gm, meta):
    high = defaultdict(set); mature = defaultdict(set)
    for asi, llm, primary, title, bid, ratings in gm.ROWS:
        tags = set()
        for t in ([asi] + [x.strip() for x in llm.split(",")] + [primary]):
            if t and t.startswith("ASI"): tags.add(t)
        for i, val in enumerate(ratings):
            mid = i + 1
            if val == "выс.":
                for c in tags:
                    high[c].add(mid)
                    if meta.get(mid, {}).get("prod-viable") == "true": mature[c].add(mid)
    return high, mature

def fig_echelon(gm, meta, out):
    high, mature = echelon_tables(gm, meta)
    rows = sorted(ASI, key=lambda c: (len(high[c]), len(mature[c])))
    tot = np.array([len(high[c]) for c in rows]); mat = np.array([len(mature[c]) for c in rows])
    imm = tot - mat; y = np.arange(len(rows))
    labels = [f"{c} · {ASI_NAMES[c]}" for c in rows]
    focal, imm_col, alarm = "#2b6cb0", "#9ec5e8", "#c0392b"
    fig, ax = plt.subplots(figsize=(7.4, 4.6))
    ax.barh(y, mat, color=focal, edgecolor="white", height=0.62, zorder=3, label="Промышленно зрелые")
    ax.barh(y, imm, left=mat, color=imm_col, edgecolor=focal, height=0.62, zorder=3,
            hatch="////", label="Сильные, но промышленно незрелые")
    for yi, t in zip(y, tot):
        if t > 0: ax.text(t + 0.15, yi, str(t), va="center", ha="left", fontsize=8, color="#222", zorder=5)
        else: ax.plot(0.06, yi, "o", ms=4, color=alarm, zorder=5)
    ax.axvline(1.5, color=alarm, lw=1.1, ls=(0, (4, 2)), zorder=2)
    ax.annotate("порог уязвимости\n(≤1 сильного средства)", xy=(1.5, 1.0), xytext=(4.6, 1.3),
                color=alarm, fontsize=6.8, va="center", ha="left", zorder=6,
                arrowprops=dict(arrowstyle="->", color=alarm, lw=0.8))
    ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=7.5)
    for tick, c in zip(ax.get_yticklabels(), rows):
        if len(high[c]) <= 1: tick.set_color(alarm)
    ax.set_xlabel("Показатель эшелонированности Э(C):\nчисло независимых сильных средств")
    ax.set_xlim(0, 14); ax.margins(y=0.02)
    ax.set_title("Эшелонированность защиты по классам угроз OWASP ASI (2026)", fontsize=9, loc="left")
    ax.legend(loc="lower right", frameon=False, fontsize=7, bbox_to_anchor=(1.0, 0.10))
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    fig.tight_layout(); fig.savefig(out, dpi=200, bbox_inches="tight"); plt.close(fig)

def fig_heatmap(gm, out):
    LEVELS = ["Текст", "Действие", "Сеть/инфра", "Цепочка", "Подлин./аудит"]
    scen = []
    for asi, llm, primary, title, bid, ratings in gm.ROWS:
        counts = {L: 0 for L in LEVELS}
        for i, val in enumerate(ratings):
            if val == "выс.":
                L = LEVEL_OF[i + 1]
                if L in counts: counts[L] += 1
        t = title.replace("↳ ", "").strip()
        if len(t) > 34: t = t[:33] + "…"
        scen.append((f"{primary} · {t}", [counts[L] for L in LEVELS]))
    labels = [s[0] for s in scen]; M = np.array([s[1] for s in scen])
    fig, ax = plt.subplots(figsize=(7.6, 7.4))
    im = ax.imshow(M, cmap=plt.cm.Blues, aspect="auto", vmin=0, vmax=M.max())
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            v = M[i, j]
            if v > 0:
                ax.text(j, i, str(v), ha="center", va="center",
                        color="white" if v > M.max() * 0.55 else "#1a3a5c", fontsize=8.5, fontweight="bold")
    ax.set_xticks(range(len(LEVELS))); ax.set_xticklabels(LEVELS, fontsize=8, rotation=20, ha="right")
    ax.set_yticks(range(len(labels))); ax.set_yticklabels(labels, fontsize=7.3)
    ax.set_xticks(np.arange(-.5, len(LEVELS), 1), minor=True)
    ax.set_yticks(np.arange(-.5, len(labels), 1), minor=True)
    ax.grid(which="minor", color="white", lw=1.2); ax.tick_params(which="minor", length=0)
    ax.set_title("Число сильных средств защиты по архитектурным уровням\nдля сценариев атак (OWASP ASI/LLM)",
                 fontsize=9, loc="left")
    cb = fig.colorbar(im, ax=ax, fraction=0.032, pad=0.02)
    cb.set_label("Число средств с высокой силой", fontsize=7.5); cb.ax.tick_params(labelsize=7)
    fig.tight_layout(); fig.savefig(out, dpi=200, bbox_inches="tight"); plt.close(fig)

if __name__ == "__main__":
    gm = load_gen(); meta = load_meta()
    img = os.path.join(ROOT, "Статья", "img")
    fig_heatmap(gm, os.path.join(img, "ris4_heatmap.png"))
    fig_echelon(gm, meta, os.path.join(img, "ris5_echelon.png"))
    print("Рис. 4 и Рис. 5 обновлены из единого источника.")
