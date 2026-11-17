# Movie Ratings

## What this is

Movie Ratings is a small web app for our study group. You enter a movie title, a rating from 1 to 5 and your name, and the app shows all ratings in a table. You can search movies by title.

## How to run it

You need Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000 in your browser. Stop it with `Ctrl+C`.

The entries are kept in memory: after a restart the list is empty again.

More details for Mac and Windows: [docs/how-to-run.md](docs/how-to-run.md)

## Team

| GitHub | Role |
|---|---|
| v-johns | Protecting `main` (ruleset, pull request template), movie fields, search, README |
| azra-sarac | Reviews, rating check 1–5, sorting, docs: how to run, glossary |
| ahmtekn0 | Board and issues, delete, count and average, docs: how we review |

## How we work

- Every piece of work starts as an issue on our board (Todo, In Progress, Done). Issues belong to one of three epics: Movies, Overview, Docs.
- One branch per issue, named after it, for example `9-search-by-title`.
- Nobody commits directly to `main`. A ruleset requires a pull request with one approval.
- Every pull request uses our template (What, Why, How to check) and closes its issue with `closes #n`.
- Another team member reviews with at least one comment on a line. If something must be fixed, they choose "Request changes".
- After the approval, the author merges with "Create a merge commit".
- Every pull request adds one line to the top of `CHANGELOG.md`, with the pull request number.
- Conflicts are solved on the laptop: merge `main` into the branch, fix, commit, push.

## Sources
- 2026-11-09: Course sheet "Team Project and Assessment 1" (v-johns), used for the checklist and our plan
- 2026-11-09: Expert sheet C "Protect main" (v-johns), used to set up the ruleset and the pull request template

## Use of AI

- 2026-11-09: Claude Code (ahmtekn0), used to plan epics and issues and to create issues #4#14 from our plan, checked on GitHub
- 2026-11-09: Claude (v-johns), used to plan the work from the assignment, checked against the course sheets
- 2026-11-12: Claude Code (ahmtekn0), used to draft my review and approval on PR #15, checked by reading the diff myself
- 2026-11-12: Claude Code (ahmtekn0), used to help write docs/how-we-review.md (PR #16), checked by reading every section
- 2026-11-12: Claude (v-johns), used to explain the field changes for #4 and the Git steps, checked with `git show` and the review
- 2026-11-15: Claude (azra-sarac), used to explain Git steps and for drafts of docs/how-to-run.md, docs/glossary.md and the sorting line in main.py, checked by reading every line, comparing with the README and testing the commands myself
- 2026-11-15: Claude (v-johns), used to explain the search filter (#9) and to draft the README sections (#10), checked line by line with `git diff`
- 2026-11-16: Claude Code (ahmtekn0), used to add the review order and solve the CHANGELOG merge conflict in PR #16, checked by reading the final files
- 2026-11-16: Claude Code (ahmtekn0), used to write and test the count and average feature in PR #27, checked by running the app with different ratings
- 2026-11-16: Claude Code (ahmtekn0), used to test PR #21 and draft my reviews on #21 and #22, checked by reading the comments
- 2026-11-16: Claude Code (ahmtekn0), used to solve CHANGELOG conflicts in #16 and #27 and merge them, checked by running the app
- 2026-11-16: Claude (v-johns), used to prepare my reviews of other pull requests, checked by reading the changes myself in "Files changed"
- 2026-11-17: Claude Code (ahmtekn0), used to write and test the delete feature in PR #28, checked by running the app and reading every line
- 2026-11-17: Claude Code (ahmtekn0), used to answer the review on PR #28, solve its CHANGELOG conflict and merge it, checked by running the app
- 2026-11-17: Claude (v-johns), used to resolve the merge conflicts in main.py and CHANGELOG.md for #9 and #10 and to fill in this section, checked with `git diff` and by reading the final files