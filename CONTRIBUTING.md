# Contributing to DSA Repository

Thank you for contributing to this Data Structures and Algorithms repository.

## How to contribute

1. Fork the repository and clone your fork.
2. Create a focused branch for your change.
3. Follow the directory conventions below.
4. Test your implementation and review the diff.
5. Submit a pull request with a clear description.

## Types of contributions

- Algorithm implementations in different languages
- Problem solutions with original explanations
- Documentation and tutorials
- Bug fixes, optimizations, and meaningful edge-case tests

## Repository layout

```text
solutions/
  platforms/
    <platform>/
      <difficulty>/<problem-slug>/
  languages/
    <language>/
      <difficulty>/<problem-slug>/
algorithms/
data-structures/
problems/        # browser-backed paths; do not move casually
docs/
index.html       # existing browser; keep its sections and behavior intact
```

### Where to add a solution

- Use `solutions/platforms/<platform>/` for submissions tied to a platform, such as LeetCode, CodeChef, HackerRank, or GeeksforGeeks.
- Use `solutions/languages/<language>/` for standalone language-focused examples and curated practice archives.
- Use lowercase directory names and kebab-case problem slugs. Preserve a platform problem ID when available, for example `0020-valid-parentheses`.
- Prefer stable filenames such as `solution.py`, `solution.cpp`, or `solution.sql` for new entries. Keep historical timestamped filenames when maintaining legacy submissions.
- Do not create a second top-level folder for a platform or language already represented under `solutions/`.

## Code and documentation standards

- Write readable, idiomatic code with meaningful names.
- Explain the core idea in your own words.
- State time and space complexity.
- Include relevant edge cases and sample inputs/outputs where useful.
- Avoid copying full problem statements unnecessarily.
- Keep alternatives only when they add learning value; label the preferred approach.

Language notes:
- **Python:** follow PEP 8 and use clear function/class names.
- **C++:** use consistent formatting, descriptive identifiers, and appropriate standard-library types.
- **SQL:** use consistent formatting and explain non-obvious query logic.

## Compatibility and safety

- Do not move, rename, or delete anything under `problems/` without first checking every browser reference.
- Do not edit or redesign `index.html` as part of a folder-only change.
- Do not mass-delete duplicate-looking files. Compare content and references first; some duplicates may be intentional historical submissions.
- Keep changes scoped and validate links affected by the change.

## Review checklist

- [ ] Correct solution and complexity analysis
- [ ] Relevant edge cases considered
- [ ] File is in the appropriate directory
- [ ] Internal links and images still resolve
- [ ] No unrelated browser/UI changes
