# FLOW018 - Rating 760

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Small Factorial

Write a program to find the factorial value of any number entered by the user.

### Input Format

The first line contains an integer  **T**, the total number of testcases. Then  **T**  lines follow, each line contains an integer  **N**.

### Output Format

For each test case, display the factorial of the given number  **N**  in a new line.

### Constraints
- 1 ≤ T ≤ 1000
- 0 ≤ N ≤ 20
### Sample 1:
Input
Output

```
3 
3 
4
5

```

```
6
24
120

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-27T07:22:58.554Z  

```py
# cook your dish here
def fact(n):
    prod=1
    for i in range(1,n+1):
        prod=i*prod
    return prod
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        print(fact(n))
```

---

[View on CodeChef](https://www.codechef.com/problems/FLOW018)