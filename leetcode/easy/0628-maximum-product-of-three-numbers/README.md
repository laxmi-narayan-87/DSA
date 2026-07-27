# Maximum Product of Three Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`,  *find three numbers whose product is maximum and return the maximum product*.

 

 **Example 1:** 

```
Input: nums = [1,2,3]
Output: 6

```

 **Example 2:** 

```
Input: nums = [1,2,3,4]
Output: 24

```

 **Example 3:** 

```
Input: nums = [-1,-2,-3]
Output: -6

```

 

 **Constraints:** 

- 3 <= nums.length <= 104
- -1000 <= nums[i] <= 1000

## Solution

**Language:** Python  
**Runtime:** 18 ms (beats 67.75%)  
**Memory:** 20.4 MB (beats 42.30%)  
**Submitted:** 2026-07-27T06:23:02.958Z  

```py
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        p1=nums[0]*nums[1]*nums[n-1]
        p2=nums[n-1]*nums[n-2]*nums[n-3]
        return max(p1,p2)
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-product-of-three-numbers/)