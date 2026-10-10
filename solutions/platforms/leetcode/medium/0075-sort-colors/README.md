# Sort Colors

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array `nums` with `n` objects colored red, white, or blue, sort them  **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

 **Example 1:** 

 **Input:**  nums = [2,0,2,1,1,0]

 **Output:**  [0,0,1,1,2,2]

 **Explanation:** 

The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.

 **Example 2:** 

 **Input:**  nums = [2,0,1]

 **Output:**  [0,1,2]

 **Explanation:** 

The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.

 

 **Constraints:** 

- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2.

 

 **Follow up:**  Could you come up with a one-pass algorithm using only constant extra space?

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 11.18%)  
**Memory:** 19.2 MB (beats 62.22%)  
**Submitted:** 2026-08-19T09:26:12.327Z  

```py
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cat0=nums.count(0)
        cat1=nums.count(1)
        cat2=nums.count(2)
        for i in range(len(nums)):
            if i<cat0:
                nums[i]=0
            elif cat0<=i<cat0+cat1:
                nums[i]=1
            elif i>=(cat0+cat1):
                nums[i]=2
        return nums
```

---

[View on LeetCode](https://leetcode.com/problems/sort-colors/)