# Examples

- [john-1-1-5-study.md](john-1-1-5-study.md): a complete sample passage study on John 1:1–5, with verses inline (KJV, WEB; public domain), a translation-difference table, and indented quote blocks with the citation format. Library quotes are **placeholders**, never real quotations.
- [john-1-1-5-study.logos.html](john-1-1-5-study.logos.html): the same study converted by `tools/md_to_logos_html.py`, ready to paste into a Logos note. Note how the table became a list and the `>` quotes became `ql-indent-1` paragraphs.
- [john-3-16-group-study.md](john-3-16-group-study.md): a worked small-group handout on John 3:16–21 (class or Logos note type): leader's questions, the prompt, Logos steps, and the answered handout with a cross-tradition presentation. Chrysostom is quoted from the public-domain NPNF on CCEL; licensed library quotes are placeholders.
- [john-3-16-group-study.logos.html](john-3-16-group-study.logos.html): its Logos-note HTML.

Regenerate the HTML:

```bash
python3 tools/md_to_logos_html.py examples/john-1-1-5-study.md --title "John 1:1-5: The Word in the Beginning" > examples/john-1-1-5-study.logos.html
```
