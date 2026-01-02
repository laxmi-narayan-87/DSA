# 961. N-Repeated Element in Size 2N Array

## Problem Statement

Given an array of size `2n` containing `n + 1` unique elements where exactly one element is repeated `n` times, return that repeated element.

**Problem Link:** [LeetCode 961 - N-Repeated Element in Size 2N Array](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/2-January-2026.md)

---

## Solution

```python
from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
```

### Idea

* Use a set to track elements seen so far.
* Since exactly one element is repeated `n` times, the first duplicate encountered is the answer. 

### Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`
