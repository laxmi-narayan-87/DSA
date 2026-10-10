# 3507. Minimum Pair Removal to Sort Array I

## Problem Statement

Given an array `nums`, you can perform the following operation any number of times:   Select the adjacent pair with the **minimum sum** in `nums` and replace the pair with their sum.   Return the **minimum number of operations** needed to make the array **non-decreasing**.

**Problem Link:** [LeetCode 3507 - Minimum Pair Removal to Sort Array I](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/22-January-2026.md)

---

## Solution

```python
from typing import List

class Solution: 
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operation = 0
        
        def is_sorted(arr):
            """Check if array is non-decreasing"""
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True
        
        # Keep merging pairs until array is sorted
        while not is_sorted(nums):
            # Calculate sum of all adjacent pairs
            pair_sum = [nums[i] + nums[i + 1] for i in range(len(nums) - 1)]
            
            # Find the index of the pair with minimum sum
            min_index = pair_sum.index(min(pair_sum))
            
            # Replace the pair with their sum
            nums[min_index] = pair_sum[min_index]
            nums.pop(min_index + 1)
            
            operation += 1
        
        return operation
```

### Idea

* Use **Simulation** to follow the problem's exact rules
* **Algorithm:**
  1. Check if the array is already non-decreasing → return 0
  2. While array is not sorted:
     - Calculate sums of all adjacent pairs
     - Find the minimum sum and its leftmost position
     - Replace the pair with their sum (merge them)
     - Remove the second element of the pair
     - Increment operation count
  3. Return the total number of operations

### Example Walkthrough

For `nums = [5,2,3,1]`:

**Initial:** `[5, 2, 3, 1]` (not sorted)
- Adjacent pairs: `(5,2)=7`, `(2,3)=5`, `(3,1)=4`
- Minimum sum: 4 at index 2
- Merge: `[5, 2, 4]`
- Operations: 1

**Step 2:** `[5, 2, 4]` (not sorted)
- Adjacent pairs: `(5,2)=7`, `(2,4)=6`
- Minimum sum: 6 at index 1
- Merge: `[5, 6]`
- Operations: 2

**Step 3:** `[5, 6]` (sorted ✓)
- Return 2

---

For `nums = [1,2,2]`:
- Already non-decreasing
- Return 0

### Complexity

* **Time:** `O(n³)` - worst case, we perform O(n) operations, each checking O(n) pairs and sorting check is O(n)
* **Space:** `O(n)` - storing pair sums

### Key Observations

1. **Greedy approach works:** Always merging the minimum sum pair leads to optimal solution
2. **Array shrinks:** Each operation reduces array length by 1
3. **Maximum operations:** At most `n-1` operations (merge all into one element)
4. **Negative numbers:** The algorithm handles negative numbers correctly

### Edge Cases

- Already sorted array → 0 operations
- Array with 1 element → 0 operations (trivially sorted)
- All equal elements → 0 operations
- Decreasing array → Multiple operations needed
