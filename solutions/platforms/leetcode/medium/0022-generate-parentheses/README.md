# Generate Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given `n` pairs of parentheses, write a function to  *generate all combinations of well-formed parentheses*.

 

 **Example 1:** 

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

```

 **Example 2:** 

```
Input: n = 1
Output: ["()"]

```

 

 **Constraints:** 

- 1 <= n <= 8

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.4 MB (beats 36.93%)  
**Submitted:** 2026-10-02T18:49:58.931Z  

```py
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backtrack(s, open_count, close_count):
            if len(s) == 2 * n:
                ans.append(s)
                return

            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/generate-parentheses/)