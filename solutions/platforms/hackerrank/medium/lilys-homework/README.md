# Lily's Homework

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Whenever George asks Lily to hang out, she's busy doing homework. George wants to help her finish it faster, but he's in over his head! Can you help George understand Lily's homework so she can hang out with him?

Consider an array of $n$ distinct integers, $arr = [a[0], a[1], \ldots, a[n-1]]$. George can swap any two elements of the array any number of times. An array is *beautiful* if the sum of $|arr[i] - arr[i-1]|$ among $0 < i \lt n$ is minimal.

Given the array $arr$, determine and return the minimum number of swaps that should be performed in order to make the array *beautiful*.

**Example**   

$arr = [7, 15, 12, 3]$   

One minimal array is $[3, 7, 12, 15]$.  To get there, George performed the following swaps:

<pre>
	Swap      Result
    	  [7, 15, 12, 3]
	3 7   [3, 15, 12, 7]
    7 15  [3, 7, 12, 15]
   </pre>
    
It took $2$ swaps to make the array beautiful. This is minimal among the choices of beautiful arrays possible.

**Function Description**  

Complete the *lilysHomework* function in the editor below.   

lilysHomework has the following parameter(s):  

- *int arr[n]:* an integer array   

**Returns**  

- *int:* the minimum number of swaps required   

**Input Format**

The first line contains a single integer, $n$, the number of elements in $arr$.	
The second line contains $n$ space-separated integers, $arr[i]$.

**Constraints**

- $1 \le n \le 10^5$
- $1 \le arr[i] \le 2 \times 10^9$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T10:38:11.974Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    # Write your code here
    def count_swaps(target):
        a = arr[:]
        pos = {value: i for i, value in enumerate(a)}
        swaps = 0

        for i in range(len(a)):
            if a[i] != target[i]:
                j = pos[target[i]]

                a[i], a[j] = a[j], a[i]

                pos[a[j]] = j
                pos[a[i]] = i

                swaps += 1

        return swaps

    ascending = sorted(arr)
    descending = ascending[::-1]

    return min(count_swaps(ascending), count_swaps(descending))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/lilys-homework/problem)