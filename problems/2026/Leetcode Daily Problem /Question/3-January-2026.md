# 1411. Number of Ways to Paint N × 3 Grid

## Problem Statement

You are given a grid of size `n × 3`. You want to paint each cell of the grid with **exactly one** of the three colors: 

- Red
- Yellow
- Green

### Rules:
- No two **adjacent cells** may have the same color.
- Adjacent means cells that share a **horizontal or vertical** side.

Given `n`, the number of rows of the grid, return the **number of valid ways** to paint the grid.

Since the answer can be very large, return it **modulo `10^9 + 7`**.

**Problem Link:** [LeetCode 1411 - Number of Ways to Paint N × 3 Grid](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/)

---

## Examples

### Example 1
```
Input:  n = 1
Output: 12
```
**Explanation:**  
There are 12 possible valid colorings for a 1 × 3 grid.

---

### Example 2
```
Input:  n = 5000
Output: 30228214
```

---

## Constraints

- `1 <= n <= 5000`
- `n == grid.length`
