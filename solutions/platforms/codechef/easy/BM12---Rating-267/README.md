# BM12 - Rating 267

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Debug this code - Determine the Score

The code given in the IDE is incorrect - Try and debug this program!!!

There is a problem worth $X$ points and it has $10$ test cases.
It is known that $X$ is a multiple of $10$.
It is known that each test case is worth the same number of points.
You pass $N$ test cases among them. Determine the score that you will get.

### Input Format
- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $X$ and $N$, the total points for the problem and the number of test cases which pass.
### Output Format

For each test case, output the points scored by you.

### Sample 1:
Input
Output

```
2
10 3
100 10
```

```
3
100
```

### Explanation:

 **Test Case $1$:**  The problem is worth $10$ points and since there are $10$ test cases, each test case is worth $1$ point. Since you pass $3$ test cases, your score will be $1 \cdot 3 = 3$ points.

 **Test Case $2$:**  The problem is worth $100$ points and since there are $10$ test cases, each test case is worth $10$ points. Since you pass all the $10$ test cases, your score will be $10 \cdot 10 = 100$ points.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T18:10:29.022Z  

```py
# The code below is incorrect. Debug the code to solve the problem

t = int(input())
for i in range(t):
    X, N = map(int, input().split())
    points_per_testcase = X//10
    score = points_per_testcase*N
    print(score)
```

---

[View on CodeChef](https://www.codechef.com/problems/BM12)