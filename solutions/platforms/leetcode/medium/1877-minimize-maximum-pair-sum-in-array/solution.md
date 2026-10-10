# 1877. Minimize Maximum Pair Sum in Array

## Problem Statement

The pair sum of a pair `(a, b)` is equal to `a + b`. The maximum pair sum is the largest pair sum in a list of pairs.

Given an array `nums` of **even** length `n`, pair up the elements of `nums` into `n / 2` pairs such that:

- Each element of `nums` is in **exactly one** pair, and
- The **maximum pair sum** is **minimized**.

Return the minimized maximum pair sum after optimally pairing up the elements.

**Problem Link:** [LeetCode 1877 - Minimize Maximum Pair Sum in Array](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/24-January-2026.md)

---

## Solution 1: Sorting (Two Pointers)

```python
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        n = len(nums)
        for i in range(n // 2):
            current = nums[i] + nums[n - 1 - i]
            if result < current:
                result = current
        return result
```

### Idea

* **Sort** the array in ascending order.
* Use **two pointers** approach: pair the smallest with the largest element.
* Pair `nums[0]` with `nums[n-1]`, `nums[1]` with `nums[n-2]`, and so on.
* This **greedy strategy** minimizes the maximum pair sum by balancing extremes.
* Track and return the maximum sum among all pairs.

### Complexity

* **Time:** `O(n log n)` - Dominated by sorting
* **Space:** `O(1)` - Only using variables (excluding sorting space)

---

## Solution 2: Counting Sort (Optimized for Range)

```python
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_val = max(nums)
        count = [0] * (max_val + 1)
        for num in nums:
            count[num] += 1
        l, r = 0, max_val
        res = 0
        while l <= r:
            while l <= r and count[l] == 0:
                l += 1
            while l <= r and count[r] == 0:
                r -= 1
            if l <= r and count[l] > 0 and count[r] > 0:
                res = max(res, l + r)
                count[l] -= 1
                count[r] -= 1
        return res
```

### Idea

* Use **counting sort** technique with a frequency array.
* Count occurrences of each number in the input range `[0, max_val]`.
* Use **two pointers** (`l` for smallest, `r` for largest) on the count array.
* Skip indices with zero count and pair the smallest available with the largest available.
* Decrement counts after pairing and track the maximum pair sum.
* **Advantage:** Can be faster than comparison-based sorting when the range is small.

### Complexity

* **Time:** `O(n + max_val)` - Linear pass + pointer traversal
* **Space:** `O(max_val)` - Frequency array

---

## Comparison

| Approach | Time Complexity | Space Complexity | Best Use Case |
|----------|----------------|------------------|---------------|
| Sorting | `O(n log n)` | `O(1)` | General purpose, large ranges |
| Counting Sort | `O(n + max_val)` | `O(max_val)` | Small value range (≤ 10^5) |

**When to use Counting Sort:**
- When `max_val` is reasonable (≤ 10^5 as per constraints)
- Can be faster in practice for this problem's constraints

**When to use Regular Sorting:**
- More space-efficient
- Cleaner, more readable code
- Better for very large value ranges
