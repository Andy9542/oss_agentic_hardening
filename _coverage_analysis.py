#!/usr/bin/env python3
"""Единый воспроизводимый источник показателей перекрытия угроз.

Импортирует данные матрицы из _gen_matrix.py (ROWS/METHODS/METHOD_IDS) и
метаданные карточек методов из 10-methods/*.md (frontmatter: layer,
method-type, prod-viable, covers). На их основе ДЕТЕРМИНИРОВАННО вычисляет:

  * echelon[C]  — показатель эшелонированности класса угроз C =
                  число РАЗЛИЧНЫХ средств, имеющих оценку «выс.» хотя бы
                  в одном сценарии, где класс C выступает основным или
                  сопутствующим (asi-тег);
  * mature[C]   — из них промышленно зрелых (prod-viable == "true").

Правило подсчёта единообразно для всех классов; промышленная готовность
показывается ОТДЕЛЬНЫМ признаком и НЕ вычитается из основного счёта.
Второй кодировщик, повторив эти шаги, получит те же числа.

Перегенерация выгрузок:
    python _coverage_analysis.py            # печать сводки
    python _coverage_analysis.py --csv PATH # выгрузка reconciled_matrix.csv
"""
from __future__ import annotations
import os, re, glob, importlib.util
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))

def _load_matrix():
    spec = importlib.util.spec_from_file_location("_gen_matrix", os.path.join(HERE, "_gen_matrix.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def _parse_frontmatter(txt):
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    if not m: return {}
    fm={}; key=None
    for ln in m.group(1).split("\n"):
        if re.match(r"^\s*-\s", ln) and key:
            fm[key].append(ln.strip()[2:].strip())
        elif ":" in ln:
            k,_,v = ln.partition(":"); k=k.strip(); v=v.strip()
            if v=="": fm[k]=[]; key=k
            else: fm[k]=v; key=None
    return fm

def load_method_meta():
    meta={}
    for f in sorted(glob.glob(os.path.join(HERE, "10-methods", "*.md"))):
        fm=_parse_frontmatter(open(f, encoding="utf-8").read())
        if fm.get("id"):
            mid=int(fm["id"])
            meta[mid]={k:fm.get(k) for k in
                       ("layer","method-type","prod-viable","effectiveness","robustness","evidence-level","covers")}
            meta[mid]["slug"]=os.path.basename(f)[:-3]
    return meta

def _row_classes(asi, primary):
    cs={primary}
    for tag in (asi or "").replace(" ","").split(","):
        if tag and tag!="\u2014": cs.add(tag)
    return cs

def compute():
    gm=_load_matrix(); meta=load_method_meta()
    prod={mid:meta[mid]["prod-viable"] for mid in meta}
    echelon=defaultdict(set); mature=defaultdict(set)
    for asi,llm,primary,scen,bid,vals in gm.ROWS:
        classes=_row_classes(asi, primary)
        for mid,v in zip(gm.METHOD_IDS, vals):
            if v==gm.HIGH:
                for c in classes:
                    echelon[c].add(mid)
                    if prod.get(mid)=="true": mature[c].add(mid)
    return gm, meta, echelon, mature

ASI_ORDER=[f"ASI{i:02d}" for i in range(1,11)]

if __name__=="__main__":
    import sys
    gm,meta,echelon,mature=compute()
    if "--csv" in sys.argv:
        import csv
        path=sys.argv[sys.argv.index("--csv")+1]
        with open(path,"w",newline="",encoding="utf-8") as fh:
            w=csv.writer(fh); w.writerow(["class","echelon_high","echelon_mature","methods_high","methods_mature"])
            for c in ASI_ORDER:
                hi=sorted(echelon.get(c,[])); mat=sorted(mature.get(c,[]))
                w.writerow([c,len(hi),len(mat)," ".join(map(str,hi))," ".join(map(str,mat))])
        print("written", path)
    else:
        for c in ASI_ORDER:
            hi=sorted(echelon.get(c,[])); mat=sorted(mature.get(c,[]))
            print(f"{c}: эшелон={len(hi)} зрелых={len(mat)}  {hi}")
