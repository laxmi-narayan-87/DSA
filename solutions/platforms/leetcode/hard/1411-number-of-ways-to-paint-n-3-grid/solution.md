# 1411. Number of Ways to Paint N × 3 Grid

## Problem Statement

You are given a grid of size `n × 3`. You want to paint each cell of the grid with **exactly one** of the three colors: Red, Yellow, and Green.  No two adjacent cells (sharing a horizontal or vertical side) may have the same color.  Return the number of valid ways to paint the grid modulo `10^9 + 7`.

**Problem Link:** [LeetCode 1411 - Number of Ways to Paint N × 3 Grid](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/03-January-2026.md)

---

## Solution

```python
class Solution:
    def numOfWays(self, n:  int) -> int:
        MOD = 10**9 + 7
        
        same = 6  # patterns like ABA (2 colors)
        diff = 6  # patterns like ABC (3 colors)
        
        for _ in range(2, n + 1):
            new_same = (3 * same + 2 * diff) % MOD
            new_diff = (2 * same + 2 * diff) % MOD
            same, diff = new_same, new_diff
        
        return (same + diff) % MOD
```

### Idea

* Classify row patterns into two types:
  - **Same (ABA):** 2 unique colors in a row (e.g., Red-Yellow-Red) — 6 patterns
  - **Diff (ABC):** 3 unique colors in a row (e. g., Red-Yellow-Green) — 6 patterns
* Use dynamic programming to calculate valid transitions: 
  - From ABA pattern: can transition to 3 ABA patterns and 2 ABC patterns
  - From ABC pattern: can transition to 2 ABA patterns and 2 ABC patterns
* Iterate from row 2 to n, updating the counts

### Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`
