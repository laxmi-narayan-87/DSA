# 1458. Max Dot Product of Two Subsequences

## Problem Statement

Given two arrays `nums1` and `nums2`, return the **maximum dot product** between non-empty subsequences of `nums1` and `nums2` with the same length.

**Problem Link:** [LeetCode 1458 - Max Dot Product of Two Subsequences](https://leetcode.com/problems/max-dot-product-of-two-subsequences/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/08-January-2026.md)

---

## Solution

```python
from typing import List

class Solution: 
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[float('-inf')] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                prod = nums1[i] * nums2[j]
                dp[i][j] = prod
                
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i][j], prod + max(0, dp[i-1][j-1]))
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
        
        return dp[-1][-1]
```

### Idea

* Use **Dynamic Programming** with a 2D table: 
  - `dp[i][j]` = maximum dot product using elements up to index `i` in `nums1` and index `j` in `nums2`
* For each position `(i, j)`, consider four options:
  1. **Start fresh:** Just take `nums1[i] * nums2[j]`
  2. **Extend previous:** Add current product to `dp[i-1][j-1]` (only if it's positive)
  3. **Skip nums1[i]:** Take `dp[i-1][j]`
  4. **Skip nums2[j]:** Take `dp[i][j-1]`
* The answer is `dp[n-1][m-1]` - the maximum dot product considering all elements
* Initialize with `-inf` to handle all negative cases

### Complexity

* **Time:** `O(n × m)` - fill the entire DP table
* **Space:** `O(n × m)` - store the DP table
