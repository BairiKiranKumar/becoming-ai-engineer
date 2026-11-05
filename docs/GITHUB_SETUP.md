# Set up the public repository

**Recommended repository name:** `becoming-ai-engineer`  
**Visibility:** Public (only after the owner approves publication)  
**Default branch:** `main`

## Repository About text

**Description (copy/paste):**

> Free, visual-first AI Engineering course: 30 days, 90 connected lessons, diagrams, practical examples and hands-on projects. Beginner to production AI.

**Website / social link:** https://www.instagram.com/kiranbuildswithai/

**Topics:** `ai-engineering`, `learn-ai`, `generative-ai`, `llm`, `rag`, `ai-agents`, `mcp`, `python`, `typescript`, `ai-course`

## Before publishing

- [ ] Approve the repository owner and name (availability under the account has not been checked).
- [ ] Review `README.md`, `ROADMAP.md`, `GETTING_STARTED.md`, and the 90 public topic titles.
- [ ] Decide and add full content/code licenses (see `docs/LICENSING.md`).
- [ ] Choose a private channel for sensitive security reports or enable GitHub's private vulnerability reporting.
- [ ] Confirm the public repo contains **no** video-production workspace files or unreleased content.
- [ ] Run `python tools/course.py check`; it should report `0/90` lessons published before release.

## Create the repository

Create an **empty** public repository named `becoming-ai-engineer` in GitHub. Do not initialize it with a new README, `.gitignore`, or license because the starter already includes those files (except the deliberately undecided licenses).

Use a separate local directory such as `C:\Projects\becoming-ai-engineer` rather than turning the private AI Video Editor workspace itself into the public repository.

From a terminal opened **inside** the unzipped `becoming-ai-engineer` directory:

```powershell
git init -b main
git add .
git commit -m "docs: initialize Becoming an AI Engineer course"
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/becoming-ai-engineer.git
git push -u origin main
```

Replace `<YOUR_GITHUB_USERNAME>` with the owner you select. Do not run these commands before authorizing the public repo; publishing is a deliberate action.

## Suggested repository settings

- **Issues:** On, so learners can report corrections.
- **Actions:** On, with `Course integrity` checks. The included workflow validates the public catalog and roadmap but does not publish anything.
- **Branch rules:** Require PR review and passing `Course integrity` check before merge, once the first workflow run is available. Keep human release approval mandatory.
- **Discussions:** Optional, once there is time to moderate questions.
- **Pages:** Not required; GitHub's Markdown pages are sufficient to start.

## When a lesson is approved

Follow [`docs/PUBLISHING.md`](PUBLISHING.md). Public PRs expose their contents, so never use public branches to stage unreleased course material well in advance. Publish only an approved individual guide, update `data/course_manifest.json`, regenerate `ROADMAP.md`, and confirm the live link before the corresponding Reel is posted.

## How it relates to the private production workspace

- Private source of truth: `C:\Projects\AI Video Editor\ai-engineer-series\tracker\lessons.json` and its production SOP.
- Public source of truth: this repository's `data/course_manifest.json` for **publicly visible guide status only**.
- Immutable IDs (`D01L01` to `D30L03`) and `expected_path` connect the two.
- The human publisher verifies that the public status is updated **after** the corresponding private production approval; do not synchronize private notes, approvals, footage, or other confidential fields into this public manifest.
