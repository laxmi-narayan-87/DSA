# GS14

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### String mirror - Double strings

Listen

Write a program in the IDE which does the following

- Accepts the count of test cases - $t$ - in the 1st line First line of each test case consists of a string $S$
- You need to perform the following operation Create a variable $X$ which contains the string $S$ concatenated with the string $S$ Output $X$ for each test case

We learned how to concatenate two strings in learn python course.

### Sample 1:
Input
Output

```
3
ab
bc
cd
```

```
abab
bcbc
cdcd
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-31T11:24:00.909Z  

```py
t = int(input())
for i in range(t):
    # take input and output the join using +
    x=input()
    print(x*2)
```

---

[View on CodeChef](https://www.codechef.com/problems/GS14)