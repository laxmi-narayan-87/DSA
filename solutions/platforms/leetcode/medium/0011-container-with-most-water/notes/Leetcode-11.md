# LeetCode 11: Container With Most Water

[![LeetCode](https://img.shields.io/badge/LeetCode-11-orange)](https://leetcode.com/problems/container-with-most-water/)

---

## Problem

Given an array `height` of length `n`, where each element represents a vertical line on the x-axis at position `i` with height `height[i]`, find **two lines** such that together with the x-axis they form a container that **holds the most water**. Return the maximum area of water the container can hold.

**Constraints:**

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

---

## Example

**Input:**
```python
height = [1,8,6,2,5,4,8,3,7]
```
**Output:**
```
49
```
**Explanation:**
Choosing lines at positions 1 and 8 → min(8,7) * (8-1) = 7*7 = 49

---

## Approaches

### Approach 1: Brute Force

**Idea:**  
Check all pairs (i, j) and calculate the area. Keep track of the maximum.

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        for i in range(n):
            for j in range(i+1, n):
                area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, area)
        return max_area
```
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)

*Drawback: Too slow for large inputs.*

---

### Approach 2: Two Pointers (Optimal)

**Idea:**

- Initialize two pointers, `left = 0` and `right = n-1`.
- Calculate area between left and right.
- Move the pointer pointing to the smaller height inward.
- Repeat until pointers meet.

*Rationale: Moving the smaller line can potentially increase the height while reducing width minimally, maximizing area.*

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_area = 0
        
        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
```
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## Key Insights

- Area depends on min height * width.
- Always move the smaller height pointer to potentially increase min height.
- Two pointers approach eliminates unnecessary pair checks.

---

## Tags

#two-pointers #greedy #array #medium
