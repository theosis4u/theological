---
title: "Logos + GitHub Guide"
date: 2026-10-11
topic: workflow
---

# Integrating Logos Bible Software with a GitHub Markdown Repo and an AI Assistant
{: .no_toc}

## Contents
{: .no_toc}

* Contents
{:toc}

---

## About this guide

This guide describes a working setup that connects Logos Bible Software (both the desktop install and the web app at `app.logos.com`) with a Git repository of Markdown files and an AI assistant. The goal is simple: your study work lives in plain text you control, your study partners read it comfortably inside Logos, and every quotation carries a link back to the exact spot in the source.

For a companion template of standing instructions for the AI assistant (request types, source tiers, verification and citation rules), see [A Working Method and Template for AI-Assisted Theological Study](ai-theology-method-template.md).

No Logos? See [Free resources](free-resources.md). New to this repo? Begin with [START-HERE.md](../START-HERE.md). If you only have Microsoft Copilot (no shell or browser automation), see [Using the workflow with Microsoft Copilot and Logos](copilot-workflow.md). To seed a repo from existing chats, posts, emails, notes, and documents, see [Starting points](starting-points.md). See also the [setup checklist and FAQ](setup-checklist.md) and the [AI coverage testing kit](ai-coverage-test.md).

For what was built and why, see the [project history](../docs/project-history.md).

All names, paths, and IDs below are placeholders. Replace `<you>`, `<random>`, and similar markers with your own values.

## 1. Architecture

The setup has three parts, and each one has a single job.

- **A private Markdown repository is the source of truth.** Every study, handout, and source collection is a `.md` file with front matter. Git gives you history, diffs, and backups. Keep this repo private by default; publish only what you choose to share, in a separate public repo.
- **Logos notes are the shared reading surface.** Anyone with access to the Logos account sees the notes, with Bible references turned into live links. Notes are generated *from* the Markdown, not edited independently, so the two never drift apart for long.
- **AI chats are exported into the repo.** Past conversations with an AI assistant become Markdown files too, so the assistant (and you) can search and cite earlier work instead of starting over.

A typical cycle: draft in Markdown, review the diff on GitHub, convert to Logos HTML, paste into a new note, and export any later edits made in Logos back into Markdown.

## 2. Importing old AI chats into Markdown

Chat sites rarely offer a clean export, so the reliable path is to render each conversation and then structure it.

1. **List the chats.** Collect each conversation's URL and title from the chat site's history (for example, a project or folder view).
2. **Render each chat to PDF.** Open the conversation in a browser and print it to PDF. Long chats load lazily, so scroll to the end first.
3. **Extract the text.** Use `pdftotext -layout chat.pdf chat.txt` (from poppler-utils).
4. **Segment into turns.** Split the text into user and assistant turns, using the speaker markers or layout cues the site prints. Mark each turn with a heading such as `## User` and `## Assistant`.
5. **Clean up.** Remove page headers, footers, page numbers, UI labels ("Copy", "Share", "Regenerate"), and hyphenation breaks.
6. **Add front matter** to each file:

   ```yaml
   ---
   title: "Short descriptive title"
   source: https://example-chat-site.com/chat/<id>
   date: 2026-01-31
   project: "<project or folder name>"
   topic: soteriology
   ---
   ```

7. **Sort by topic** into folders (for example `chats/soteriology/`, `chats/revelation/`), then write an `INDEX.md` that lists every file with its date and a one-line summary.

Treat the chat site as **read-only** throughout: never delete, rename, or edit conversations there while exporting.

## 3. Writing Logos notes from Markdown

### 3.1 What the Logos note editor accepts

The Logos note editor is a rich-text editor that keeps only a small set of HTML. Stick to:

- `<p>`, `<strong>`, `<em>`, `<ul>`, `<ol>`, `<li>`, and `<a href>` links.
- Headings (`<h1>`–`<h3>`) do not survive as headings; they become **bold paragraphs**, which still read well as section headers.
- `<blockquote>` is stripped. For an indented quote, use `<p class="ql-indent-1">…</p>`.
- Tables are not supported. Convert them to bullet lists, one row per item.
- Use `<p><br></p>` for a blank line between blocks.
- The **first line becomes the note title** in the notes list, so start with `<p><strong>Title</strong></p>` and put no blank line above it.
- Bible references written in plain text (for example "Eph 2:8" or "Romans 3:21–26") turn into clickable passage links automatically. You do not need to link them yourself.

