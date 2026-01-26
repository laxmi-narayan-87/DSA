# 1200. Minimum Absolute Difference

## Problem Statement

Given an array of **distinct** integers `arr`, find all pairs of elements with the **minimum absolute difference** of any two elements.

Return a list of pairs in **ascending order** (with respect to pairs), each pair `[a, b]` follows:

- `a`, `b` are from `arr`
- `a < b`
- `b - a` equals to the minimum absolute difference of any two elements in `arr`

**Problem Link:** [LeetCode 1200 - Minimum Absolute Difference](https://leetcode.com/problems/minimum-absolute-difference/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/26-January-2026.md)

---

## Solution 1: Single Pass

```python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        ans = []
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min_diff:
                min_diff = diff
                ans = [[arr[i], arr[i + 1]]]
            elif diff == min_diff:
                ans.append([arr[i], arr[i + 1]])
        return ans
```

### Idea

* Sort the array in ascending order.
* Iterate through adjacent pairs and calculate their difference.
* If a smaller difference is found, reset the result list with the new pair.
* If the same minimum difference is found, append the pair to the result.
* Since the array is sorted, pairs are automatically in ascending order.

### Complexity

* **Time:** `O(n log n)` - Dominated by sorting
* **Space:** `O(1)` - Excluding output array

---

## Solution 2: Two Pass

```python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min_diff:
                min_diff = diff
        ans = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff:
                ans.append([arr[i], arr[i + 1]])
        return ans
```

### Idea

* Sort the array in ascending order.
* **First pass:** Find the minimum absolute difference between adjacent elements.
* **Second pass:** Collect all pairs that have this minimum difference.
* More readable but slightly less efficient due to two passes.

### Complexity

* **Time:** `O(n log n)` - Dominated by sorting
* **Space:** `O(1)` - Excluding output array

---

## Comparison

| Approach | Passes | Pros | Cons |
|----------|--------|------|------|
| Single Pass | 1 | More efficient, single iteration | Slightly more complex logic |
| Two Pass | 2 | Clearer separation of concerns | Two iterations through array |

Both solutions have the same time complexity. The single-pass approach is more efficient in practice.
