# 3637. Trionic Array I

## Problem Statement

Return true if array `nums` can be divided into three consecutive segments: strictly increasing, strictly decreasing, and strictly increasing, with valid split indices p and q.

**Problem Link:** [LeetCode 3637 - Trionic Array I](https://leetcode.com/problems/trionic-array-i/)

**Related:** [February 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/February%20/Leetcode%20Daily%20Problems/Question/03-February-2026.md)

---

## Solution 1: Brute Force

```python
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        for p in range(1, n - 1):
            for q in range(p + 1, n - 1):
                flag = True
                # Check if nums[0...p] is strictly increasing
                for i in range(0, p):
                    if nums[i] >= nums[i + 1]:
                        flag = False
                        break
                # Check if nums[p...q] is strictly decreasing
                for i in range(p, q):
                    if nums[i] <= nums[i + 1]:
                        flag = False
                        break
                # Check if nums[q...n-1] is strictly increasing
                for i in range(q, n - 1):
                    if nums[i] >= nums[i + 1]:
                        flag = False
                        break
                if flag:
                    return True
        return False
```

### Idea

* Try all possible combinations of split indices `p` and `q` where `0 < p < q < n-1`.
* For each combination:
  - Verify `nums[0...p]` is strictly increasing
  - Verify `nums[p...q]` is strictly decreasing
  - Verify `nums[q...n-1]` is strictly increasing
* If all three conditions are satisfied for any (p, q) pair, return `true`.
* If no valid combination exists, return `false`.

### Complexity

* **Time:** `O(n³)` - Two nested loops for p and q, and linear validation for each pair
* **Space:** `O(1)` - Only using variables

---

## Solution 2: Preprocessing with State Arrays

```python
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # inc[i] = True if nums[0...i] is strictly increasing
        inc = [False] * n
        inc[0] = True
        for i in range(1, n):
            inc[i] = inc[i - 1] and nums[i] > nums[i - 1]
        
        # dec[i] = True if nums[i...n-1] is strictly decreasing
        dec = [False] * n
        dec[n - 1] = True
        for i in range(n - 2, -1, -1):
            dec[i] = dec[i + 1] and nums[i] > nums[i + 1]
        
        # Try all possible p and q
        for p in range(1, n - 1):
            if not inc[p]:
                continue
            for q in range(p + 1, n - 1):
                # Check if middle segment is strictly decreasing
                is_dec = True
                for i in range(p, q):
                    if nums[i] <= nums[i + 1]:
                        is_dec = False
                        break
                
                if is_dec and dec[q]:
                    return True
        
        return False
```

### Idea

* **Preprocessing:** Build two boolean arrays to avoid redundant checks:
  - `inc[i]`: True if `nums[0...i]` is strictly increasing
  - `dec[i]`: True if `nums[i...n-1]` is strictly decreasing
* For each potential split (p, q):
  - Check if `inc[p]` is True (first segment is valid)
  - Check if middle segment `nums[p...q]` is strictly decreasing
  - Check if `dec[q]` is True (third segment is valid)
* Return `true` if any valid split is found.

### Complexity

* **Time:** `O(n³)` - Still need to check middle segment for each (p, q) pair
* **Space:** `O(n)` - For preprocessing arrays

---

## Solution 3: Optimized with Full Preprocessing

```python
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # canInc[i] = True if nums[0...i] is strictly increasing
        canInc = [False] * n
        canInc[0] = True
        for i in range(1, n):
            canInc[i] = canInc[i - 1] and nums[i] > nums[i - 1]
        
        # canDec[i][j] = True if nums[i...j] is strictly decreasing
        canDec = [[False] * n for _ in range(n)]
        for i in range(n):
            canDec[i][i] = True
            for j in range(i + 1, n):
                canDec[i][j] = (j == i + 1 or canDec[i][j - 1]) and nums[j - 1] > nums[j]
        
        # incFrom[i] = True if nums[i...n-1] is strictly increasing
        incFrom = [False] * n
        incFrom[n - 1] = True
        for i in range(n - 2, -1, -1):
            incFrom[i] = incFrom[i + 1] and nums[i] < nums[i + 1]
        
        # Try all possible p and q
        for p in range(1, n - 1):
            if not canInc[p]:
                continue
            for q in range(p + 1, n - 1):
                if canDec[p][q] and incFrom[q]:
                    return True
        
        return False
```

### Idea

* **Full preprocessing:** Pre-compute all necessary checks:
  - `canInc[i]`: nums[0...i] is strictly increasing
  - `canDec[i][j]`: nums[i...j] is strictly decreasing
  - `incFrom[i]`: nums[i...n-1] is strictly increasing
* For each (p, q) pair, simply lookup the precomputed values in O(1).
* Return `true` if any valid configuration exists.

### Complexity

* **Time:** `O(n²)` - O(n²) preprocessing + O(n²) checking pairs
* **Space:** `O(n²)` - For the 2D decreasing array

---

## Comparison

| Approach | Time | Space | Best For |
|----------|------|-------|----------|
| Brute Force | O(n³) | O(1) | Simple implementation |
| Partial Preprocessing | O(n³) | O(n) | Balanced approach |
| Full Preprocessing | O(n²) | O(n²) | Optimal time complexity |
