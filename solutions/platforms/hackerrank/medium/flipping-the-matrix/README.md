# Flipping the Matrix

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Sean invented a game involving a $2n \times 2n$ matrix where each cell of the matrix contains an integer. He can reverse any of its rows or columns any number of times.  The goal of the game is to maximize the sum of the elements in the $n \times n$ submatrix located in the upper-left quadrant of the matrix.

Given the initial configurations for $q$ matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.  

**Example**  
$matrix = [[1, 2], [3, 4]]$  

```
1 2
3 4
```
It is $2 \times 2$ and we want to maximize the top left quadrant, a $1 \times 1$ matrix.  Reverse row $1$:
```
1 2
4 3
```
And now reverse column $0$:
```
4 2
1 3
```
The maximal sum is $4$.

**Function Description**  

Complete the *flippingMatrix* function in the editor below.  

flippingMatrix has the following parameters:  
- *int matrix[2n][2n]:* a 2-dimensional array of integers  

**Returns**  
- *int:* the maximum sum possible.   

**Input Format**

The first line contains an integer $q$, the number of queries.   

The next $q$ sets of lines are in the following format:

- The first line of each query contains an integer, $n$. 
- Each of the next $2n$ lines contains $2n$ space-separated integers $matrix[i][j]$ in row $i$ of the matrix.  

**Constraints**

+ $1 \le q \le 16$  
+ $1 \le n \le 128$  
+ $0 \le matrix[i][j] \le 4096$, where $0 \le i, j \lt 2n$.

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-21T10:50:18.786Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix) // 2
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += max(matrix[i][j],matrix[i][2*n - 1 - j],matrix[2*n - 1 - i][j],matrix[2*n - 1 - i][2*n - 1 - j])
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/flipping-the-matrix/problem)