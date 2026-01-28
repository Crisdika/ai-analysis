# PR Review Configuration

This repository uses assistive PR review. The goal is to catch obvious errors and clear risks only.

## Review Scope

ONLY analyze the diff content. Ignore all code outside the PR changes.

## What to Flag

Flag these issues ONLY if they appear in NEW code within the diff:

### Python Errors (Flag as warning)
- Possible unhandled NoneType
- Variables created but never used
- Unintentional implicit None return
- Mutable default arguments in functions
- datetime.now() without timezone when relevant

### Clear Risks (Flag as warning)
- Bare except: or except Exception: without specific handling
- Confusing conditional logic that is hard to follow
- Silent pass in critical flow
- Use of eval() or exec()
- SQL built via string concatenation without parameterization

### Minimal Readability (Flag as suggestion)
- New functions that are excessively long (50+ lines)
- More than 3 levels of nested if/else
- Extremely generic names (data, temp, obj) in new code

## What to IGNORE - DO NOT comment on these

- Architecture and system design
- Performance optimizations
- Design patterns
- Test coverage or test existence
- Legacy code not modified in the diff
- Code style or formatting
- Type hints
- Large refactoring opportunities
- SOLID principles or Clean Code standards

## Response Format

- Short, objective comments
- One issue per comment
- Neutral, polite, collaborative language
- Treat all suggestions as optional
- Do not explain theoretical principles

## If no relevant issues found

Respond exactly: "No issues found. Checked for bugs and CLAUDE.md compliance."

## Tone

- Collaborative
- Pragmatic
- Respectful
- No sarcasm
- Not rigid or auditor-like