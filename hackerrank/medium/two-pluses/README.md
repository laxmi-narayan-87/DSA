# Ema's Supercomputer

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Ema built a quantum computer! Help her test its capabilities by solving the problem below.

------

Given a grid of size $n \times m$, each cell in the grid is either $good$ or $bad$.

A *valid* plus is defined here as the crossing of two segments (horizontal and vertical) of equal lengths. These lengths must be odd, and the middle cell of its horizontal segment must cross the middle cell of its vertical segment.	

In the diagram below, the blue pluses are *valid* and the orange ones are *not valid*.
<img src="https://s3.amazonaws.com/hr-challenge-images/13512/1445015866-5e338e8b70-pluseses.png" title="pluseses.png" /><br>

Find the two largest *valid* pluses that can be drawn on $good$ cells in the grid, and return an integer denoting the maximum product of their areas.  In the above diagrams, our largest pluses have areas of $5$ and $9$.  The product of their areas is $5 \times 9 = 45$.

**Note:** The two pluses *cannot* overlap, and the product of their areas should be maximal.

**Function Description**  

Complete the *twoPluses* function in the editor below.  It should return an integer that represents the area of the two largest pluses.

twoPluses has the following parameter(s):  

- *grid*: an array of strings where each string represents a row and each character of the string represents a column of that row  

**Input Format**

The first line contains two space-separated integers, $n$ and $m$.  
Each of the next $n$ lines contains a string of $m$ characters where each character is either **G** ($good$) or **B** ($bad$). These strings represent the rows of the grid.  If the $y^{th}$ character in the $x^{th}$ line is **G**, then $(x,y)$ is a $good$ cell.  Otherwise it's a $bad$ cell.




**Constraints**

* $2 \le n \le 15$<br>
* $2 \le m \le 15$<br>

**Output Format**

Find $2$ pluses that can be drawn on $good$ cells of the grid, and return an integer denoting the maximum product of their areas.

**Sample Input 0**

    5 6
    GGGGGG
    GBBBGB
    GGGGGG
    GGBBGB
    GGGGGG
    
**Sample Output 0**

	5

**Sample Input 1**
    
    6 6
    BGBBGB
    GGGGGG
    BGBBGB
    GGGGGG
    BGBBGB
    BGBBGB

**Sample Output 1**

	25

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T10:40:29.212Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    # Write your code here
    n = len(grid)
    m = len(grid[0])

    pluses = []

    for r in range(n):
        for c in range(m):

            if grid[r][c] != 'G':
                continue

            k = 0

            while True:
                if (r-k < 0 or
                    r+k >= n or
                    c-k < 0 or
                    c+k >= m):
                    break

                if (grid[r-k][c] != 'G' or
                    grid[r+k][c] != 'G' or
                    grid[r][c-k] != 'G' or
                    grid[r][c+k] != 'G'):
                    break

                area = 1 + 4 * k

                cells = set()

                for x in range(r-k, r+k+1):
                    cells.add((x, c))

                for y in range(c-k, c+k+1):
                    cells.add((r, y))

                pluses.append((area, cells))

                k += 1

    ans = 0

    for i in range(len(pluses)):
        area1, cells1 = pluses[i]

        for j in range(i + 1, len(pluses)):
            area2, cells2 = pluses[j]

            if cells1.isdisjoint(cells2):
                ans = max(ans, area1 * area2)

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/two-pluses/problem)