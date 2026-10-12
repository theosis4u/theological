# Start Here

The recommended first step: hand this repository to your AI assistant and let it interview you, then build your own **private** study setup from the templates here. It takes about 15–30 minutes.

## 1. Give your assistant the repo

Use whichever method your assistant supports:

| Assistant can… | Do this |
|---|---|
| Browse the web or read GitHub | Paste the repo URL: `https://github.com/theosis4u/theological` |
| Accept file uploads | On GitHub, click **Code > Download ZIP**, then upload the ZIP (or unzip and upload key files) |
| GitHub Copilot (VS Code) | Clone or open the repo in VS Code (or press `.` on the GitHub page for github.dev) and use Copilot Chat there |
| Microsoft 365 Copilot | Put the files in OneDrive and add them as references in a **Copilot Notebook** (see the [Copilot guide](guides/copilot-workflow.md)) |

**If your chatbot can't read repos or ZIPs**, upload or paste just these files:

1. [README.md](README.md)
2. [guides/ai-theology-method-template.md](guides/ai-theology-method-template.md)
3. [traditions/README.md](traditions/README.md) (plus your tradition's pack)
4. [guides/starting-points.md](guides/starting-points.md)

## 2. Onboarding prompt

Paste this after giving the assistant the repo or files:

```text
I'm setting up a Bible study workflow using the repository (or files) I just gave you. Please do the following, in order.

A. READ AND SUMMARIZE
Read the repo: README, START-HERE, guides/, traditions/, prompts/, examples/, starter-kit/, tools/.
Summarize in plain words (under 250 words) what it offers and how the pieces fit together. If you could not open some files, list them.

B. INTERVIEW ME, ONE QUESTION AT A TIME
Ask these one at a time, wait for my answer, and offer choices where useful:
1. Which tradition should lead? Offer the packs in traditions/ (Eastern Orthodox, Roman Catholic, Reformed/Presbyterian, Lutheran, Anglican, Wesleyan/Methodist, Baptist, Pentecostal), plus "other" and "ecumenical / compare traditions".
2. My default Bible translation, and 1-3 comparison translations.
3. Study resources I own: do I use Logos (desktop, web, both)? Which study Bibles, commentaries, catechisms or confessions?
4. What I use this for: group study, teaching, personal study, debate or social media, writing.
5. Tone and length preferences, and anything I dislike in AI answers.

C. SOURCES TO CONNECT OR IMPORT
Ask which existing material I want to bring in: AI chat history (Grok, ChatGPT, Claude, Copilot), my X posts, email through connected apps, Logos notes, documents, lecture transcripts.
For each, tell me plainly what YOU can actually access or connect to in this environment, and what I must export and upload myself (use guides/starting-points.md). If you can't do something, say so.

D. PLAN
Propose a folder layout for my PRIVATE study repo (based on starter-kit/) and an import plan that starts with an inventory (titles, dates, sources, counts) before converting anything. Wait for my approval.

E. DRAFT MY FILES
Produce a filled-in PROFILE.md and METHOD.md from starter-kit/PROFILE.md and guides/ai-theology-method-template.md, using my answers and my tradition pack's "your tradition first" text. Mark anything you assumed as [check]. Show them for review; don't treat them as final.

RULES FOR YOU
- One question at a time.
- Don't invent capabilities, files, tools, or access you don't have.
- Read-only on my sources: never delete, edit, send, or post anything.
- Private by default: assume everything goes in a private repo unless I say otherwise.
- Never invent quotes, citations, page numbers, or links; mark anything unverified.
- Keep my answers out of anything public.
```

## 3. Example (first few exchanges)

> **User:** *(uploads the ZIP and pastes the onboarding prompt)*
>
> **Assistant:** Here's what this repo offers. It's a toolkit for studying Scripture with Logos Bible Software, a private Markdown repository, and an AI assistant. The **guides** explain the workflow: keeping studies as Markdown files you control, turning them into Logos notes, and quoting sources with links back to the exact spot in a book. The **method template** is a set of standing instructions for an assistant: answer lengths by request type, ranked sources, fairness to other traditions, and never inventing citations. **Tradition packs** fill in that template for eight traditions. The **prompts** and **examples** show finished studies. The **starter kit** is a skeleton for your own private repo, and **tools** are small Python scripts for converting notes and importing chats. I opened every folder.
>
> First question: which tradition should lead in your studies? Options: Eastern Orthodox, Roman Catholic, Reformed/Presbyterian, Lutheran, Anglican, Wesleyan/Methodist, Baptist, Pentecostal, other, or ecumenical (compare traditions side by side).
>
> **User:** Lutheran, but I often compare with Catholic and Reformed views.
>
> **Assistant:** Got it: Lutheran first, with Catholic and Reformed as regular comparisons. Next: what's your default Bible translation, and which one to three translations do you want to compare against?
>
> **User:** ESV by default; compare with the KJV and NRSVue.
>
> **Assistant:** Thanks. Do you use Logos, and if so, desktop, web, or both? Which study Bibles or confessional resources do you own?
>
> *(…the interview continues…)*
>
> **Assistant:** About importing: I can read files you upload here, but I can't log in to your other AI accounts or your email from this chat. For ChatGPT history, use Settings > Data controls > Export data and upload the ZIP; I'll start with an inventory and won't convert anything until you approve.

## 4. What to do next

- Create your private repo from the [starter kit](starter-kit/) and commit the reviewed `PROFILE.md` and `METHOD.md`.
- Work through the [setup checklist](guides/setup-checklist.md), especially the Logos citation settings.
- Read the [main workflow guide](guides/logos-github-workflow.md), or the [Copilot guide](guides/copilot-workflow.md) if Copilot is all you have.
- Import older material with [starting points](guides/starting-points.md).
- Try a [prompt](prompts/) and compare with the [examples](examples/).
- Check your assistant's library coverage with the [coverage test](guides/ai-coverage-test.md).
