# Structure Migration Plan

## Scope of this change

This change introduces repository structure documentation only. The existing `index.html` and all current paths used by the browser are intentionally untouched.

## Current issues

- Several solution archives overlap (`Python3/`, `Python/`, `leetcode/`, and `problems/`).
- Some identical solution contents appear in more than one path.
- The contribution guide and actual folder layout have drifted.
- Browser data and directory paths are coupled, so moving files can create broken links.

## Safe migration sequence

1. Inventory all source files by problem ID, language, platform, and content hash.
2. Mark one canonical solution for each problem/language; classify exact duplicates and alternate approaches separately.
3. Add tests or syntax checks for the files selected as canonical.
4. Build a generated manifest and validate all existing browser links against the current paths.
5. Move a small, reviewed batch to the canonical `solutions/` layout while retaining compatibility paths until consumers no longer depend on them.
6. Run the inventory, duplicate report, and link validation again.
7. Remove a legacy copy only after references are updated and the change has been reviewed.

## Explicit exclusions

- Do not edit `index.html` or redesign its sections in this migration.
- Do not change problem-browser behavior as part of folder organization.
- Do not mass-delete identical files: identical contents can be intentional exports or platform-compatible copies.
- Do not rewrite historical solutions merely to normalize formatting.

## Completion criteria for a future file migration

- No source files lost.
- Every migrated problem has a canonical location and provenance.
- Existing browser links remain valid.
- Duplicate files are classified, not blindly removed.
- The final tree and changed-file list are reviewed before merging.
