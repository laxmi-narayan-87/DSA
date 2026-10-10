# 2943. Maximize Area of Square Hole in Grid

## Problem Statement

You are given two integers, `n` and `m`, and two integer arrays, `hBars` and `vBars`. The grid has `n + 2` horizontal and `m + 2` vertical bars.  You can remove some bars from `hBars` and `vBars`. Return the **maximum area of a square-shaped hole** in the grid after removing some bars (possibly none).

**Problem Link:** [LeetCode 2943 - Maximize Area of Square Hole in Grid](https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/15-January-2026.md)

---

## Solution

```python
from typing import List

class Solution: 
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def longest_consecutive(arr):
            """Find the longest consecutive sequence in the array"""
            arr.sort()
            longest = 1
            current = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    current += 1
                    longest = max(longest, current)
                else:
                    current = 1
            return longest
        
        longesth = longest_consecutive(hBars)
        longestv = longest_consecutive(vBars)
        side = min(longesth, longestv) + 1
        return side * side
```

### Idea

* To create a square hole, we need to remove **consecutive bars** in both directions
* **Key insight:** Removing `k` consecutive bars creates a gap of `k + 1` units
  - Example: Remove bars [2, 3] → creates gap from bar 1 to bar 4 → size = 3 units
* **Algorithm:**
  1. Find the longest consecutive sequence in `hBars` (removable horizontal bars)
  2. Find the longest consecutive sequence in `vBars` (removable vertical bars)
  3. The square side = `min(longesth, longestv) + 1` (limited by the smaller dimension)
  4. Return `side × side` for the area
* Sort each array and find the longest run of consecutive integers

### Example Walkthrough

For `hBars = [2,3]`, `vBars = [2]`:
- `longesth = 2` (bars 2,3 are consecutive)
- `longestv = 1` (only bar 2)
- `side = min(2, 1) + 1 = 2`
- Area = `2 × 2 = 4`

### Complexity

* **Time:** `O(h log h + v log v)` - sorting both arrays, where h = len(hBars), v = len(vBars)
* **Space:** `O(1)` - only using constant extra space (excluding sort space)
