# demo-ai-pr-workflow

A live demo of a **fully AI-driven PR workflow** where:

- AI raises the PR
- AI (Claude Code) reviews the code
- Human stakeholder clicks **Approve** (the only human action)
- AI bot executes the merge — no human can merge to `main` directly

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Fork / Feature Branch                                  │
│  AI or engineer pushes code changes here                │
└─────────────────────────┬───────────────────────────────┘
                          │  Opens PR
                          ▼
┌─────────────────────────────────────────────────────────┐
│  main (branch-protected)                                │
│                                                         │
│  Rules:                                                 │
│  ✓ Require PR before merging                            │
│  ✓ Require 1 approving review (from stakeholder)        │
│  ✓ Block direct pushes                                  │
│  ✓ Merge bypass: BOT_GITHUB_TOKEN only                  │
│    → Regular accounts and even stakeholders cannot      │
│      execute the merge. Only the bot can.               │
└─────────────────────────────────────────────────────────┘
```

## The Flow

1. **PR opened** → `ai-review.yml` triggers
2. Claude Code reviews the diff + test results, posts a comment on the PR
3. **Stakeholder reads** Claude's review + the code diff
4. **Stakeholder clicks Approve** (only human action in the entire flow)
5. `ai-merge.yml` triggers → verifies approver is authorized
6. Bot posts "merging now..." comment → executes `gh pr merge`
7. PR is merged by the bot token — GitHub shows "Merged by [bot account]"

## Required Secrets

Set these in **Settings → Secrets → Actions**:

| Secret | Description |
|--------|-------------|
| `ANTHROPIC_API_KEY` | Claude API key for code review |
| `BOT_GITHUB_TOKEN` | PAT from the bot account (needs `repo` + `workflow` scopes) |
| `AUTHORIZED_APPROVERS` | Comma-separated GitHub usernames allowed to approve (e.g. `SHAI-ankur-pratap,stakeholder2`) |

## Branch Protection Setup

In **Settings → Branches → Add rule for `main`**:

- [x] Require a pull request before merging
- [x] Require approvals: **1**
- [x] Require status checks to pass: `Claude Code Reviews PR`
- [x] Restrict who can push to matching branches
  - Add only: **the bot account username**
- [x] Do not allow bypassing the above settings (except for bot account listed above)

## Demo Script (Live In-Person)

```bash
# 1. Create a feature branch and make a change
git checkout -b feature/add-power-function
# ... make a change to src/app.py ...

# 2. Push the branch
git push origin feature/add-power-function

# 3. Open a PR (as the bot or as yourself)
gh pr create --title "feat: add power function" --body "Adds a power/exponentiation operation to the calculator."

# 4. Watch GitHub Actions — Claude reviews in ~60 seconds
# 5. Stakeholder clicks Approve on the PR
# 6. Watch GitHub Actions — bot merges in ~15 seconds
```

## Why Forking?

The **forking approach** keeps AI work in a separate namespace:
- Fork gives the AI bot its own space to stage changes
- Main repo stays clean — only PRs from the fork (or branches) land there
- Permissions are cleanly separated: fork is open, main is locked

To demo the fork variant:
```bash
# Fork the repo under the bot account, make changes in the fork
gh repo fork SHAI-ankur-pratap/demo-ai-pr-workflow --clone
# Work in the fork, then open PR from fork → upstream main
gh pr create --repo SHAI-ankur-pratap/demo-ai-pr-workflow
```
