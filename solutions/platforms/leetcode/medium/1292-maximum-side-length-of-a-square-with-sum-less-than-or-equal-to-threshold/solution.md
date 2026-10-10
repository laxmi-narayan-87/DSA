# 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

## Problem Statement

Given a `m x n` matrix `mat` and an integer `threshold`, return the **maximum side-length of a square** with a sum less than or equal to `threshold` or return `0` if there is no such square.

**Problem Link:** [LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/19-January-2026.md)

---

## Solution

```python
from typing import List

class Solution: 
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        
        # Build prefix sum array
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (mat[i][j] + prefix[i][j + 1] + 
                                        prefix[i + 1][j] - prefix[i][j])
        
        def square_sum(i, j, k):
            """Calculate sum of k×k square starting at (i, j)"""
            return (prefix[i + k][j + k] - prefix[i][j + k] - 
                    prefix[i + k][j] + prefix[i][j])
        
        # Try from largest to smallest square size
        for k in range(min(m, n), 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if square_sum(i, j, k) <= threshold:
                        return k
        
        return 0
```

### Idea

* Use **Prefix Sum Array** for efficient range sum queries
* **Prefix sum formula:**
  - `prefix[i][j]` = sum of all elements in rectangle from `(0,0)` to `(i-1,j-1)`
  - Sum of rectangle from `(r1,c1)` to `(r2,c2)` = `prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]`
* **Algorithm:**
  1. Build prefix sum array in `O(m×n)` time
  2. Try square sizes from `min(m, n)` down to 1 (largest first)
  3. For each size `k`, check all possible top-left positions
  4. Calculate square sum in `O(1)` using prefix sum
  5. Return the first (largest) `k` where sum ≤ threshold

### Example Walkthrough

For `mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]`, `threshold = 4`:
- Build prefix sum array
- Try k=3: All 3×3 squares have sum > 4
- Try k=2: Check position (0,0):
  - Square:  [[1,1],[1,1]]
  - Sum = 1+1+1+1 = 4 ≤ 4 ✓
  - Found!  Return 2

### Complexity

* **Time:** `O(m × n × min(m,n))` - O(mn) to build prefix + O(mn × min(m,n)) to check all squares
* **Space:** `O(m × n)` - prefix sum array

### Optimization Note
This can be further optimized using **binary search** on the side length, reducing time complexity to `O(m × n × log(min(m,n)))`.
