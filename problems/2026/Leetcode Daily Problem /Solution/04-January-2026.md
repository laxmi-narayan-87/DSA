# 1390. Four Divisors

## Problem Statement

Given an integer array `nums`, return the **sum of divisors** of the integers in the array that have **exactly four divisors**. If there is no such integer in the array, return `0`.

**Problem Link:** [LeetCode 1390 - Four Divisors](https://leetcode.com/problems/four-divisors/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/04-January-2026.md)

---

## Solution

```python
from typing import List

class Solution: 
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisors(n):
            divs = set()
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divs. add(i)
                    divs.add(n // i)
                if len(divs) > 4:
                    return []
            return list(divs) if len(divs) == 4 else []
        
        total = 0
        for num in nums:
            d = divisors(num)
            if d:
                total += sum(d)
        return total
```

### Idea

* For each number in the array, find all its divisors: 
  - Iterate from 1 to √n
  - For each divisor `i`, both `i` and `n/i` are divisors
  - Use a set to avoid duplicates
* Early termination:  if divisors exceed 4, return empty list
* Only count numbers with exactly 4 divisors and sum their divisors
* Return the total sum

### Complexity

* **Time:** `O(n × √m)` where n is the length of nums and m is the maximum value
* **Space:** `O(1)` (excluding the output, small constant space for divisor set)