### 3.2 The converter script

[`tools/md_to_logos_html.py`](../tools/md_to_logos_html.py) applies all of these rules:

```bash
python3 tools/md_to_logos_html.py studies/my-study.md > /tmp/note.html
python3 tools/md_to_logos_html.py studies/my-study.md --title "My Study Note" > /tmp/note.html
```

It reads the `title` from front matter (or `--title`), turns `> ` quote lines into `ql-indent-1` paragraphs, converts pipe tables to lists, keeps Markdown links as `<a href>`, and inserts the spacing paragraphs.

### 3.3 Pasting as rich text

The HTML has to reach the note as rich text, not as visible tags. Two ways work:

- **Serve it locally and copy from the browser.** Run `python3 -m http.server 8000` in the folder with `note.html`, open `http://localhost:8000/note.html`, select all, and copy. Some browser automation tools block `file://` pages, which is why a local server is used.
- **Load the clipboard directly (Linux).** `xclip -selection clipboard -t text/html -i /tmp/note.html`

Then in Logos:

1. Create a new note in the target notebook (or open the existing one).
2. **Confirm the right note is open** before pasting. The notes list can lag behind clicks, so check the title in the editor itself.
3. Click into the note body and paste.
4. Check that spacing, bold, lists, links, and indented quotes came through.

Only replace or delete an existing note when you mean to, and save its current text to the repo first (see section 4).

## 4. Exporting Logos notes back to Markdown

Logos has no direct Markdown export, but the editor's HTML can be captured.

1. Run a tiny local save server: a Python script using `http.server` that serves one page containing a `contenteditable` `<div>` and a Save button. The button `POST`s the div's `innerHTML` to the server, which writes it to a file such as `exports/<note-title>.html`. About 30 lines of Python is enough.
2. In Logos, click into the note body, select all, and copy.
3. Paste into the contenteditable area on the save page and click Save.
4. Convert the saved HTML to Markdown, for example with `pandoc -f html -t gfm exports/note.html -o note.md`, then turn indented paragraphs back into `> ` quotes and restore the front matter.
5. Commit, and review the diff against the earlier version.

## 5. Citations: inline links instead of anchors

### 5.1 Copying with citations (recommended)

When you copy text from a resource in Logos, it can attach a citation with a link to the exact location:

1. In the resource panel, select the text you want to quote.
2. Use **Share > Copy** (or the copy option in the selection menu).
3. In the copy settings, turn on **Copy citations** and **Hyperlink copied citations**.
4. Paste into the note.

You get the quoted text followed by an APA-style citation, for example:

> Author, A. (Year). *Resource Title* (p. 123). Publisher.

The title is linked to an address of the form:

```
https://ref.ly/res/<resourceId>/<version>/<offset>?len=<n>
```

That is an ordinary web URL. It opens the resource at that position in Logos for anyone with the resource, and it works outside Logos too, so the same link can go straight into your Markdown:

```markdown
> Quoted text from the resource …
>
> — [Author, *Resource Title*, p. 123](https://ref.ly/res/<resourceId>/<version>/<offset>?len=<n>)
```

Known limitation: the pasted quote may lose its original bold and italics.

Indent longer quotes (`ql-indent-1` in Logos, `> ` in Markdown) so readers can tell quoted sources from your own writing at a glance.

### 5.2 Anchors (and why inline citations export better)

Logos notes also support **anchors**. To make one, highlight a passage in a resource open in another panel, then in the note choose to create an anchor from the selection. Without a resource selection, the anchor falls back to a plain Bible-passage link.

Anchors have drawbacks for this workflow:

- They live **only in the note header**, not in the body next to the text they support.
- They are stored as internal links of the form `/books/<id>/references/...` and `/offsets/...`, which are not visible when you copy the note body.
- When a resource's sections run together, it can be hard to select exactly one section.

