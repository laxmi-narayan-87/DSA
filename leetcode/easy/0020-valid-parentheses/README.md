# Valid Parentheses

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

 

 **Example 1:** 

 **Input:**  s = "()"

 **Output:**  true

 **Example 2:** 

 **Input:**  s = "()[]{}"

 **Output:**  true

 **Example 3:** 

 **Input:**  s = "(]"

 **Output:**  false

 **Example 4:** 

 **Input:**  s = "([])"

 **Output:**  true

 **Example 5:** 

 **Input:**  s = "([)]"

 **Output:**  false

 

 **Constraints:** 

- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 24.83%)  
**Submitted:** 2026-10-01T17:59:16.525Z  

```py
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch=="(" or ch =="{" or ch=="[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                    
                if (ch==")" and stack[-1]=="(") or (ch=="}" and stack[-1]=="{") or (ch=="]" and stack[-1]=="["):
                    stack.pop()
                else:
                    return False
        if len(stack)!=0:
            return False
        return True
```

---

[View on LeetCode](https://leetcode.com/problems/valid-parentheses/)