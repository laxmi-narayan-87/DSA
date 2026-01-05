# 1975. Maximum Matrix Sum

## Problem Statement

You are given an `n × n` integer matrix. You can perform the following operation any number of times:  choose any two adjacent elements and multiply each of them by `-1`. Return the maximum possible sum of the matrix's elements after performing the allowed operations.

**Problem Link:** [LeetCode 1975 - Maximum Matrix Sum](https://leetcode.com/problems/maximum-matrix-sum/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/5-January-2026.md)

---

## Solution

```python
from typing import List

class Solution: 
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        neg = 0
        minabs = float('inf')
        
        for row in matrix:
            for x in row:
                if x < 0:
                    neg += 1
                ax = abs(x)
                total += ax
                if ax < minabs:
                    minabs = ax
        
        if neg % 2 == 0:
            return total
        else:
            return total - 2 * minabs
```

### Idea

* Key insight: Each operation flips the sign of two adjacent elements
* Since we can flip pairs, we can move negative signs around the matrix
* If we have an **even** number of negatives, we can eliminate all of them → return sum of absolute values
* If we have an **odd** number of negatives, exactly one must remain negative → make the smallest absolute value negative
* Track: 
  - Total sum of absolute values
  - Count of negative numbers
  - Minimum absolute value in the matrix

### Complexity

* **Time:** `O(n²)` - iterate through all elements once
* **Space:** `O(1)` - only using constant extra space
