# Live Demo Script — AI-Driven PR Workflow

## The Story (tell this in the room)

> "Once a developer opens a PR from their fork, they're done. No review meetings,
> no waiting for a senior engineer. Claude reviews the code, scans for security issues,
> and posts its findings. The stakeholder gets one question: Allow or Deny.
> They click one button. Claude merges. No human touches main directly — ever."

---

## Setup (do this before the demo)

### 1. Add secrets to the repo

Go to: **Settings → Secrets and variables → Actions → New repository secret**

| Secret | Value |
|--------|-------|
| `ANTHROPIC_API_KEY` | Your Claude API key |
| `BOT_GITHUB_TOKEN` | PAT from bot account with `repo` + `workflow` scopes |
| `AUTHORIZED_APPROVERS` | `SHAI-ankur-pratap` (comma-separated stakeholder usernames) |

### 2. Check branch protection is active

Go to: **Settings → Branches → main**

Confirm:
- ✅ Require a pull request before merging
- ✅ Require approvals: 1
- ✅ Block direct pushes

> Only `BOT_GITHUB_TOKEN`'s account can merge. Everyone else is blocked — including the approver.

---

## The Demo Flow (run this live)

### Step 1 — Developer forks the repo

Have a second GitHub account (or colleague) fork the repo:

```
https://github.com/SHAI-ankur-pratap/demo-ai-pr-workflow
→ Fork → their personal account
```

### Step 2 — Developer makes a change on their fork

```bash
git clone https://github.com/<their-fork>/demo-ai-pr-workflow
cd demo-ai-pr-workflow
git checkout -b feature/add-modulo

# Edit src/app.py — add a modulo() function:
# def modulo(a: float, b: float) -> float:
#     if b == 0:
#         raise ValueError("Cannot modulo by zero")
#     return a % b

git add src/app.py
git commit -m "feat: add modulo operation"
git push origin feature/add-modulo
```

### Step 3 — Developer opens PR from fork → main

```bash
gh pr create \
  --repo SHAI-ankur-pratap/demo-ai-pr-workflow \
  --title "feat: add modulo operation" \
  --body "Adds modulo (%) to the calculator."
```

Or via GitHub UI: their fork → Pull requests → New pull request → base: `SHAI-ankur-pratap/demo-ai-pr-workflow:main`

### Step 4 — Watch Claude review automatically (~60 seconds)

GitHub Actions fires `ai-review.yml`. Claude Code:
1. Reads the PR diff from the fork
2. Runs a code review (correctness, edge cases, quality, tests)
3. Runs a security scan
4. Posts the full review as a PR comment

**Point at the screen:** "The engineer did nothing. Claude found the PR, read it, and posted this review. No one asked it to."

### Step 5 — Stakeholder clicks Approve (the only human action)

Go to the PR on GitHub → **Files changed** → **Review changes** → **Approve** → **Submit review**

That's the one human click. Nothing else.

### Step 6 — Watch Claude merge automatically (~15 seconds)

GitHub Actions fires `ai-merge.yml`. Claude bot:
1. Verifies the approver is in the authorized list
2. Posts "merging now" comment
3. Executes `gh pr merge --squash`
4. Posts merge confirmation: "Merged by Claude Code bot — no human pushed to main"

**Point at the commit history:** The merge shows as committed by the bot account. No engineer's name on the main branch merge. No stakeholder's name either. Just the bot.

---

## What to say at each step

| Moment | What to say |
|--------|-------------|
| PR opened | "The engineer's job is done. They opened the PR. Everything from here is AI." |
| Claude posts review | "This took 60 seconds. A human review takes hours, sometimes days." |
| Approve click | "This is the only human action in the entire flow. One click." |
| Claude merges | "Notice whose name is on the merge commit. Not mine. Not yours. The bot." |
| Show branch protection | "Try to push directly to main right now. You can't. Nobody can except the bot." |

---

## Why the fork approach?

| Without fork | With fork |
|-------------|-----------|
| Engineers have write access to the org repo | Engineers only have access to their own fork |
| Risk of accidental direct commits to branches | Main org repo is read-only to engineers |
| Hard to audit "who touched what" | Every engineer's work is isolated in their fork |
| Access control is per-branch | Access control is at the repo level — cleaner |

The fork is the engineer's workspace. The org repo is Claude's responsibility.

---

## Architecture diagram (show this on screen)

```
Developer's Personal Fork
github.com/<dev>/demo-ai-pr-workflow
         │
         │  git push (to their fork only)
         │
         ▼
  Opens PR ──────────────────────────────────────────┐
                                                      │
                                                      ▼
                              SHAI-ankur-pratap/demo-ai-pr-workflow
                              ┌──────────────────────────────────┐
                              │  main (strictly protected)        │
                              │                                   │
                              │  GitHub Actions fires:            │
                              │  1. Claude reviews PR diff        │
                              │  2. Claude scans for security     │
                              │  3. Posts findings as comment     │
                              │                                   │
                              │  Stakeholder notified             │
                              │        │                          │
                              │   ALLOW / DENY                    │
                              │        │                          │
                              │  If ALLOW:                        │
                              │  Claude bot executes merge        │
                              │  (only identity with push access) │
                              └──────────────────────────────────┘
```
