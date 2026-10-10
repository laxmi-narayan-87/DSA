# LeetCode 165: Compare Version Numbers

[![LeetCode](https://img.shields.io/badge/LeetCode-165-red)](https://leetcode.com/problems/compare-version-numbers/)

## Problem

Compare two version strings `version1` and `version2`. Each version string contains digits separated by dots (`.`). Return:

- `1` if `version1 > version2`  
- `-1` if `version1 < version2`  
- `0` if both are equal  

Rules:
- Compare segments numerically.
- Treat missing segments in the shorter version as `0`.
- Ignore leading zeros.

---

## Examples

Input: version1 = "1.01", version2 = "1.001"  
Output: 0

Input: version1 = "1.0", version2 = "1.0.0"  
Output: 0

Input: version1 = "0.1", version2 = "1.1"  
Output: -1

---

## Approach 1 — Split and Compare

Simple, readable solution using built-ins.

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        n = max(len(v1), len(v2))
        
        for i in range(n):
            num1 = int(v1[i]) if i < len(v1) else 0
            num2 = int(v2[i]) if i < len(v2) else 0
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0
```

Complexity:
- Time: O(m + n) where m and n are lengths of the version strings (characters).
- Space: O(m + n) for the split lists.

---

## Approach 2 — Pointer Traversal (space-efficient)

Traverse both strings manually with two pointers, parse numbers on the fly, avoid extra arrays.

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = j = 0
        n1, n2 = len(version1), len(version2)

        while i < n1 or j < n2:
            num1 = 0
            num2 = 0

            while i < n1 and version1[i] != '.':
                num1 = num1 * 10 + (ord(version1[i]) - ord('0'))
                i += 1

            while j < n2 and version2[j] != '.':
                num2 = num2 * 10 + (ord(version2[j]) - ord('0'))
                j += 1

            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1

            # skip dot if present
            i += (i < n1)
            j += (j < n2)

        return 0
```

Complexity:
- Time: O(m + n) — each character processed once.
- Space: O(1) — no extra arrays used.

---

## Summary

- Approach 1 is concise and easy to read (uses `.split()` and `int()`).
- Approach 2 is more space-efficient and demonstrates manual parsing (useful in constrained environments or when avoiding higher-level helpers).
- Both handle unequal lengths and leading zeros correctly.

---

## Tags

#string #parsing #simulation #easy
