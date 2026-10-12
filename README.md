# theological
Theological Writings Produced With Grok

A public toolkit for studying Scripture with **Logos Bible Software**, a **GitHub Markdown repository**, and an **AI assistant**: keep your study work in plain text you control, share it as Logos notes, cite sources with links to the exact location, and give your assistant a clear, fair working method. Everything here is generic and can be adapted to any Christian tradition; no tradition is presented as the house view.

## Step 0: Start here

**New here? Read [START-HERE.md](START-HERE.md).** Give this repo to your AI assistant with the onboarding prompt; it will summarize the toolkit, interview you one question at a time, and draft your private `PROFILE.md` and `METHOD.md`.

## Map

| Folder / file | What it's for |
|---|---|
| [START-HERE.md](START-HERE.md) | Step 0: give the repo to your assistant and run the onboarding prompt |
| [guides/logos-github-workflow.md](guides/logos-github-workflow.md) | The main how-to: architecture, importing AI chats, writing and exporting Logos notes, citations, desktop data, Study Assistant, translation comparison |
| [guides/ai-theology-method-template.md](guides/ai-theology-method-template.md) | Fill-in working method for your AI assistant (request types, source tiers, verification, fairness, honesty, citation rules) |
| [guides/copilot-workflow.md](guides/copilot-workflow.md) | The same workflow using only Microsoft Copilot (and optionally GitHub Copilot) plus Logos, by copy and paste |
| [guides/starting-points.md](guides/starting-points.md) | Optional ways to seed a study repo from existing material (AI chats, X, email, Logos, documents, transcripts), then sort and commit it |
| [guides/free-resources.md](guides/free-resources.md) | Free scholarly alternatives to Logos, cross-tradition and by tradition, and how to use them with an AI assistant |
| [guides/setup-checklist.md](guides/setup-checklist.md) | Setup checklist and FAQ / pitfalls |
| [guides/ai-coverage-test.md](guides/ai-coverage-test.md) | Matched-prompt kit for testing an AI assistant's coverage of your library, with a bug-report template |
| [starter-kit/](starter-kit/) | Skeleton for your own **private** study repo |
| [traditions/](traditions/) | Starter packs for eight traditions, with text for the method's "your tradition first" slot |
| [prompts/](prompts/) | One prompt per request type, each with an example |
| [examples/](examples/) | Worked examples: a passage study (John 1:1–5) and a small-group handout (John 3:16–21), each with generated Logos-note HTML |
| [tools/](tools/) | Python scripts: Markdown→Logos HTML, chat PDF importer, index builder, note save server, notes DB reader |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to add a tradition pack; style rules |
| [LICENSE](LICENSE) | MIT for code, CC BY 4.0 for docs |

## Guides

- [Integrating Logos Bible Software with a GitHub Markdown repo and an AI assistant](guides/logos-github-workflow.md)
- [A working method and template for AI-assisted theological study](guides/ai-theology-method-template.md)
- [Using the workflow with Microsoft Copilot and Logos](guides/copilot-workflow.md)
- [Starting points: seeding a study repo from existing material](guides/starting-points.md)
- [Free resources for exegesis and theology (no Logos needed)](guides/free-resources.md)
- [Setup checklist and FAQ](guides/setup-checklist.md)
- [Testing an AI study assistant's coverage of your library](guides/ai-coverage-test.md)

## Tools

- [`tools/md_to_logos_html.py`](tools/md_to_logos_html.py): convert Markdown studies to Logos-note HTML
- See [tools/README.md](tools/README.md) for all scripts and usage.

## Quick start

0. Run the onboarding in [START-HERE.md](START-HERE.md).
1. Read the [workflow guide](guides/logos-github-workflow.md) and work through the [setup checklist](guides/setup-checklist.md).
2. Create your private study repo from the [starter kit](starter-kit/) (below).
3. Fill in `PROFILE.md` and `METHOD.md` using the [method template](guides/ai-theology-method-template.md) and your [tradition pack](traditions/).
4. Try a [prompt](prompts/) and compare the result with the worked examples: [passage study](examples/john-1-1-5-study.md) and [group study handout](examples/john-3-16-group-study.md).

## Using the starter kit

**Copy the folder** (simplest):

```bash
git clone https://github.com/theosis4u/theological.git
mkdir my-study-repo && cp -r theological/starter-kit/. my-study-repo/
mkdir my-study-repo/tools && cp theological/tools/*.py my-study-repo/tools/
cd my-study-repo && git init && git add . && git commit -m "Start study repo"
# then create a PRIVATE repo on GitHub and push to it
```

**Or use GitHub's template feature:** a repository owner can mark a repo as a template (Settings > General > "Template repository"), after which others click **Use this template** to create their own copy. This repo is not set up that way; if you want a one-click template, copy `starter-kit/` into its own repo and mark *that* repo as a template. Either way, make your study repo **private**.

## License

Code in `tools/` is under the MIT License; documentation and written content are under CC BY 4.0. Public-domain Bible text (KJV, WEB) is quoted where noted. See [LICENSE](LICENSE).
