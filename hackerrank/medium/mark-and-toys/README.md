# Mark and Toys

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.

 **Note**  Each toy can be purchased only once.

 **Example** 

The budget is units of currency. He can buy items that cost for, or for units. The maximum is items.

 **Function Description** 

Complete the function  *maximumToys*  in the editor below.

maximumToys has the following parameter(s):

- int prices[n]: the toy prices
- int k: Mark's budget

 **Returns** 

- int: the maximum number of toys

 **Input Format** 

The first line contains two integers, and, the number of priced toys and the amount Mark has to spend.
The next line contains space-separated integers

 **Constraints** 

A toy can't be bought multiple times.

 **Sample Input** 

```
7 50
1 12 5 111 200 1000 10

```

 **Sample Output** 

```
4

```

 **Explanation** 

He can buy only toys at most. These toys have the following prices:.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T10:24:41.315Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    prices.sort()
    psum=0
    for i in range(len(prices)):
        psum=psum+prices[i]
        if psum>k:
            return i
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/mark-and-toys/problem)