# How we review pull requests

## Who reviews
Every pull request is reviewed by one other team member, never by the author.
We take turns, so everyone reviews the work of the others.

## What we check
- [ ] The PR description says what changed and why, and has `closes #n`
- [ ] There is one new line in `CHANGELOG.md`
- [ ] Commit messages say what changed
- [ ] The change does only what the issue asks for

## Comments
We leave comments on the exact line in "Files changed".
We write short, friendly and clear comments, and suggest a fix when we can.

## Approve or Request changes
- **Approve:** everything in the checklist is fine, small optional ideas are okay.
- **Request changes:** something is broken, missing or does not match the issue.

## After the review
After the approval, the author merges the pull request.
The issue closes by itself and the card moves to Done on the board.

## Example
In #15, the docstring in `main.py` was broken. The review asked for changes, the author fixed it, then the PR was approved.