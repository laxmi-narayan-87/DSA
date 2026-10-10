# 1984. Minimum Difference Between Highest and Lowest of K Scores

## Problem Statement

Given a 0-indexed integer array nums and an integer k, pick k students' scores to minimize the difference between the highest and lowest scores.

**Problem Link:** [LeetCode 1984 - Minimum Difference Between Highest and Lowest of K Scores](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/25-January-2026.md)

---

## Solution

```python
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        min_diff = float('inf')
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            min_diff = min(min_diff, diff)
        return min_diff
```

### Idea

* Sort the array to arrange scores in ascending order.
* Use a sliding window of size `k` to find consecutive elements.
* For each window, calculate the difference between the last and first element.
* The minimum difference comes from selecting `k` consecutive elements after sorting.

### Complexity

* **Time:** `O(n log n)`
* **Space:** `O(1)` (excluding sorting space)
