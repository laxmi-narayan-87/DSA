# Maximum Product of Two Digits

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a positive integer `n`.

Return the  **maximum**  product of any two digits in `n`.

 **Note:**  You may use the  **same**  digit twice if it appears more than once in `n`.

 

 **Example 1:** 

 **Input:**  n = 31

 **Output:**  3

 **Explanation:** 

- The digits of n are [3, 1].
- The possible products of any two digits are: 3 * 1 = 3.
- The maximum product is 3.

 **Example 2:** 

 **Input:**  n = 22

 **Output:**  4

 **Explanation:** 

- The digits of n are [2, 2].
- The possible products of any two digits are: 2 * 2 = 4.
- The maximum product is 4.

 **Example 3:** 

 **Input:**  n = 124

 **Output:**  8

 **Explanation:** 

- The digits of n are [1, 2, 4].
- The possible products of any two digits are: 1  *2 = 2, 1*  4 = 4, 2 * 4 = 8.
- The maximum product is 8.

 

 **Constraints:** 

- 10 <= n <= 109

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.2 MB (beats 54.97%)  
**Submitted:** 2026-07-25T08:15:02.149Z  

```py
class Solution:
    def maxProduct(self, n: int) -> int:
        n=str(n)
        maxprod=float(-inf)
        prod=1
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                prod= int(n[i])*int(n[j])
                if prod>maxprod:
                    maxprod=prod
        return maxprod
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-product-of-two-digits/)