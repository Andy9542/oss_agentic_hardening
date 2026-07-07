---
name: obsidian-json-canvas
description: >-
  Create and validate Obsidian JSON Canvas (.canvas) visual maps for oss_agentic_hardening.
  Use when the user wants a visual diagram, concept map, flow board, architecture canvas,
  demo storyboard for methods №6/№10/№16/№22/№28, or mentions .canvas, JSON Canvas,
  Obsidian canvas, visual vault map. Prefer mermaid skill for inline diagrams in .md files.
---

# Obsidian JSON Canvas

Create `.canvas` files per [jsoncanvas.org](https://jsoncanvas.org/).

## References

- [canvas-schema.md](references/canvas-schema.md)
- [vault-conventions.md](../obsidian-shared/references/vault-conventions.md)

## Workflow

1. Gather nodes (methods, labels, file refs) and edges (flow, complements)
2. Assign unique string ids (`n1`, `n2`, …)
3. Position nodes (x, y, width, height) for readable layout
4. Write `30-mocs/<name>.canvas` or user path
5. Validate:

```bash
python .agents/skills/obsidian-json-canvas/scripts/validate_canvas_json.py <file.canvas>
```

## File nodes

Use repo-relative paths: `10-methods/06-content-dlp-inspection.md`

## Pair with

- **mermaid** — inline charts in markdown
- **obsidian-vault** — placing canvas in 30-mocs/
