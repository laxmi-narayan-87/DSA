# LeetCode 165: Compare Version Numbers – First Principles Breakdown

[![LeetCode](https://img.shields.io/badge/LeetCode-165-red)](https://leetcode.com/problems/compare-version-numbers/)

## 🧠 Core Problem

Compare two hierarchical numeric identifiers (e.g., "1.0.3" vs "1.0.7") reliably.

Fundamental idea: break the strings into atomic segments, convert to integers, compare numerically, and handle unequal lengths or leading zeros.

---

## 1. Fundamental Concepts

- A version string is a sequence of digits separated by dots (`.`).
- To compare versions:
  1. Break the string into segments.
  2. Convert each segment to an integer.
  3. Compare corresponding segments left to right.
- Avoiding built-ins like `len()` or `split()` requires manual traversal.
- Numeric comparison is essential—string comparison can be misleading ("10" vs "2").

---

## 2. Manual String Length (first-principles)

```python
def string_length(s):
    count = 0
    while True:
        try:
            _ = s[count]
            count += 1
        except IndexError:
            break
    return count
```

Principle: Manually count characters to determine boundaries safely when not using `len()`.

---

## 3. Parsing Version Segments (first-principles)

Maintain two pointers, `i` and `j`. Build numbers digit by digit until a dot or string end:

```python
num1 = 0
while i < n1 and version1[i] != '.':
    num1 = num1 * 10 + ("0123456789".find(version1[i]))
    i += 1
# repeat similarly for version2 → num2
```

This converts character sequences to numeric values reliably.

---

## 4. Comparing Segments and Skipping Dots

After parsing `num1` and `num2`:

```python
if num1 > num2: return 1
if num1 < num2: return -1

# Skip dot if present
i += (i < n1)
j += (j < n2)
```

Principles:
- Segment isolation mirrors human comparison of versions.
- Early exit on difference avoids unnecessary computation.
- Skipping dots ensures proper traversal.

---

## 5. Complete First-Principles Code

A self-contained implementation that avoids `split()` and `len()` and works using manual traversal:

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Compute string length manually
        def string_length(s):
            count = 0
            while True:
                try:
                    _ = s[count]
                    count += 1
                except IndexError:
                    break
            return count

        n1, n2 = string_length(version1), string_length(version2)
        i = j = 0

        while i < n1 or j < n2:
            num1 = 0
            num2 = 0

            # Parse number from version1
            while i < n1 and version1[i] != '.':
                # convert character digit to integer (safe manual conversion)
                num1 = num1 * 10 + ("0123456789".find(version1[i]))
                i += 1

            # Parse number from version2
            while j < n2 and version2[j] != '.':
                num2 = num2 * 10 + ("0123456789".find(version2[j]))
                j += 1

            # Compare numbers
            if num1 > num2:
                return 1
            if num1 < num2:
                return -1

            # Skip dot if present
            i += (i < n1)
            j += (j < n2)

        return 0
```

---

## 6. Why It Works

- Segment Isolation: Handles one number at a time.
- Numeric Reliability: Converts strings to integers to avoid lexicographic errors.
- Early Exit: Stops once a difference is found.
- Handles Unequal Lengths: Missing segments are treated as `0`.
- Handles Leading Zeros: `"01"` equals `"1"`.

---

## 7. Complexity Analysis

- Time Complexity: O(m + n) — each character of both strings is processed once.
- Space Complexity: O(1) — no extra arrays or split lists used.

---

## 8. Example Walkthrough

Example:
```python
version1 = "1.01"
version2 = "1.001"
```

- Segment 1: `1` vs `1` → equal  
- Segment 2: `01` → `1`, `001` → `1` → equal  
Result → `0` (versions are equal)

---

## 9. First Principles Takeaways

- Decompose complex strings into atomic units.
- Convert characters to numeric values manually when avoiding helpers.
- Compare sequentially and short-circuit on difference.
- Handle edge cases like unequal lengths or leading zeros.

---

Tags: #string #parsing #simulation #first-principle #easy
