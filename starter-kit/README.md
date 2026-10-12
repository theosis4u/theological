# Study Repo Starter Kit

A ready-made skeleton for a **private** Bible study repository that works with Logos and an AI assistant. It follows the [workflow guide](../guides/logos-github-workflow.md) and the [method template](../guides/ai-theology-method-template.md).

## How to use it

Recommended first: run the onboarding prompt in [START-HERE.md](../START-HERE.md); your assistant will draft `PROFILE.md` and `METHOD.md` for you.

1. Create a new **private** repository on GitHub (for example `my-study-repo`).
2. Copy the contents of this `starter-kit/` folder into it (see the root README for copy commands).
3. Copy the `tools/` folder from this repo alongside it if you want the scripts.
4. Fill in `PROFILE.md` (who you are as a student and what you want) and `METHOD.md` (your working method, starting from the template and a [tradition pack](../traditions/)).
5. Give your AI assistant `PROFILE.md` and `METHOD.md` at the start of each session, or point it at the repo.
6. Save every study as `YYYY-MM-DD-short-slug.md` in a topic folder, using the front matter in `_front-matter-example.md`, and rebuild `INDEX.md` with `python3 tools/build_index.py . -o INDEX.md`.

Optional: seed it from material you already have (AI chats, posts, emails, Logos notes, documents) using [Starting points](../guides/starting-points.md).

## Folders

| Folder | For |
|---|---|
| `passage-studies/` | Studies of a specific passage |
| `doctrine/` | Topic and doctrine comparisons |
| `debates/` | Analyses of debates, posts, and articles |
| `class-notes/` | Notes and handouts for a class or study group |
| `chats/` | Imported AI chats (one subfolder per topic if you like) |
| `sources/` | Parallel translations and copied source quotes with citations |
| `templates/` | Your old prompts or query templates, for reference |
| `exports/` | Raw HTML exported from Logos notes before conversion |

Rename or add folders freely; `build_index.py` groups by the `topic` field first, then by folder.

Keep this repo private by default. Publish only what you choose, in a separate public repo.
