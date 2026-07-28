# Sparse Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results. 

**Example**  

$stringList = ['ab','ab','abc']$  
$queries = ['ab','abc','bc']$  

There are $2$ instances of '$ab$', $1$ of '$abc$', and $0$ of '$bc$'. For each query, add an element to the return array: $results = [2, 1, 0]$.

**Function Description**

Complete the function $matchingStrings$ with the following parameters:

-  $string\ stringList[n]$: an array of strings to search  
-  $string\ queries[q]$: an array of query strings  

**Returns**  

- $int[q]$: the results of each query  

**Input Format**

The first line contains and integer $n$, the size of $stringList[]$.  
Each of the next $n$ lines contains a string $stringList[i]$.  
The next line contains $q$, the size of $queries[]$.  
Each of the next $q$ lines contains a string $queries[i]$.  

**Constraints**

$1 \leq n \leq 1000$  
$1 \leq q \leq 1000$  
$1 \leq |stringList[i]|,|queries[i]| \leq 20$ . 

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-28T10:01:40.081Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#

def matchingStrings(stringList, queries):
    # Write your code here
    freq = {}
    for s in stringList:
        freq[s] = freq.get(s, 0) + 1
    result = []
    for q in queries:
        result.append(freq.get(q, 0))
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/sparse-arrays/problem)