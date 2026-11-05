# Public course publishing protocol

This repository is **not** the content production workspace. All 90 videos and their 90 learning guides are intended to be produced and approved before the 30-day public release begins.

## Private → public

Local preparation exception: a user-requested complete guide may be staged at its expected path in the local public checkout with catalog status `prepared` and `guide_path: null`. The validator requires the file to exist but the roadmap does not expose a live link. Keep production-only assets in the private workspace. Transition to `published` only through the approved release process below; no push or PR is implied by local preparation.

1. Complete research, examples, diagrams, guide, video, QA and human sign-off privately.
2. Keep unreleased content in the private local/source workspace; **a public GitHub pull request is publicly readable** even when unmerged.
3. Near the approved release slot, open a PR containing only the approved public lesson and assets, plus the manifest update.
4. Ensure `data/course_manifest.json` changes the matching record from `planned` to `published` and sets `guide_path` to exactly `expected_path`.
5. Run `python tools/course.py check` and regenerate `ROADMAP.md` with `python tools/course.py roadmap`. Review the resulting diff.
6. Merge the lesson PR and verify that the real GitHub link loads in a private browser session.
7. Publish the corresponding Reel only after the lesson link is live; verify the correct ID/URL mapping.
8. When someone comments `GUIDE`, provide the exact public lesson link through the **approved, tested** response process. Do not claim automatic DM delivery until it is actually configured and verified.
9. Record the public URLs and release evidence in the *private production tracker*, not in this repo.

## Proposed release slots

Three educational videos per day during a 30-day **release window**, subject to human approval and change before launch. Publishing slots are not an algorithm guarantee.

The public roadmap may show upcoming topic titles, but must never link to uncreated guides or imply planned lessons are already available.

## Release safeguards

- Do not expose draft media, unreviewed content, internal notes or private tracker events.
- No automated GitHub merges, Instagram publishing, external messaging or paid API calls without prior approval.
- If link verification fails, hold the Reel; do not send learners to a broken guide.
- Fix published material transparently through a normal reviewed pull request.
