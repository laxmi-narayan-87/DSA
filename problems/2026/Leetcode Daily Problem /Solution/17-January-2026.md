# 3047. Find the Largest Area of Square Inside Two Rectangles

## Problem Statement

There exist `n` rectangles in a 2D plane with edges parallel to the x and y axis. You are given two 2D integer arrays `bottomLeft` and `topRight`. You need to find the **maximum area of a square** that can fit inside the intersecting region of **at least two rectangles**. Return `0` if such a square does not exist. 

**Problem Link:** [LeetCode 3047 - Find the Largest Area of Square Inside Two Rectangles](https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/17-January-2026.md)

---

## Solution

```python
from typing import List

class Solution: 
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_area = 0
        
        # Check all pairs of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                # Find intersection boundaries
                left = max(bottomLeft[i][0], bottomLeft[j][0])
                right = min(topRight[i][0], topRight[j][0])
                bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                top = min(topRight[i][1], topRight[j][1])
                
                # Check if rectangles intersect
                if left < right and bottom < top:
                    # Calculate the largest square that fits
                    side = min(right - left, top - bottom)
                    max_area = max(max_area, side * side)
        
        return max_area
```

### Idea

* Use **Brute Force** to check all pairs of rectangles
* **Find intersection:** For each pair of rectangles, calculate the intersection region: 
  - `left` = max of left boundaries (rightmost left edge)
  - `right` = min of right boundaries (leftmost right edge)
  - `bottom` = max of bottom boundaries (topmost bottom edge)
  - `top` = min of top boundaries (bottommost top edge)
* **Check validity:** Rectangles intersect if `left < right` and `bottom < top`
* **Calculate square:** The largest square has side length = `min(width, height)` of intersection
  - Width = `right - left`
  - Height = `top - bottom`
* Track the maximum area across all pairs

### Example Walkthrough

For `bottomLeft = [[1,1],[2,2],[3,1]]`, `topRight = [[3,3],[4,4],[6,6]]`:
- Rectangles 0 and 1: intersection = `[2,2]` to `[3,3]` → side = 1 → area = 1
- Rectangles 1 and 2: intersection = `[3,2]` to `[4,3]` → side = 1 → area = 1
- Rectangles 0 and 2: no intersection
- Maximum area = 1

### Complexity

* **Time:** `O(n²)` - check all pairs of rectangles
* **Space:** `O(1)` - only using constant extra space
