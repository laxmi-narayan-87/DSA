# 3453. Separate Squares I

## Problem Statement

You are given a 2D integer array `squares`. Each `squares[i] = [xi, yi, li]` represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.  Find the **minimum y-coordinate value** of a horizontal line such that the **total area of the squares above the line** equals the **total area of the squares below the line**.

**Problem Link:** [LeetCode 3453 - Separate Squares I](https://leetcode.com/problems/separate-squares-i/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/13-January-2026.md)

---

## Solution

```python
from typing import List

class Solution: 
    def separateSquares(self, squares: List[List[int]]) -> float:
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)
        
        def balance(mid:  float):
            above = below = 0.0
            for x, y0, l in squares: 
                if mid <= y0:
                    # Entire square is above the line
                    above += l * l
                elif mid >= y0 + l:
                    # Entire square is below the line
                    below += l * l
                else:
                    # Square is split by the line
                    below += l * (mid - y0)
                    above += l * (y0 + l - mid)
            return above, below
        
        # Binary search for the balance point
        for _ in range(60):  # 60 iterations for precision within 10^-5
            mid = (low + high) / 2
            above, below = balance(mid)
            if below < above:
                low = mid
            else:
                high = mid
        
        return low
```

### Idea

* Use **Binary Search** to find the y-coordinate where areas are balanced
* **Search range:**
  - `low` = minimum y-coordinate of all squares (bottom-most point)
  - `high` = maximum y-coordinate of all squares (top-most point)
* **For each candidate line at y = mid:**
  - Calculate area above and below the line
  - If square is entirely above or below, count full area
  - If square is split, calculate partial areas based on intersection
* **Binary search adjustment:**
  - If `below < above`: move line up (`low = mid`)
  - Otherwise: move line down (`high = mid`)
* Run 60 iterations to achieve precision within `10^-5`

### Complexity

* **Time:** `O(n × log(range))` - 60 iterations × n squares = `O(60n) = O(n)`
* **Space:** `O(1)` - only using constant extra space
