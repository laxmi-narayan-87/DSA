# 66. Plus One

## Problem Statement

Given a large integer represented as an array of digits, increment it by one and return the resulting array. 

**Problem Link:** [LeetCode 66 - Plus One](https://leetcode.com/problems/plus-one/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/1-January-2026.md)

---

## Solution

```python

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0
        return [1] + digits
```

### Idea

* Start adding `1` from the last digit.
* If the digit becomes less than `10`, we are done.
* If it becomes `10`, set it to `0` and carry to the next digit.
* If all digits overflow (e.g., `[9,9,9]`), prepend `1`.

### Complexity

* **Time:** `O(n)`
* **Space:** `O(1)` (in-place, excluding output)
