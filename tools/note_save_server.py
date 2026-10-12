#!/usr/bin/env python3
"""Tiny local page for exporting Logos notes (or any rich text) to HTML files.

Open http://127.0.0.1:8767/ , type a file name, paste the copied note body into the
box, and click Save. The HTML is written to OUTDIR/<name>.html. Convert it to
Markdown afterwards, e.g.:  pandoc -f html -t gfm OUTDIR/name.html -o name.md

Listens on localhost only. Usage: note_save_server.py [--outdir exports] [--port 8767]
"""
import argparse, http.server, json, os

PAGE = '''<!doctype html><html><head><meta charset="utf-8"><title>Note export</title></head><body>
<input id=n placeholder="file name"> <button id=b>Save</button> <span id=s></span>
<div id=d contenteditable style="border:1px solid #888;min-height:400px;padding:8px;margin-top:8px"></div>
<script>b.onclick=()=>fetch('/save',{method:'POST',body:JSON.stringify({n:n.value,h:d.innerHTML})})
.then(r=>r.text()).then(t=>s.textContent=t)</script></body></html>'''


def make_handler(outdir):
    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200); self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers(); self.wfile.write(PAGE.encode())

        def do_POST(self):
            j = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
            name = os.path.basename(j.get('n') or '').strip() or 'note'
            path = os.path.join(outdir, name + '.html')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(j.get('h', ''))
            self.send_response(200); self.end_headers()
            self.wfile.write(f'saved {path} ({len(j.get("h", ""))} chars)'.encode())
    return H


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--outdir', default='exports')
    ap.add_argument('--port', type=int, default=8767); a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    print(f'Serving on http://127.0.0.1:{a.port}/ , saving to {os.path.abspath(a.outdir)}')
    http.server.HTTPServer(('127.0.0.1', a.port), make_handler(a.outdir)).serve_forever()
