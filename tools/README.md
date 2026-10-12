# Tools

Small, dependency-light Python 3 scripts for a Markdown + Logos study workflow. All are generic; replace paths with your own. See the [workflow guide](../guides/logos-github-workflow.md) for context.

| Script | What it does | Needs |
|---|---|---|
| `md_to_logos_html.py` | Markdown study file → simple HTML that pastes cleanly into a Logos note | stdlib |
| `chat_pdf_to_md.py` | AI chat printed to PDF → user/assistant turns → Markdown with front matter | `pip install pymupdf` |
| `build_index.py` | Builds `INDEX.md` from the front matter of every `.md` file | stdlib |
| `note_save_server.py` | Local page to paste a copied Logos note body into and save it as HTML | stdlib |
| `logos_notes_reader.py` | Read-only schema lister / exporter for a **copy** of the Logos notes SQLite DB | stdlib |
| `classify_topics.py` | Keyword-based topic suggester; writes a CSV for review | stdlib (PyYAML optional) |

## md_to_logos_html.py

```bash
python3 tools/md_to_logos_html.py study.md > note.html
# also link plain Bible references (John 3:16, Eph 2:8-10) to Biblia.com for readers without Logos:
python3 tools/md_to_logos_html.py study.md --biblia kjv1900 > note.html
python3 tools/md_to_logos_html.py study.md --title "John 1:1-5" > note.html
```

`>` quotes become `<p class="ql-indent-1">` (Logos strips `<blockquote>`); pipe tables become bullet lists; headings become bold paragraphs in Logos. Then paste as rich text: serve the folder (`python3 -m http.server 8000`) and copy from the browser, or on Linux `xclip -selection clipboard -t text/html -i note.html`.

## chat_pdf_to_md.py

1. Open the chat, scroll to the end so everything loads, and print to PDF.
2. Run:

```bash
python3 tools/chat_pdf_to_md.py chat.pdf -o chats/soteriology/2026-01-31-my-chat.md \
  --title "My chat" --source "https://example.com/chat/<id>" --date 2026-01-31 \
  --project "My project" --topic soteriology --assistant-label Assistant
```

Turn detection is layout-based: user messages are lines inside light, right-aligned "bubble" rectangles. If a site prints differently, run with `--debug` and adjust `--bubble-min-x`, `--bubble-right`, and `--line-min-x`. Always skim the output; headings and code blocks may need manual touch-up. The source PDF is only read.

## build_index.py

```bash
python3 tools/build_index.py . -o INDEX.md
```

## note_save_server.py

```bash
python3 tools/note_save_server.py --outdir exports
# open http://127.0.0.1:8767/, name the file, paste the note body, click Save
pandoc -f html -t gfm exports/my-note.html -o my-note.md
```

Listens on localhost only. File names are reduced to a base name (no directories).

## logos_notes_reader.py

**Untested against all Logos versions; the schema is undocumented.** Close Logos and copy `Documents\<random>.mxq\NotesToolManager\notestool.db` (plus any `-wal`/`-shm` files) first. The copy is opened read-only.

```bash
python3 tools/logos_notes_reader.py notestool-copy.db --schema
python3 tools/logos_notes_reader.py notestool-copy.db --export out/            # tables named like note/notebook/anchor/highlight
python3 tools/logos_notes_reader.py notestool-copy.db --export out/ --tables Notes,Notebooks
```

Note bodies may be stored in an internal rich-text format rather than HTML; inspect the export before converting.

## Tested

All five scripts were run on synthetic inputs (a generated chat PDF, a toy SQLite DB, local POSTs to the save server, and a sample repo). They have not been tested against every chat site's print layout or every Logos version.

## classify_topics.py

Keyword-based topic suggester for sorting imported material (see [starting points](../guides/starting-points.md)). Reads a JSON map (or YAML with PyYAML), scores title matches ×3 and body matches ×1, and writes a CSV for review. It never moves or edits files.

```bash
python3 tools/classify_topics.py --example-map > topics.json
python3 tools/classify_topics.py imports/ --map topics.json -o suggestions.csv [--min-score 2] [--ext .md,.txt]
```

Tested on sample files with the JSON map (the YAML path requires PyYAML and was not tested).
