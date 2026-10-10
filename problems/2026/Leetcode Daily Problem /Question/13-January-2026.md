# 3453. Separate Squares I

## Problem Statement

You are given a 2D integer array `squares`. Each `squares[i] = [xi, yi, li]` represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the **minimum y-coordinate value** of a horizontal line such that the total area of the squares above the line equals the total area below it. Answers within `10^-5` are accepted.

**Note:** Overlapping areas are counted multiple times.

**Problem Link:** [LeetCode 3453 - Separate Squares I](https://leetcode.com/problems/separate-squares-i/)

## Examples

```text
Input: squares = [[0,0,1],[2,2,1]]
Output: 1.00000
```

Any horizontal line between `y = 1` and `y = 2` balances the two areas; the minimum valid value is `1`.

```text
Input: squares = [[0,0,2],[1,1,1]]
Output: 1.16667
```

## Constraints

- `1 <= squares.length <= 5 * 10^4`
- `squares[i] = [xi, yi, li]` and `squares[i].length == 3`
- `0 <= xi, yi <= 10^9`
- `1 <= li <= 10^9`
- The total area of all squares does not exceed `10^12`

## Solution

See the matching implementation in [13-January-2026.md](../Solution%20/13-January-2026.md).