Inline `ref.ly` citations sit next to the quote, survive a copy of the note body, and work as normal links in Markdown on GitHub. That makes the repo self-contained: you can find and verify a source from the Markdown alone without opening Logos to look up an anchor.

### 5.3 Free, shareable links

`ref.ly` links open the passage in Logos for people who own the book. For everyone else they open the Logos web app, which may show only a preview or a sign-in or purchase prompt. In anything you share with people who may lack Logos:

- Link Bible references to [Biblia.com](https://biblia.com/), Faithlife's free online reader, which opens verses with no sign-in. The format is `https://biblia.com/bible/<translation>/<Book><chapter>.<verse>`, for example `https://biblia.com/bible/kjv1900/Eph2.8` or a range like `https://biblia.com/bible/esv/John3.16-21`. Book names can be abbreviated (`Eph`, `1Cor`, `Ps`). Translations that opened without sign-in in a check on 2026-10-11 include `kjv1900`, `leb`, `asv`, `esv`, `nkjv`, `nasb95`, `niv`, and `nrsvue`. The NET is there as `gs-netbible` (e.g. `https://biblia.com/bible/gs-netbible/John3.16`); `netbible2ed` (2nd edition) requires sign-in or purchase.
- Keep the `ref.ly` link on library quotes, and add a free source link where one exists (CCEL, New Advent, the confession sites in [Free resources](free-resources.md)).
- **Pop-ups, comparison, and NET notes.** Verse pop-ups (Reftagger) show verse text only. At each main passage, add a *Compare + NET notes* link to Bible Gateway, e.g. `https://www.biblegateway.com/passage/?search=John%203:16&version=NET;NRSVUE;NKJV;KJV`, which shows the passage in parallel with the NET translators' notes as footnotes (a 2nd-edition-era NET text; its copyright line reads 1996–2017). The free NET on Biblia.com is `gs-netbible` (e.g. `https://biblia.com/bible/gs-netbible/John3.16`); `netbible2ed` there requires sign-in or purchase. The full NET 2nd edition with all notes is free to read at [netbible.org](https://netbible.org/) and is available in Logos (*The NET Bible: Full Notes Edition*, 2nd ed.). Use full references in these links.
- `tools/md_to_logos_html.py --biblia kjv1900` turns plain references like `John 3:16` into Biblia links during conversion.

### 5.4 Verse pop-ups on a public site

This repo is published with GitHub Pages and Faithlife's free [Reftagger](https://faithlife.com/products/reftagger) script. Reftagger scans each page for Bible references and turns them into links that show the verse in a hover pop-up.

How it is configured here (`_includes/reftagger.html`; setting names checked against the live `RefTagger.js`):

| Setting | Value | Why |
|---|---|---|
| `bibleVersion` | `"NET"` | Reftagger maps `NET` to Biblia's `gs-netbible`. Its wording matched the NET 2nd edition on netbible.org in every verse checked. `netbible2ed` is **not** served to Reftagger (the pop-up shows an error), so it can't be used. |
| `convertHyperlinks` + `hyperlinkTestList: ["biblia.com"]` | on | Reftagger skips existing links by default; this adds pop-ups to the Biblia.com links in the text, and leaves other links (e.g. `ref.ly`) alone. |
| `noSearchTagNames` | `["code", "pre"]` | The default skips h1–h3. Overriding it lets references in headings get pop-ups, while code stays untouched. |
| `socialSharing` | `[]` | No share buttons. |

Limits to know:

- **Pop-ups show verse text only**, never the NET translators' notes. For notes and a parallel view, add a *Compare + NET notes* link to Bible Gateway at each main passage (section 5.3).
- **Only full references are tagged** (book, chapter, and verse). "v. 16" or "vv. 14–15" are ignored.
- **Pop-ups appear only on the published site**, not when you view files on github.com.

To do the same on your own public repo (for example, one made from the starter kit):

1. Copy `_config.yml`, `_includes/head.html`, and `_includes/reftagger.html` from this repo. They use GitHub Pages' built-in Jekyll with the `minima` theme; `README.md` becomes the home page and `.md` links are rewritten by `jekyll-relative-links`. `header_pages` in `_config.yml` sets the short top navigation.
2. Change `bibleVersion` to the translation you want, if Reftagger supports it (for example `"KJV"`, `"ESV"`, `"LEB"`). Test one pop-up in a browser after publishing.
3. In the repo's **Settings > Pages**, publish from the `main` branch, root folder. The site appears at `https://<user>.github.io/<repo>/` after a minute or two.
4. On long pages, use the kramdown auto table of contents: put `{: .no_toc}` under the page title and the "Contents" heading, then `* Contents` followed by `{:toc}`. It builds a nested list of every heading. (On github.com it shows as plain text; the website renders it.)

**Write full references.** Always write book, chapter, and verse ("John 3:16", "John 3:14–15"), not "v. 16" or "vv. 14–15", even when the chapter is obvious. Verse pop-ups and Logos's automatic Bible-reference links only recognize full references.

**Placeholders.** Write placeholders as `*[Placeholder: …]*` or `[ref.ly link]`, never with angle brackets, which the site treats as HTML and hides.

GitHub Pages for a **private** repo requires a paid GitHub plan, and even then the published site is public unless your organization's plan supports private Pages. Keep personal study notes out of any repo you publish.

## 6. Local desktop data

The desktop app keeps user data in a folder like:

```
C:\Users\<you>\Documents\<random>.mxq\
```

(The folder name is random per install; it may be on another drive if you moved it.) Inside are SQLite databases for your own data, for example:

- `NotesToolManager\notestool.db` for notes and notebooks
- other `*.db` files for highlights, favorites, layouts, and so on

Guidelines:

- **Copy the databases before opening them**, and never open them while Logos is running. Open the copies read-only with `sqlite3` or a database browser.
- **Book text is encrypted** in the resource files, so you cannot search it locally. Use the web app (or the desktop app) for full-text search of your books.
- **Beware stale copies.** If the data folder was ever moved, an older copy may remain under `C:\Users\<you>\AppData\Local\...`. Check modification dates to make sure you are reading the live one.
- Treat these files as read-only. Write notes through the app, not by editing the database.

## 7. The Logos Study Assistant

Logos includes an AI Study Assistant that can answer questions from your library.

- **Scope it to "Your books"** so answers draw on resources you own, and check which resources it actually cites.
- **Treat answers as leads, not quotations.** Open each cited resource, read the passage in context, and quote from the resource itself (using section 5.1), not from the assistant's summary.
- **Name the resources you want.** In testing, tradition-level questions ("what does tradition X teach…") sometimes drew on few or none of the owned resources for some traditions, while naming a specific resource or scoping to a single book worked better. Ask about specific books by title, then verify.
- **Test coverage yourself.** Coverage across resources and traditions may be uneven; some resources you own may not be retrieved. Ask matched questions (the same question framed for different traditions or sources you know are in your library) and compare which resources it cites; the [coverage testing kit](ai-coverage-test.md) gives a full procedure. If something you own never appears, note the resource, the question, and the answer, and report it to Faithlife.
- You can ask it to format answers so they paste cleanly into a note, then edit and verify before saving.

## 8. Comparing translations

Use the **Text Comparison** tool in Logos to show a passage in several versions side by side, then copy the parallel text into your Markdown sources file. Keep the full parallels in a separate sources file and quote only notable differences inline in the study itself, for example a verse where one version renders a key phrase differently from the others.

A footnoted default translation is useful as the base text, with checks against a few others on key verses.

## 9. Tips and gotchas

- **Canvas rendering limits selection.** The web app draws some resource text in a way that browser automation cannot easily select or read.
- **Limited view mode** (an accessibility setting in the web app) exposes text in a more accessible form, which helps automation select and read it. Turn it back off afterward if you do not normally use it.
- **The notes list lags.** After creating or switching notes, confirm the title in the editor before pasting or deleting.
- **Translator notes may not copy.** Some Bible notes display on screen but do not copy out; the publisher's public website may have the same notes.
- **Some resources are notes-only.** A study Bible's notes may be in your library without its Bible text.
- **Do not auto-overwrite notes.** Save the original to the repo before replacing or deleting any note.
- **Keep the repo private by default**, and publish selected material in a separate public repo.
- **Verify every quote** against the resource before sharing, especially text written from memory or summarized by an AI.
