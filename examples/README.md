# Examples

- [john-1-1-5-study.md](john-1-1-5-study.md): a complete sample passage study on John 1:1–5, with verses inline (KJV, WEB; public domain), a translation-difference table, and indented quote blocks with the citation format. Library quotes are **placeholders**, never real quotations.
- [john-1-1-5-study.logos.html](john-1-1-5-study.logos.html): the same study converted by `tools/md_to_logos_html.py`, ready to paste into a Logos note. Note how the table became a list and the `>` quotes became `ql-indent-1` paragraphs.
- [john-3-16-group-study.md](john-3-16-group-study.md): a worked small-group handout on John 3:16–21 (class or Logos note type): leader's questions, the prompt, Logos steps, and the answered handout with a cross-tradition presentation. Chrysostom is quoted from the public-domain NPNF on CCEL; licensed library quotes are placeholders.
- [john-3-16-group-study.logos.html](john-3-16-group-study.logos.html): its Logos-note HTML.
- [ephesians-2-week-01.md](ephesians-2-week-01.md): a worked passage study on Ephesians 2 read in the frame of Ephesians 1–6 (the audience, the wall, the new creation). It argues one reading (the corporate Jew–Gentile frame) and sets out the Reformed, Lutheran, Orthodox and Arminian readings by branch, including Chrysostom's counter-reading of the wall. Includes a color-coded chart and diagrams, a Mermaid outline, and brief, cited commentary quotations. LSV text (CC BY-SA 4.0); Chrysostom from the public-domain NPNF.
- [ephesians-1-6-audience-mapping.md](ephesians-1-6-audience-mapping.md): its companion, the full LSV text of Ephesians 1–6 with every audience phrase color-coded (Yellow/gold = Jewish believers, Blue = Gentiles, Green = both; Pink marks Ephesians 2:1–10 in the chart). Shows how to use CSS classes for colors on the website (`audience_colors: true` in front matter).

Regenerate the HTML:

```bash
python3 tools/md_to_logos_html.py examples/john-1-1-5-study.md --title "John 1:1-5: The Word in the Beginning" > examples/john-1-1-5-study.logos.html
```

## Website demos

- [Quran pop-up demo](quran-popup-demo.md) (`quran_popups: true`)
- [Sefaria Linker demo](sefaria-linker-demo.md) (`sefaria_linker: true`)
