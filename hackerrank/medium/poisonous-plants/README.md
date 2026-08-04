# Poisonous Plants

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There are a number of plants in a garden. Each of the plants has been treated with some amount of pesticide. After each day, if any plant has more pesticide than the plant on its left, being weaker than the left one, it dies.  
  
You are given the initial values of the pesticide in each of the plants. Determine the number of days after which no plant dies, i.e. the time after which there is no plant with more pesticide content than the plant to its left.  
  
**Example**  

$p = [3,6,2,7,5]$  // pesticide levels

Use a $1$-indexed array.  On day $1$, plants $2$ and $4$ die leaving $p' = [3,2,5]$.  On day $2$, plant $3$ in $p'$ dies leaving $p'' = [3,2]$.  There is no plant with a higher concentration of pesticide than the one to its left, so plants stop dying after day $2$.  

**Function Description**  
Complete the function *poisonousPlants* in the editor below.  

poisonousPlants has the following parameter(s):

- *int p[n]*: the pesticide levels in each plant  

Returns  
- *int*: the number of days until plants no longer die from pesticide  

**Input Format**

The first line contains an integer $n$, the size of the array $p$.  
The next line contains $n$ space-separated integers $p[i]$.  


**Constraints**

$1 \le n \le 10^5$  
$0 \le p[i] \le 10^9$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-04T11:07:56.995Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    # Write your code here
    stack = []
    ans = 0

    for x in p:
        days = 0

        while stack and x <= stack[-1][0]:
            days = max(days, stack.pop()[1])

        if not stack:
            days = 0
        else:
            days += 1

        ans = max(ans, days)
        stack.append((x, days))

    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/poisonous-plants/problem)