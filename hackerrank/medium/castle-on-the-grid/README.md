# Castle on the Grid

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a square grid with some cells open (**.**) and some blocked (**X**).  Your playing piece can move along any row or column until it reaches the edge of the grid or a blocked cell.  Given a grid, a start and a goal, determine the minmum number of moves to get to the goal.  

**Example**. 

$grid = \text{['...','.X.','...']}$   
$startX = 0$  
$startY = 0$  
$goalX = 1$  
$goalY = 2$  

The grid is shown below:

    ...
    .X.
    ...
    
The starting position $(startX, startY) = (0,0)$ so start in the top left corner.  The goal is $(goalX, goalY) = (1,2)$.  The path is $(0,0) \rightarrow (0,2) \rightarrow (1,2)$.  It takes $2$ moves to reach the goal.

**Function Description**  
Complete the *minimumMoves* function in the editor.   

minimumMoves has the following parameter(s):

- *string grid[n]:* an array of strings that represent the rows of the grid  
- *int startX:* starting X coordinate    
- *int startY:* starting Y coordinate    
- *int goalX:* ending X coordinate    
- *int goalY:* ending Y coordinate    

**Returns**  

- *int:* the minimum moves to reach the goal

**Input Format**

The first line contains an integer $n$, the size of the array *grid*.   
Each of the next $n$ lines contains a string of length $n$.  
The last line contains four space-separated integers, $\text{startX, startY, goalX, goalY}$  


**Constraints**

- $1 \leq n \leq 100$
- $0 \leq startX,\ startY,\ goalX,\ goalY < n$


**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-30T05:09:24.270Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    n = len(grid)
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((startX, startY))
    dist[startX][startY] = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        x, y = q.popleft()
        if x == goalX and y == goalY:
            return dist[x][y]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != 'X':
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                nx += dx
                ny += dy
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/castle-on-the-grid/problem)