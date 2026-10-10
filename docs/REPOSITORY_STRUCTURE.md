# Repository Structure

The repository separates platform submissions, language-focused archives, reusable algorithm/data-structure references, and the static problem browser.

## Current layout

```text
solutions/
  platforms/
    codechef/
    geeksforgeeks/
    hackerrank/
    leetcode/
  languages/
    mysql/
    python/
    python3/
algorithms/
data-structures/
problems/
docs/
index.html
```

The platform and language folders were moved under `solutions/` while retaining their internal paths and file contents. `gfg/` was renamed to `geeksforgeeks/`; `MySQL/`, `Python/`, and `Python3/` now live under `solutions/languages/`.

## Directory responsibilities

| Path | Responsibility | Change policy |
|---|---|---|
| `solutions/platforms/` | Platform-specific submissions | Keep each platform grouped under one directory |
| `solutions/languages/` | Language-focused archives and standalone examples | Use lowercase language directory names |
| `problems/` | Pages/data consumed by the existing static browser | Compatibility-sensitive; preserve existing paths |
| `algorithms/` | Reusable algorithm implementations and explanations | Organize by algorithm family |
| `data-structures/` | Data-structure implementations and explanations | Organize by data structure |
| `docs/` | Repository conventions, templates, migration notes | Documentation only |
| `index.html` | Existing static problem browser | Keep its sections and behavior unchanged |

## Rules for future changes

1. Add platform submissions under `solutions/platforms/<platform>/`.
2. Add language-focused examples under `solutions/languages/<language>/`.
3. Use lowercase directory names and kebab-case problem slugs for new folders.
4. Keep a preferred solution clear; retain alternatives only when they add learning value.
5. Do not delete historical submissions as part of structural changes.
6. Preserve the existing `problems/` paths and do not redesign `index.html` during repository organization.
7. Check relative Markdown links and image references when changing paths.
8. Treat duplicate detection and deduplication as a separate audited phase; identical content alone is not enough to justify deletion.
