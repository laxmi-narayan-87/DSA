# 3010. Divide an Array Into Subarrays With Minimum Cost I

## Problem Statement

Find the minimum sum of costs when dividing array `nums` into 3 disjoint contiguous subarrays, where the cost of each subarray is its first element.

**Problem Link:** [LeetCode 3010 - Divide an Array Into Subarrays With Minimum Cost I](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/)

**Related:** [February 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/February%20/Leetcode%20Daily%20Problems/Question/1-February-2026.md)

---

## Solution 1: Brute Force

```python
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                cost = nums[0] + nums[i] + nums[j]
                ans = min(ans, cost)
        return ans
```

### Idea

* Try all possible ways to divide the array into 3 subarrays.
* The first subarray always starts at index 0, so its cost is always `nums[0]`.
* Try all possible starting positions `i` for the second subarray (1 to n-2).
* Try all possible starting positions `j` for the third subarray (i+1 to n-1).
* Calculate total cost: `nums[0] + nums[i] + nums[j]`.
* Track and return the minimum cost found.

### Complexity

* **Time:** `O(n²)` - Nested loops iterating through all possible split positions
* **Space:** `O(1)` - Only using variables

---

## Solution 2: Greedy with Sorting

```python
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        return nums[0] + sum(sorted(nums[1:])[:2])
```

### Idea

* **Key observation:** The first subarray must start at index 0, so its cost is fixed at `nums[0]`.
* The second and third subarrays can start at any positions in `nums[1:]`.
* To minimize total cost, we want the two smallest values from `nums[1:]` as starting points.
* Sort `nums[1:]` and take the sum of the two smallest elements.
* Add `nums[0]` to get the minimum total cost.
* **Why this works:** Since we only care about the first element of each subarray, and the subarrays just need to be contiguous (not necessarily non-empty except for having a first element), we can always arrange them to start with the smallest available values.

### Complexity

* **Time:** `O(n log n)` - Dominated by sorting
* **Space:** `O(n)` - For the sorted slice

---

## Solution 3: Linear Scan (Most Optimal)

```python
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min1 = min2 = float('inf')
        for i in range(1, len(nums)):
            if nums[i] < min1:
                min2 = min1
                min1 = nums[i]
            elif nums[i] < min2:
                min2 = nums[i]
        return nums[0] + min1 + min2
```

### Idea

* The first subarray cost is fixed at `nums[0]`.
* Find the two smallest elements in `nums[1:]` using a single pass.
* Maintain two variables: `min1` (smallest) and `min2` (second smallest).
* For each element:
  - If it's smaller than `min1`, update both `min2 = min1` and `min1 = element`.
  - Otherwise, if it's smaller than `min2`, update `min2 = element`.
* Return `nums[0] + min1 + min2`.
* **Optimization:** Avoids sorting by only tracking the two minimum values.

### Complexity

* **Time:** `O(n)` - Single pass through the array
* **Space:** `O(1)` - Only using two variables

---

## Comparison

| Approach | Time | Space | Best For |
|----------|------|-------|----------|
| Brute Force | O(n²) | O(1) | Understanding the problem |
| Sorting | O(n log n) | O(n) | Clean, concise code |
| Linear Scan | O(n) | O(1) | Optimal performance |
