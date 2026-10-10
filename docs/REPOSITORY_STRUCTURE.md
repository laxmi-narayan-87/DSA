# Repository Structure

The repository separates platform submissions, language-focused archives, reusable algorithm/data-structure references, and the static problem browser. The 2026 LeetCode daily archive is organized under `solutions/platforms/leetcode/` by difficulty and problem ID; `problems/2026/README.md` remains as a dated migration index.

## Current layout

```text
solutions/
  platforms/
    codechef/
    geeksforgeeks/
    hackerrank/
    leetcode/
  languages/
    cpp/
    mysql/
    python/
algorithms/
data-structures/
  arrays/
  linked-lists/
  trees/
    notes/
  graphs/
problems/
docs/
index.html
```

The platform and language folders were moved under `solutions/` while retaining their internal paths and file contents. `gfg/` was renamed to `geeksforgeeks/`; MySQL lives under `solutions/languages/mysql/`. The Python and Python 3 archives are combined under `solutions/languages/python/`. The C++ archive is consolidated under `solutions/languages/cpp/`, preserving each statement and timestamped source file. Existing tree deep dives are retained under `data-structures/trees/notes/`.

## Directory responsibilities

| Path | Responsibility | Change policy |
|---|---|---|
| `solutions/platforms/` | Platform-specific submissions | Keep each platform grouped under one directory |
| `solutions/languages/` | Language-focused archives and standalone examples | Use lowercase language directory names |
| `problems/` | Static-browser content and archive indexes | Preserve browser-consumed paths; use platform folders for new or migrated LeetCode problem content |
| `algorithms/` | Reusable algorithm implementations and explanations | Organize by algorithm family |
| `data-structures/` | Data-structure implementations and explanations | Organize by structure using lowercase directory names |
| `data-structures/linked-lists/` | Linked-list theory, implementation, examples, and practice topics | Keep reusable references here; platform submissions stay in the platform archive |
| `data-structures/trees/` | Tree theory, traversals, BSTs, and specialist notes | Preserve existing B-tree, red-black-tree, and skip-list notes |
| `data-structures/graphs/` | Graph representations, traversal, shortest paths, and practice topics | Keep reusable references here |
| `docs/` | Repository conventions, templates, migration notes | Documentation only |
| `index.html` | Static problem browser | Keep the existing browser behavior and problem links intact |

## Topic-folder conventions

For data-structure topic folders, use this structure when applicable:

- `README.md` — concepts, trade-offs, complexity, and links to other notes.
- `implementation/` — small runnable reference implementations.
- `problems/README.md` — practice roadmap; do not copy platform submissions here.
- `examples/README.md` — traces and edge cases.
- `notes/` — focused deep dives for specialized variants.

## Rules for future changes

1. Add platform submissions under `solutions/platforms/<platform>/`.
2. Add language-focused examples under `solutions/languages/<language>/`.
3. Use lowercase directory names and kebab-case slugs for new folders.
4. Keep a preferred solution clear; retain alternatives only when they add learning value.
5. Do not delete historical submissions as part of structural changes.
6. Preserve paths consumed by the existing static browser and do not redesign `index.html` during repository organization; daily LeetCode statements and solutions belong under `solutions/platforms/leetcode/`.
7. Check relative Markdown links and image references when changing paths.
8. Treat duplicate detection and deduplication as a separate audited phase; identical content alone is not enough to justify deletion.
