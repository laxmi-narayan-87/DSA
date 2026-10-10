# Structure Migration Record

## Completed: top-level archive consolidation

The following archives were moved into the `solutions/` namespace, preserving their internal directory layout and file contents:

| Previous path | New path |
|---|---|
| `codechef/` | `solutions/platforms/codechef/` |
| `gfg/` | `solutions/platforms/geeksforgeeks/` |
| `hackerrank/` | `solutions/platforms/hackerrank/` |
| `leetcode/` | `solutions/platforms/leetcode/` |
| `MySQL/` | `solutions/languages/mysql/` |
| `Python/` | `solutions/languages/python/` |
| `Python3/` | `solutions/languages/python/` (merged with Python archive) |

## Explicitly preserved

- The initial migration preserved `index.html`; the problem browser was subsequently updated to use the consolidated Python archive.
- The legacy `problems/Python3/` archive was moved into `solutions/languages/python/`; the browser links were updated to the new locations.
- Other paths under `problems/` remain unchanged.
- `algorithms/` and `data-structures/` remain at the repository root; their browser links are unchanged.
- Source and Markdown files were moved as tree entries, without rewriting their contents.
- The separate `solutions/languages/python3/` directory was merged into `solutions/languages/python/`; all 103 files from that archive were retained.
- The legacy `problems/Python3/` archive was also consolidated into `solutions/languages/python/`; all 205 files were retained without path collisions.
- Historical duplicates and alternative solutions were retained.

## Follow-up audit

This migration consolidates the top-level layout; it does not claim that duplicate solutions have been deduplicated or that every historical README count is synchronized.

Recommended next checks:

1. Scan Markdown links and embedded images for references that point outside their moved subtree.
2. Inventory solutions by platform, problem ID, language, and content hash.
3. Identify exact duplicates separately from distinct approaches.
4. Add syntax checks/tests for selected canonical solutions before any deduplication.
5. Validate the static browser against the consolidated `solutions/languages/python/` paths and remaining `problems/` paths.

Do not delete legacy or duplicate-looking solutions without checking provenance and references.
