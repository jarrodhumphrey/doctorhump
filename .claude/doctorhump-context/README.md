# doctorhump Context Documentation

This folder contains comprehensive context documentation for the doctorhump.com project. These files are designed to quickly onboard Claude Code (or any AI assistant) to the project without needing to explore the entire codebase.

## Purpose

To eliminate the laborious "getting on the same page" process at the start of each Claude Code session. Instead of exploring files, reading git history, and asking questions, Claude can read these 5 curated documents and be immediately productive.

## Files in This Folder

### 1. [overview.md](overview.md)
**What doctorhump is and why it exists**
- Brand identity (doctorhump - lowercase, one word)
- Three core pillars (AI, Case Race, Personal)
- Mission and audiences
- Content resources (testimonials, planning docs)
- Development philosophy
- Key reminders for Claude

### 2. [architecture.md](architecture.md)
**How the site is structured and organized**
- File structure (root vs /docs folder)
- URL structure (current and aspirational)
- Page-by-page breakdown
- Navigation strategy
- Content management approach
- Technical decisions and rationale

### 3. [styles.md](styles.md)
**Design system and visual guidelines**
- Color palette (ice theme + warm amber accents)
- Typography standards
- Layout principles
- Component styles (cosmic buttons, carousels, etc.)
- Animations and motion
- Design philosophy (simplistic, beautiful, cool)
- Consistency checklist

### 4. [deployment.md](deployment.md)
**Technical setup and deployment workflow**
- Hosting platform (Azure Static Web Apps)
- Git workflow and branch strategy
- Deployment process (GitHub Actions)
- Local development setup
- Performance optimization
- Troubleshooting common issues

### 5. [current-priorities.md](current-priorities.md)
**What's done, what's next, and what needs attention**
- Completed features
- Incomplete features and gaps
- Technical debt
- Content gaps
- Recommended next steps (short/medium/long-term)
- Open questions
- Success metrics

## How to Use

### For Claude Code Sessions

At the start of any new session, run:
```
/doctorhump-context
```

This slash command will instruct Claude to read all 5 files in order and get completely up to speed.

### For Human Developers

If someone new joins the project (or Jarrod needs a refresher), read these files in order:
1. overview.md (understand the "why")
2. architecture.md (understand the "what")
3. styles.md (understand the "how it should look")
4. deployment.md (understand the "how to ship it")
5. current-priorities.md (understand the "what's next")

Total reading time: ~15-20 minutes for complete context.

## Maintenance

**These files should be updated when:**
- Major features are completed (update current-priorities.md)
- New pages are added (update architecture.md)
- Design patterns change (update styles.md)
- Deployment process changes (update deployment.md)
- Brand strategy shifts (update overview.md)

**Who maintains:** Jarrod or Claude during sessions (update as you go)

**Frequency:** After any significant milestone or at end of major work sessions

## Benefits

✅ **Faster onboarding** - No need to explore codebase from scratch every session
✅ **Consistency** - Claude always has the full context, not just fragments
✅ **Token efficiency** - Read curated docs instead of entire files
✅ **Less repetition** - Don't re-explain brand strategy, design decisions, etc.
✅ **Institutional memory** - Captures decisions and rationale
✅ **Scalability** - If project grows or team expands, context is documented

## Version History

**Created:** 2025-11-22
**Last Updated:** 2025-11-22
**Status:** Initial version - all 5 core files created

---

**Next time you open Claude Code for doctorhump, just type `/doctorhump-context` and you're ready to go!**
