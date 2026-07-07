# JSON Canvas (.canvas)

Spec: https://jsoncanvas.org/

## Top-level keys

```json
{
  "nodes": [],
  "edges": []
}
```

Optional: `metadata` with `version`, `frontmatter`.

## Node types

| type | Purpose |
|------|---------|
| `text` | Markdown text box |
| `file` | Link to vault file |
| `link` | External URL |
| `group` | Container for nodes |

### Text node example

```json
{
  "id": "n1",
  "type": "text",
  "x": 0,
  "y": 0,
  "width": 280,
  "height": 120,
  "text": "# DLP\nКонтентная инспекция"
}
```

### File node example

```json
{
  "id": "n2",
  "type": "file",
  "file": "10-methods/06-content-dlp-inspection.md",
  "x": 320,
  "y": 0,
  "width": 400,
  "height": 200
}
```

## Edge example

```json
{
  "id": "e1",
  "fromNode": "n1",
  "toNode": "n2",
  "label": "egress"
}
```

## Demo ideas (this vault)

- **№6→№10→№16** — DLP → schema → IFC chain
- **№22 kill switch** — split-screen operator vs breaker
- **№28 toxic flow** — GitHub-MCP flow graph

## vs Mermaid

- Mermaid: inline in `.md` notes (use **mermaid** skill)
- Canvas: standalone `.canvas` for Obsidian visual board

## Validate

```bash
python .agents/skills/obsidian-json-canvas/scripts/validate_canvas_json.py <file.canvas>
```
