# 3314. Construct the Minimum Bitwise Array I

## Problem Statement

You are given an array `nums` consisting of `n` **prime integers**.  You need to construct an array `ans` of length `n`, such that, for each index `i`, the bitwise OR of `ans[i]` and `ans[i] + 1` is equal to `nums[i]`, i.e. `ans[i] OR (ans[i] + 1) == nums[i]`.  Additionally, you must **minimize** each value of `ans[i]` in the resulting array.

**Problem Link:** [LeetCode 3314 - Construct the Minimum Bitwise Array I](https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/20-January-2026.md)

---

## Solution

```python
from typing import List

class Solution: 
    def minBitwiseArray(self, nums:  List[int]) -> List[int]:
        result = []
        for num in nums:
            original = num
            candidate = -1
            # Try all values from 1 to num-1
            for j in range(1, original):
                if (j | (j + 1)) == original:
                    candidate = j
                    break
            result.append(candidate)
        return result
```

### Idea

* Use **Brute Force** to find the minimum value for each number
* **Key observation:** `j | (j + 1)` always produces an odd number
  - When we add 1 to `j`, the rightmost 0 bit becomes 1
  - ORing with the original number keeps all 1 bits
  - The result always has LSB = 1 (odd)
* **Special case:** If `num` is even (like 2), no solution exists → return -1
* **Algorithm:**
  1. For each `num` in `nums`, try all candidates from 1 to `num-1`
  2. Find the first (minimum) `j` where `j | (j + 1) == num`
  3. If found, add `j` to result; otherwise add -1

### Example Walkthrough

For `nums = [2,3,5,7]`:
- `num = 2` (even): No j satisfies the condition → -1
- `num = 3`: Try j=1: `1 | 2 = 3` ✓ → 1
- `num = 5`: Try j=1,2,3,4: `4 | 5 = 5` ✓ → 4
- `num = 7`: Try j=1,2,3:  `3 | 4 = 7` ✓ → 3
- Result: `[-1,1,4,3]`

### Binary Pattern Analysis

```
num = 3 (011):  j = 1 (001) | 2 (010) = 3 (011) ✓
num = 5 (101):  j = 4 (100) | 5 (101) = 5 (101) ✓
num = 7 (111):  j = 3 (011) | 4 (100) = 7 (111) ✓
num = 11 (1011): j = 9 (1001) | 10 (1010) = 11 (1011) ✓
```

### Complexity

* **Time:** `O(n × max(nums))` - for each number, try up to `num` candidates
* **Space:** `O(1)` - only using constant extra space (excluding output array)

### Optimization Note
This can be optimized to `O(n)` by using bit manipulation to directly compute the answer by flipping the rightmost consecutive 1 bits.
