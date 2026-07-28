# Truck Tour

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Suppose there is a circle. There are $N$ petrol pumps on that circle. Petrol pumps are numbered $0$ to $(N-1)$ (both inclusive). You have two pieces of information corresponding to each of the petrol pump: (1) the amount of petrol that particular petrol pump will give, and (2) the distance from that petrol pump to the next petrol pump. 

Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol pumps. Calculate the first point from where the truck will be able to complete the circle. Consider that the truck will stop at each of the petrol pumps. The truck will move one kilometer for each litre of the petrol.


**Input Format**

The first line will contain the value of $N$.<br>
The next $N$ lines will contain a pair of integers each, i.e. the amount of petrol that petrol pump will give and the distance between that petrol pump and the next petrol pump.

**Constraints:**<br>
$ 1 \le N \le 10^5$<br>
$ 1 \le \text{amount of petrol, distance} \le 10^9$

**Constraints**

 

**Output Format**

An integer which will be the smallest index of the petrol pump from which we can start the tour.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-28T10:13:16.318Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    start = 0
    current_balance = 0
    total_balance = 0
    for i in range(len(petrolpumps)):
        petrol, distance = petrolpumps[i]
        balance = petrol - distance
        current_balance += balance
        total_balance += balance
        if current_balance < 0:
            start = i + 1
            current_balance = 0
    return start
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/truck-tour/problem)