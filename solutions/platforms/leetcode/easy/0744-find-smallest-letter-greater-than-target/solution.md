# 744. Find Smallest Letter Greater Than Target

## Problem Statement

Return the smallest character in sorted array `letters` that is lexicographically greater than `target`. If none exists, return the first character.

**Problem Link:** [LeetCode 744 - Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/31-January-2026.md)

---

## Solution

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        smallest = letters[0]
        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]
        return smallest
```

### Idea

* Store the first character as `smallest` (fallback if no character is greater than target).
* Iterate through the sorted array `letters`.
* Return the first character that is lexicographically greater than `target`.
* If no such character exists, return `smallest` (the first character in the array).
* **Key insight:** Since the array is sorted, the first character greater than target is automatically the smallest such character.

### Complexity

* **Time:** `O(n)` - Linear search through the array
* **Space:** `O(1)` - Only using a single variable

---

## Optimized Solution (Binary Search)

```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        result = letters[0]
        
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                result = letters[mid]
                right = mid - 1
            else:
                left = mid + 1
        
        return result
```

### Idea

* Use **binary search** since the array is sorted.
* Find the leftmost character that is greater than `target`.
* If found, return it; otherwise, return the first character.

### Complexity

* **Time:** `O(log n)` - Binary search
* **Space:** `O(1)` - Constant space
