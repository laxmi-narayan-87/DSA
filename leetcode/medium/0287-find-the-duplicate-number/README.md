# Find the Duplicate Number

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only  **one repeated number**  in `nums`, return  *this repeated number*.

You must solve the problem  **without**  modifying the array `nums` and using only constant extra space.

 

 **Example 1:** 

```
Input: nums = [1,3,4,2,2]
Output: 2

```

 **Example 2:** 

```
Input: nums = [3,1,3,4,2]
Output: 3

```

 **Example 3:** 

```
Input: nums = [3,3,3,3,3]
Output: 3
```

 

 **Constraints:** 

- 1 <= n <= 105
- nums.length == n + 1
- 1 <= nums[i] <= n
- All the integers in nums appear only once except for precisely one integer which appears two or more times.

 

 **Follow up:** 

- How can we prove that at least one duplicate number must exist in nums?
- Can you solve the problem in linear runtime complexity?

## Solution

**Language:** Python  
**Runtime:** 29 ms (beats 41.95%)  
**Memory:** 33.4 MB (beats 92.02%)  
**Submitted:** 2026-08-18T10:54:14.174Z  

```py
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            # dig=nums[i]
            # for j in range(i+1,n):
            #     if nums[j]==dig:
            #         return dig
            val=abs(nums[i])
            if nums[val]<0:
                return abs(nums[i])
            else:
                nums[val]*=-1
        for i in range(n):
            if nums[i]<0:
                nums[i]*=-1

```

---

[View on LeetCode](https://leetcode.com/problems/find-the-duplicate-number/)