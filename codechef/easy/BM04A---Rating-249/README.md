# BM04A - Rating 249

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Practice problem - Squats

Some more practice problems for you to do yourself.

You decided to do $X$ sets of squats at the gym today.
Each set consists of $15$ squats.
Determine the total number of squats that you did today.

### Input Format
- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains an integer $X$ — the total number of sets of squats that you did.
### Output Format

For each test case, output the total number of squats done.

### Sample 1:
Input
Output

```
3
1
4
99

```

```
15
60
1485

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T18:09:16.584Z  

```py
#Update the code below to solve the problem

t = int(input())
for i in range(t):
    X = int(input())
    print(15*X)
```

---

[View on CodeChef](https://www.codechef.com/problems/BM04A)