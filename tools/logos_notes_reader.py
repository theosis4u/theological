#!/usr/bin/env python3
"""Read-only explorer/exporter for a COPY of the Logos desktop notes database.

UNTESTED against all Logos versions. The schema is undocumented and changes, so this
script makes no assumptions: it lists every table and column, then exports rows from
tables whose names look note-related (note, notebook, anchor, highlight) to JSON/CSV.

Safety:
  * Always work on a copy. Close Logos, then copy e.g.
      C:\\Users\\<you>\\Documents\\<random>.mxq\\NotesToolManager\\notestool.db
    (plus any -wal/-shm files next to it) to a working folder.
  * The database is opened read-only (sqlite URI mode=ro); nothing is written to it.

Usage:
  logos_notes_reader.py notestool-copy.db --schema
  logos_notes_reader.py notestool-copy.db --export out_dir [--tables Notes,Notebooks] [--like note]
"""
import argparse, csv, json, os, sqlite3

DEFAULT_LIKE = ('note', 'notebook', 'anchor', 'highlight')


def connect(path):
    uri = 'file:' + os.path.abspath(path).replace('\\', '/') + '?mode=ro'
    return sqlite3.connect(uri, uri=True)


def tables(con):
    return [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]


def columns(con, t):
    return [(r[1], r[2]) for r in con.execute(f'PRAGMA table_info("{t}")')]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('db'); ap.add_argument('--schema', action='store_true')
    ap.add_argument('--export'); ap.add_argument('--tables')
    ap.add_argument('--like', action='append', help='table-name substring to export (repeatable)')
    a = ap.parse_args()
    con = connect(a.db)
    ts = tables(con)
    if a.schema or not a.export:
        for t in ts:
            n = con.execute(f'SELECT COUNT(*) FROM "{t}"').fetchone()[0]
            print(f'{t} ({n} rows)')
            for c, typ in columns(con, t):
                print(f'    {c} {typ}')
    if a.export:
        os.makedirs(a.export, exist_ok=True)
        if a.tables:
            pick = [t for t in a.tables.split(',') if t in ts]
        else:
            likes = [s.lower() for s in (a.like or DEFAULT_LIKE)]
            pick = [t for t in ts if any(s in t.lower() for s in likes)]
        for t in pick:
            cur = con.execute(f'SELECT * FROM "{t}"')
            cols = [d[0] for d in cur.description]
            rows = [dict(zip(cols, [v.hex() if isinstance(v, bytes) else v for v in r])) for r in cur]
            with open(os.path.join(a.export, t + '.json'), 'w', encoding='utf-8') as f:
                json.dump(rows, f, ensure_ascii=False, indent=1)
            with open(os.path.join(a.export, t + '.csv'), 'w', newline='', encoding='utf-8') as f:
                w = csv.DictWriter(f, cols); w.writeheader(); w.writerows(rows)
            print(f'exported {t}: {len(rows)} rows')
        if not pick:
            print('No matching tables. Run --schema and pass --tables explicitly.')


if __name__ == '__main__':
    main()
