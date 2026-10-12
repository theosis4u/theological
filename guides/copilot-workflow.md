---
title: "Using the Workflow with Microsoft Copilot and Logos"
date: 2026-10-11
topic: workflow
---

# Using the Workflow with Microsoft Copilot and Logos
{: .no_toc}

## Contents
{: .no_toc}

* Contents
{:toc}

---

## About this guide

This guide adapts the [Logos + GitHub workflow](logos-github-workflow.md) for someone who has **only Microsoft Copilot** and Logos. That might be Copilot in Edge or Windows, Microsoft 365 Copilot in Word, OneNote, or Teams, and perhaps GitHub Copilot in VS Code. There is no browser automation, shell agent, or script that drives Logos for you. Everything moves by copy and paste, which is slower but works, and keeps you in control.

> **About capabilities:** Copilot features, names, and licensing change often and differ between personal and work accounts and between tenants. The descriptions below summarize Microsoft's and GitHub's public documentation as of late 2026, with links. Check the linked pages and your organization's settings before relying on any feature.

Recommended first step: add this repo's files to a Copilot Notebook (or attach them) and run the onboarding prompt in [START-HERE.md](../START-HERE.md).

## 1. What Copilot can and can't do here

**Likely available, depending on your plan and tenant:**

- **Chat with file uploads.** You can attach documents (Word, PDF, text) to a chat and ask about them.
- **Copilot Notebooks** (Microsoft Copilot app and OneNote): a scoped workspace where you add reference files and set **custom instructions** that Copilot follows for that notebook. Microsoft's docs say answers are grounded in the references you add, which can include Word, PDF, text, OneNote pages, Copilot Pages, and (for licensed Microsoft 365 Copilot users) OneDrive or SharePoint files and folders. See [How Copilot Notebooks works](https://support.microsoft.com/en-us/microsoft-365-copilot/how-microsoft-365-copilot-notebooks-works), [Provide custom instructions for your notebook](https://support.microsoft.com/en-US/Microsoft-365-Copilot/provide-custom-instructions-for-your-microsoft-365-copilot-notebook), and [Add references to your notebook](https://support.microsoft.com/en-US/Microsoft-365-Copilot/add-references-to-your-microsoft-365-copilot-notebook).
- **Copilot Pages:** a persistent, editable page next to the chat that you can refine with Copilot and share. See [How Copilot Pages works](https://support.microsoft.com/en-US/Microsoft-365-Copilot/how-microsoft-365-copilot-pages-works).
- **Microsoft 365 Copilot in Word**, which can draft and rewrite in the document and refer to files you can access in OneDrive or SharePoint.
- **GitHub Copilot** in VS Code (or on github.com), which reads repository instructions from `.github/copilot-instructions.md`. See [Adding repository custom instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) and [About customizing Copilot responses](https://docs.github.com/en/copilot/concepts/response-customization).

**Not available:**

- Copilot **cannot open Logos**, see your library, or read your Logos notes. It only knows what you paste or upload.
- It cannot control local apps or your browser for you in a typical setup.
- Its general knowledge of theology is not your library. Treat any citation it produces from memory as unverified.

## 2. Workplace cautions (read first)

- **Follow your organization's data policy.** On a work account, prompts and files may be retained, logged, or subject to your company's compliance tools. Some employers do not allow personal use of work Copilot at all.
- **Keep personal faith notes on personal accounts** if your policy requires it. A personal Microsoft account with a Microsoft 365 Personal, Family, or Premium plan may offer some of the same features; check Microsoft's current plan pages.
- **Do not paste licensed book text in bulk.** Copy short passages you need to quote, with their citations, as you would for fair use in a paper. Don't upload whole resources or long extracts from your Logos library, and respect each publisher's license.
- **Don't share notebooks or pages** that contain personal notes with colleagues by accident; check sharing before you add references.

## 3. Store your method and profile

Start from the [method template](ai-theology-method-template.md), a [tradition pack](../traditions/), and the starter kit's `PROFILE.md` prompts. Then choose one place to keep them:

| Option | How |
|---|---|
| **Copilot Notebook instructions** (best if available) | Create a notebook such as "Bible study". Paste a condensed method (section 4 prompt below) into its **Instructions**. Add `PROFILE.md` and `METHOD.md` (saved as `.docx`, `.txt`, or `.md`) as references. |
| **Pinned document** | Keep `METHOD.md` and `PROFILE.md` as Word or text files in OneDrive. Attach them to each new chat, or start each chat by pasting them. |
| **Copilot Page** | Run the setup prompt below, send the result to a Page, edit it, and reuse it as a notebook reference. |
| **Personal custom instructions** | If your Copilot app offers personalization or custom instructions, paste the short version there. Availability varies; check your app's settings. |

Custom instruction boxes are usually short, so keep a **short version** (about 10–15 lines) for instructions and the **full method** as a reference file.

## 4. Ready-to-paste prompts

### 4.1 "Set up my method"

```text
I study Scripture using a written working method. Read the attached METHOD.md and PROFILE.md (or the text below).
1. Summarize the method in 12-15 short lines I can paste into custom instructions, keeping: request types and their lengths, source tiers, the rule to lead with <your tradition>, fairness to other traditions, "never invent a citation", and the quoting rules.
2. List anything unclear or contradictory and ask me about it.
3. From now on, at the start of each answer, state which request type you are using.
Do not add any theological positions that are not in my files.
```

### 4.2 "Clean this chat into Markdown"

```text
Below is a copied AI chat. Convert it into a Markdown file:
- Start with YAML front matter: title (short and descriptive), source (<URL or "copied from Copilot">), date (<YYYY-MM-DD>), project (<project>), topic (one of: <your topic folders>).
- Then "# <title>", then alternate "## User" and "## Assistant" sections in order.
- Remove interface text (Copy, Edit, Regenerate, "Sources", page numbers), fix broken line wraps, keep lists and quotations, and keep every link.
- Do not summarize, shorten, or reword the content.
Output only the Markdown, in a single code block.
---
<paste chat here>
```

Chat export varies: some Copilot apps let you export or share a conversation; otherwise select the conversation text and copy it. Long chats may need to be pasted in parts.

### 4.3 "Format for a Logos note"

Use this when you can't run the converter script.

```text
Convert the Markdown below into simple HTML for pasting into a Logos note. Rules:
- First line: <p><strong>TITLE</strong></p> with no blank paragraph above it.
- Use only <p>, <strong>, <em>, <ul>, <ol>, <li>, and <a href>.
- Headings become <p><strong>...</strong></p>.
- Put <p><br></p> between blocks.
- Quotations that start with ">" become <p class="ql-indent-1">...</p> (one per paragraph). Never use <blockquote>.
- Convert tables to bullet lists: "<li><strong>first cell</strong>: other cells separated by semicolons</li>".
- Keep every link and Bible reference exactly as written.
Output only the HTML in one code block.
---
<paste Markdown here>
```

To get the HTML into Logos as formatting rather than tags: save the output as `note.html`, open it in Edge, select all, copy, and paste into the note. Or skip HTML: paste the Markdown into **Word**, apply simple formatting (bold headings, lists, increased indent for quotes), then copy from Word into the Logos note.

### 4.4 "Verify these citations" checklist

Copilot cannot check your Logos library, so verification is yours. Paste this with a draft and use it as a checklist:

```text
For the draft below, list every quotation, citation, page or section number, and URL in a table with columns: item, where it appears, source claimed, and "needs checking because". Flag anything that looks paraphrased but is in quotation marks, any reference without a page or section, and any source you may have supplied from memory. Do not correct them; just list them.
```

Then, for each row:

- [ ] Open the resource in Logos and find the passage.
- [ ] Replace the quote with text copied via **Share > Copy** (citations on), so it carries the real citation and `ref.ly` link.
- [ ] Check Bible verses against the actual translation.
- [ ] Confirm confession or catechism section numbers.
- [ ] Delete anything you cannot find, or mark it "unverified".
- [ ] If you will share it, link Bible references to Biblia.com (e.g. `https://biblia.com/bible/kjv1900/John3.16`, free, no sign-in) and add a free source link next to library quotes where one exists, since `ref.ly` links may show non-owners only a preview or a purchase prompt.

## 5. The adapted workflow, step by step

1. **Ask.** Open your notebook (or a chat with your method attached) and use a prompt from the [prompt library](../prompts/).
2. **Feed it sources from Logos.** In a resource, select the passage and use **Share > Copy** with *Copy citations* and *Hyperlink copied citations* turned on (see the [setup checklist](setup-checklist.md)). Paste into the chat with "Use only this text when quoting this source." The `https://ref.ly/...` link travels with it. Keep extracts short.
3. **Compare translations.** Use Logos's Text Comparison tool, copy the result, and paste it into the chat.
4. **Draft.** Ask Copilot to write the study in Markdown with `>` for long quotes. If you use a Copilot Page or Word, keep quotes indented.
5. **Verify** with the checklist above.
6. **Save the source of truth** (section 6).
7. **Publish to Logos.** Convert with the script or the 4.3 prompt, or paste from Word, into a new note. Check the note title in the editor before pasting, because the notes list can lag. Headings will show as bold text, tables must become lists, and indented quotes need the indent style, not block quotes.

For a complete example of this flow for a group study, see the [John 3:16–21 group study handout](../examples/john-3-16-group-study.md).

To bring in older material (chats, posts, emails, documents), see [Starting points](starting-points.md); its cleanup prompts work in Copilot too.

## 6. Keeping the repo without git

You can keep the same folder structure from the [starter kit](../starter-kit/) without installing git:

- **GitHub web editor.** Create a private repo from the starter kit files (upload them on github.com), then use **Add file > Create new file** or the pencil icon to edit. Pressing `.` on a repo page opens the browser-based editor (github.dev) for multi-file edits. Commit from the web page.
- **OneDrive or SharePoint folder.** Keep the same folders and Markdown or Word files. Version history in OneDrive gives you basic history. Add the folder as a reference in a Copilot Notebook if your plan allows.
- **Either way**, keep `INDEX.md` updated by hand, or ask Copilot: "Here is my folder listing with titles and dates; produce INDEX.md grouped by topic, newest first."

## 7. Optional: the Python tools

If your machine allows Python, the scripts in [`tools/`](../tools/) still help:

- `md_to_logos_html.py` replaces the 4.3 prompt and is more consistent.
- `build_index.py` regenerates `INDEX.md`.
- `chat_pdf_to_md.py` imports chats printed to PDF (its layout settings may need tuning for Copilot's print format).

If Python isn't allowed, the prompts above cover the same steps.

## 8. GitHub Copilot in VS Code

If you have GitHub Copilot, VS Code makes a good study editor: Markdown preview, search across all your notes, and a chat that reads instructions stored in the repo.

1. Create a private repo from the [starter kit](../starter-kit/) and open it in VS Code (or github.dev).
2. Create `.github/copilot-instructions.md`. GitHub's docs describe it as repository-wide instructions in plain Markdown that Copilot applies to requests in that repository. Build it from the [method template](ai-theology-method-template.md):

   ```markdown
   # Instructions for this study repository

   This repo holds Bible studies in Markdown with YAML front matter (title, date, topic, source).
   Follow METHOD.md and PROFILE.md in the repo root.

   - Lead with <your tradition>'s reading; present other traditions fairly from their own primary texts, cited by section.
   - Default Bible text: <default translation>; compare <comparison translations> on key verses.
   - Lengths: quick question 150-400 words; passage study 600-1,200; doctrine comparison 1,000-1,800.
   - Never invent quotes, page numbers, section numbers, or URLs. Mark anything unverified.
   - Long quotes go in ">" blocks followed by "— [Author, *Title*, p. N](ref.ly link)". Keep ref.ly links exactly as pasted.
   - No tables in files meant for Logos notes; use lists.
   - New files: topic folder, name YYYY-MM-DD-short-slug.md, front matter, and add to INDEX.md.
   ```

3. Optionally add path-specific instructions, for example `.github/instructions/logos-notes.instructions.md` with front matter `applyTo: "class-notes/**"`, for rules that apply only to Logos-bound notes. GitHub documents this as supported in VS Code chat; check the docs for current support.
4. Use the [prompt library](../prompts/) in Copilot Chat, attaching the relevant files.
5. Paste Logos copies (with `ref.ly` links) into the Markdown yourself; GitHub Copilot cannot reach Logos either.
6. Commit from VS Code's Source Control panel, or from the web.

## 9. Quick reference

| Task | Copilot-only way |
|---|---|
| Method and profile | Notebook instructions plus reference files, or a pinned document |
| Quote a resource | Logos Share > Copy (citations + hyperlinks), paste into chat or draft |
| Import old chats | Copy or export the chat, then use prompt 4.2 |
| Make a Logos note | Script, prompt 4.3, or paste from Word |
| Keep history | Private GitHub repo (web editor) or OneDrive version history |
| Check citations | Prompt 4.4 plus the manual checklist |
