# 3315. Construct the Minimum Bitwise Array II

## Problem Statement

You are given an array `nums` consisting of `n` **prime integers**.  You need to construct an array `ans` of length `n`, such that, for each index `i`, the bitwise OR of `ans[i]` and `ans[i] + 1` is equal to `nums[i]`, i.e. `ans[i] OR (ans[i] + 1) == nums[i]`.  Additionally, you must **minimize** each value of `ans[i]` in the resulting array.

**Problem Link:** [LeetCode 3315 - Construct the Minimum Bitwise Array II](https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/21-January-2026.md)

---

## Solution 1: Iterative Bit Checking

```python
from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            res = -1
            d = 1
            # Check bits from right to left
            while (nums[i] & d) != 0:
                res = nums[i] - d
                d <<= 1  # Shift to next bit position
            nums[i] = res
        return nums
```

### Idea (Solution 1)

* **Iterate through bits** from LSB to MSB
* **Key insight:** Keep subtracting powers of 2 while the bit is set
* **Algorithm:**
  1. Start with `d = 1` (checking LSB)
  2. While bit at position `d` is 1 in `nums[i]`:
     - Set `res = nums[i] - d` (remove that bit)
     - Shift `d` left to check next bit
  3. The last valid subtraction gives the minimum answer
  4. If no bits are set (even number), remains -1

---

## Solution 2: Count Trailing Ones

```python
from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for p in nums: 
            if p % 2 == 0:  # Even number, no solution
                res.append(-1)
                continue
            
            # Count consecutive 1s from the right
            r = 0
            t = p
            while t & 1:
                r += 1
                t >>= 1
            
            # Subtract 2^(r-1) to flip the rightmost bit in the sequence
            res.append(p - (1 << (r - 1)))
        return res
```

### Idea (Solution 2)

* **Count trailing 1s** then subtract appropriate power of 2
* **Key insight:** Find how many consecutive 1s from the right, then flip the rightmost one
* **Algorithm:**
  1. If number is even → return -1
  2. Count consecutive 1s from LSB (let's call it `r`)
  3. Subtract `2^(r-1)` to flip the rightmost 1 in that sequence
  4. This gives the minimum valid answer

---

## Binary Pattern Analysis

Both solutions achieve the same result through different methods:

```
num = 11 = 1011:
  - Has 2 trailing 1s (positions 0-1)
  - Subtract 2^(2-1) = 2^1 = 2
  - Result: 11 - 2 = 9 = 1001 ✓

num = 13 = 1101:
  - Has 1 trailing 1 (position 0)
  - Subtract 2^(1-1) = 2^0 = 1
  - Result:  13 - 1 = 12 = 1100 ✓

num = 31 = 11111:
  - Has 5 trailing 1s (positions 0-4)
  - Subtract 2^(5-1) = 2^4 = 16
  - Result: 31 - 16 = 15 = 01111 ✓

num = 7 = 111:
  - Has 3 trailing 1s (positions 0-2)
  - Subtract 2^(3-1) = 2^2 = 4
  - Result: 7 - 4 = 3 = 011 ✓
```

---

## Why This Works

**Understanding `j | (j + 1)`:**
- When we add 1 to `j`, it flips the rightmost 0 bit to 1
- All trailing 1s become 0
- ORing `j` with `j + 1` fills in those zeros with 1s

**Finding minimum `j`:**
- We need to identify which 1 bit to "remove" from `num`
- The rightmost bit we can remove is in the trailing sequence of 1s
- Removing the leftmost bit of that sequence gives the minimum value

**Example:** `num = 1011`
- Trailing 1s: positions 0-1
- We can remove bit at position 1
- Result: `1001` → verify: `1001 | 1010 = 1011` ✓

---

## Complexity

### Solution 1
* **Time:** `O(n × log(max(nums)))` - for each number, check at most 30 bits
* **Space:** `O(1)` - modifies input array in place

### Solution 2
* **Time:** `O(n × log(max(nums)))` - for each number, count trailing 1s
* **Space:** `O(n)` - creates new result array

---

## Comparison

| Aspect | Solution 1 | Solution 2 |
|--------|-----------|------------|
| Approach | Iterative bit checking | Count trailing 1s |
| Clarity | Less intuitive | More intuitive |
| Memory | In-place modification | New array |
| Edge case handling | Implicit | Explicit check |
