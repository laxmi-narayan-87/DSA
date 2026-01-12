# 1266. Minimum Time Visiting All Points

## Problem Statement

On a 2D plane, there are `n` points with integer coordinates `points[i] = [xi, yi]`. Return the **minimum time in seconds** to visit all the points in the order given by `points`. You can move vertically, horizontally, or diagonally (one unit each direction) in 1 second.

**Problem Link:** [LeetCode 1266 - Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/12-January-2026.md)

---

## Solution

```python
from typing import List

class Solution: 
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]
            time += max(abs(x2 - x1), abs(y2 - y1))
        return time
```

### Idea

* The minimum time between two points is the **Chebyshev distance**:  `max(|x2 - x1|, |y2 - y1|)`
* **Why? ** Move diagonally as much as possible, then move straight: 
  - Diagonal moves cover both x and y distance simultaneously
  - Continue diagonally until aligned on one axis
  - Then move straight along the remaining axis
* For each consecutive pair of points, calculate the maximum of horizontal and vertical distances
* Sum up all the times to get the total minimum time

### Complexity

* **Time:** `O(n)` - iterate through all points once
* **Space:** `O(1)` - only using constant extra space
