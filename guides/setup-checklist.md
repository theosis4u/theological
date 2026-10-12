---
title: "Setup Checklist and FAQ"
date: 2026-10-11
topic: workflow
---

# Setup Checklist and FAQ
{: .no_toc}

## Contents
{: .no_toc}

* Contents
{:toc}

---

**Shortcut:** you can hand this whole repo to an AI assistant and let it do most of this for you; see [START-HERE](../START-HERE.md). For which accounts and tools to connect, see [What to connect for the best results](../START-HERE.md#what-to-connect-for-the-best-results).

A checklist for setting up the [Logos + GitHub workflow](logos-github-workflow.md), plus answers to the problems people run into most.

## Checklist

### Repository
- [ ] Create a **private** GitHub repo for your studies (start from the [starter kit](../starter-kit/)).
- [ ] Fill in `PROFILE.md` and `METHOD.md` (from the [method template](ai-theology-method-template.md) and a [tradition pack](../traditions/)).
- [ ] Copy `tools/` into the repo; install Python 3 (and `pip install pymupdf` for the chat importer).
- [ ] Decide what, if anything, goes in a separate **public** repo.

### Logos copy and citation settings

*Skip the Logos sections if you don't use Logos; use your [tradition pack](../traditions/README.md)'s free online sources and the [free resources](free-resources.md) guide instead.*

- [ ] In Logos, open the copy settings (from **Share > Copy** in a resource, or Program Settings) and turn on **Copy citations**.
- [ ] Turn on **Hyperlink copied citations**, so each citation carries a `https://ref.ly/...` link.
- [ ] Choose a **citation style** (for example APA, Chicago, or SBL) and use it consistently.
- [ ] Test once: copy a sentence from a study Bible, paste into a note, and confirm the citation line and link appear.
- [ ] For anything you share with people who may not have Logos, open one `ref.ly` link while signed out to see what they will see (it may show only a preview or a purchase/sign-in prompt), and use Biblia.com links for Bible references (e.g. `https://biblia.com/bible/kjv1900/John3.16`, free, no sign-in). Add a free source link (CCEL, New Advent, confession sites) next to library quotes where one exists.

### Notes
- [ ] Create a notebook for each class or study series.
- [ ] Convert one Markdown study with `tools/md_to_logos_html.py` and paste it into a test note to confirm formatting.
- [ ] Set up the export path (`tools/note_save_server.py`) and test a round trip.

### Free library (optional)
- [ ] Decide on a Faithlife account: a dedicated one on an assistant's own inbox, or your personal email. Approve the sign-up yourself; store the password in a password manager.
- [ ] Claim the current free books and set a monthly reminder (see [Building a free Logos library](free-resources.md#building-a-free-logos-library)).
- [ ] Bookmark the $0 store search and the free-book alert options.

### AI features
- [ ] Check which AI features your Logos subscription includes. Logos's AI tools (such as the Study Assistant and AI-assisted search) and their usage limits or credits depend on your plan and change over time; see Logos's current pricing and help pages rather than relying on this guide.
- [ ] Set the Study Assistant's scope to **Your books** when you want answers from your library.
- [ ] Run the [coverage test](ai-coverage-test.md) for the traditions you study.

### Desktop data (optional)
- [ ] Find your data folder: `C:\Users\<you>\Documents\<random>.mxq\` (or wherever you moved it).
- [ ] Back it up by copying it while Logos is closed.

## FAQ and pitfalls

**My indented quotes vanished when I pasted.**
The Logos note editor strips `<blockquote>`. Use `<p class="ql-indent-1">` paragraphs instead (the converter does this by default).

**Headings turned into bold text.**
Expected. The note editor does not keep heading levels; bold paragraphs work as section headers.

**My table disappeared.**
Notes cannot hold tables. Convert rows to bullet list items (the converter does this).

**The note title is wrong, or there is a blank line at the top.**
The first line of the note becomes its title. Start with the title line and no blank paragraph above it.

**I pasted into the wrong note.**
The notes list can lag behind clicks. Before pasting, check the title shown in the editor itself, not just the highlighted list item.

**The HTML pasted as raw tags.**
It went in as plain text. Copy it as rich text: open the HTML in a browser (served from `python3 -m http.server`, since some automation blocks `file://` pages) and copy from the rendered page, or load the clipboard with `xclip -selection clipboard -t text/html -i note.html` on Linux.

**I can't select text in a resource with automation or a screen reader.**
The web app renders resource text on a canvas, which limits selection. The web app's **limited view mode** (an accessibility setting) exposes text in a more accessible form. Turn it back off afterwards if you don't need it.

**Some Bible notes show on screen but won't copy.**
Some resources restrict copying. Check whether the publisher offers the notes publicly online, or cite the location and paraphrase.

**My anchor only linked to a Bible passage, not the resource.**
An anchor made without a selected resource range falls back to a passage link. Select text in the resource first, then create the anchor from the selection. For notes you will export, prefer inline copied citations instead (see the [workflow guide](logos-github-workflow.md#5-citations-inline-links-instead-of-anchors)).

**The desktop notes database looks out of date.**
If the data folder was moved, an older copy may remain under `C:\Users\<you>\AppData\Local\...`. Compare modification dates and use the live one. Always copy the database before opening it, and never open it while Logos is running.

**Can I search book text from the desktop files?**
No. Resource text is encrypted. Use Logos search (desktop or web).

**The Study Assistant answered from general knowledge.**
Confirm the scope is **Your books**, try naming a specific resource, and verify any claim by opening the cited resource. See the [coverage test](ai-coverage-test.md).
