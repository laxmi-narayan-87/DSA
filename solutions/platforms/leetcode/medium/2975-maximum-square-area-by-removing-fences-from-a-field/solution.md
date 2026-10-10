# 2975. Maximum Square Area by Removing Fences From a Field

## Problem Statement

There is a large `(m - 1) x (n - 1)` rectangular field with corners at `(1, 1)` and `(m, n)` containing some horizontal and vertical fences.  Return the **maximum area of a square field** that can be formed by **removing some fences** (possibly none) or `-1` if it is impossible to make a square field.

Since the answer may be large, return it **modulo `10^9 + 7`**.

**Problem Link:** [LeetCode 2975 - Maximum Square Area by Removing Fences From a Field](https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/16-January-2026.md)

---

## Solution

```python
from typing import List

class Solution: 
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # Add boundary fences (which cannot be removed)
        hFences.extend([1, m])
        vFences.extend([1, n])
        
        stt = set()
        ans = 0
        
        # Calculate all possible horizontal distances
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                stt.add(abs(hFences[j] - hFences[i]))
        
        # Calculate all possible vertical distances and find common ones
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                val = abs(vFences[j] - vFences[i])
                if val in stt:
                    ans = max(ans, val)
        
        if ans == 0:
            return -1
        return (ans * ans) % (10**9 + 7)
```

### Idea

* **Key insight:** A square can be formed if we can find the same gap distance in both horizontal and vertical fences
* **Algorithm:**
  1. Add boundary fences at positions `1` and `m` (horizontal), `1` and `n` (vertical)
  2. Calculate all possible **horizontal gaps** (distances between any two horizontal fences) and store in a set
  3. Calculate all possible **vertical gaps** (distances between any two vertical fences)
  4. Find the **maximum gap** that exists in both horizontal and vertical sets
  5. Return the square of that gap, or `-1` if no common gap exists
* By removing fences between two positions, we create a gap equal to their distance
* A square requires equal width and height, so we need a common gap size

### Example Walkthrough

For `m = 4, n = 3, hFences = [2,3], vFences = [2]`:
- After adding boundaries: `hFences = [2,3,1,4]`, `vFences = [2,1,3]`
- Horizontal gaps: `{1, 2, 3}` (distances:  3-2=1, 4-3=1, 4-2=2, 4-1=3, etc.)
- Vertical gaps: `{1, 2}` (distances: 2-1=1, 3-2=1, 3-1=2)
- Common gaps: `{1, 2}` → maximum = 2
- Area = `2 × 2 = 4`

### Complexity

* **Time:** `O(h² + v²)` - where h = len(hFences), v = len(vFences), checking all pairs
* **Space:** `O(h²)` - storing all horizontal gaps in a set
