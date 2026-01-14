# 3454. Separate Squares II

## Problem Statement

You are given a 2D integer array `squares`. Each `squares[i] = [xi, yi, li]` represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.  Find the **minimum y-coordinate value** of a horizontal line such that the **total area covered by squares above the line** equals the **total area covered by squares below the line**.

**Note:** Squares may overlap. **Overlapping areas should be counted only once** in this version.

**Problem Link:** [LeetCode 3454 - Separate Squares II](https://leetcode.com/problems/separate-squares-ii/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/14-January-2026.md)

---

## Solution

```python
from typing import List

class Solution: 
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        for x, y, length in squares:
            # Add start and end events for each square
            events.append((y, 1, x, x + length))          # Bottom edge
            events.append((y + length, -1, x, x + length)) # Top edge
        
        events.sort()
        
        active_intervals = []  
        prev_y = events[0][0]
        total_area = 0
        horizontal_slices = [] 
        
        def union_width(intervals):
            """Calculate the total width covered by overlapping intervals"""
            intervals.sort()
            total_width = 0
            rightmost = -10**30
            for left, right in intervals:
                if left > rightmost:
                    total_width += right - left
                    rightmost = right
                elif right > rightmost:
                    total_width += right - rightmost
                    rightmost = right
            return total_width
        
        # Sweep line algorithm
        for y, event_type, x_left, x_right in events: 
            if y > prev_y and active_intervals:
                height = y - prev_y
                width = union_width(active_intervals)
                horizontal_slices. append((prev_y, height, width))
                total_area += height * width
            
            if event_type == 1:
                active_intervals.append((x_left, x_right))
            else:
                active_intervals.remove((x_left, x_right))
            
            prev_y = y
        
        # Find the y-coordinate that splits the area in half
        half_area = total_area / 2
        accumulated_area = 0
        
        for start_y, height, width in horizontal_slices: 
            slice_area = height * width
            if accumulated_area + slice_area >= half_area: 
                return start_y + (half_area - accumulated_area) / width
            accumulated_area += slice_area
        
        return float(prev_y)
```

### Idea

* Use **Sweep Line Algorithm** to handle overlapping squares: 
  1. **Create events:** For each square, create start (bottom) and end (top) events
  2. **Sort events** by y-coordinate
  3. **Process events:** Maintain active intervals at current y-level
  4. **Calculate union:** For overlapping squares, compute the actual covered width using interval union
  5. **Build horizontal slices:** Store each slice with (start_y, height, width)
* **Find the splitting line:**
  - Calculate total area (handling overlaps)
  - Accumulate areas from bottom to top
  - When accumulated area reaches half, interpolate the exact y-coordinate

### Key Differences from Version I

* **Overlaps counted once:** Use interval union to avoid double-counting overlapping regions
* **More complex:** Requires sweep line algorithm instead of simple binary search

### Complexity

* **Time:** `O(n² log n)` - sorting events O(n log n), processing n events with O(n) interval union each
* **Space:** `O(n)` - store events and active intervals
