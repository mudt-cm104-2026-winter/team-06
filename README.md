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

<!-- One entry per source, added on the day you use it:
- 2026-11-05: <title or link>, used for <what>
-->

## Use of AI

<!-- One entry per use, added on the day you use it:
- 2026-11-05: <tool>, used for <what>, checked by <how you checked the result>
"none" is a valid entry.
-->
