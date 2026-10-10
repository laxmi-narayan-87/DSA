# Repository Structure

This repository contains DSA solutions, platform submissions, reusable algorithm implementations, and a static problem browser.

## Directory responsibilities

| Path | Responsibility | Change policy |
|---|---|---|
| `Python3/`, `Python/` | Existing Python solution archives | Preserve historical submissions; do not add new solutions here unless maintaining an existing archive |
| `MySQL/` | Existing SQL solution archive | Preserve historical submissions |
| `leetcode/`, `hackerrank/`, `codechef/`, `gfg/` | Platform-organized submissions | Preserve existing paths while migration is in progress |
| `problems/` | Existing problem pages/data consumed by the current browser | **Compatibility-sensitive. Do not move or rename paths without updating and testing the browser separately.** |
| `algorithms/` | Reusable algorithm implementations and explanations | Organize by algorithm family |
| `data-structures/` | Reusable data-structure implementations and explanations | Organize by data structure |
| `docs/` | Repository conventions, templates, and migration notes | Documentation only |
| `tests/` | Automated checks and reusable tests | Test code only |
| `index.html` | Existing static problem browser | Out of scope for this structure change; keep unchanged |

## Canonical layout for new solutions

Until the historical folders are migrated safely, add new solutions to the existing platform folder that best matches the problem. Avoid creating another top-level folder for the same set of solutions.

For any future migration, the intended canonical layout is:

```text
solutions/
  python/
    easy/
    medium/
    hard/
  cpp/
    easy/
    medium/
    hard/
  sql/
    easy/
    medium/
    hard/
algorithms/
  sorting/
  searching/
  graphs/
  dynamic-programming/
data-structures/
  arrays/
  linked-lists/
  stacks-queues/
  trees/
  graphs/
  heaps/
docs/
tests/
```

This target layout is a migration destination, not a claim that legacy files have already been moved.

## Rules

1. Do not delete historical submissions as part of a structure-only change.
2. Keep one clearly identified preferred solution for each problem/language. Retain alternative approaches only when they add learning value, and label them.
3. Use lowercase directory names and kebab-case problem slugs.
4. Keep platform problem IDs in slugs where available, for example `0020-valid-parentheses`.
5. Put explanatory notes and complexity analysis in Markdown; avoid duplicating full problem statements unnecessarily.
6. Preserve existing browser paths until a dedicated browser migration has been designed and validated.
7. Update documentation and tests in the same change when a path is intentionally moved.
8. Never report a migration as complete until a tree audit and link checks pass.
