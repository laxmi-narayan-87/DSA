# BM04A

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Division with integer and decimal output

Lets focus a bit more on division to clarify the concept

- $A$ $/$ $B$ will always return a float or decimal value - with 16 digits after decimal for precision For example - $5 / 3$ will return $1.6666666666666667$
- $A$ $//$ $B$ will always return an integer value. $A$ $//$ $B$ is rounded down to the closest integer For example - $5 // 3$ will return 1 For example - $3 // 3$ will return 1 For example - $7 // 3$ will return 2
### Task

In this problem you need to write a program which does the following

- Accepts the number of inputs / test cases as 't' Each line of test case contains 2 integers - declare them as variables $A$ and $B$
- For each test case, you need to perform the following operations Create a variable - $X$ - the division of $A$ and $B$ which returns a float using the operator $/$ Create a variable - $Y$ - the division of $A$ and $B$ which returns a integer using the operator $//$ Output 2 space separated integers - $X$ and $Y$ in a single line
### Sample 1:
Input
Output

```
2
10 5
10 6
```

```
2.0 2
1.6666666666666667 1
```

### Explanation:

 **Test case 1** : The 2 integers are $10$ and $5$ and we output $2.0$ and $2$ as the value of $X$ and $Y$ respectively

 **Test case 2** : The 2 integers are $10$ and $6$ and we output $2.0$ and $1$ as the value of $X$ and $Y$ respectively

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T18:08:30.274Z  

```py
# Update the '_' below to solve the problem

t = int(input())
for i in range(t): 
    a, b = map(int, input().split())
    
    # division of A by B - float / decimal result
    floatDivison = a / b
    
    # division of A by B - integer result
    integerDivison = a // b
    
    print(floatDivison, integerDivison)
```

---

[View on CodeChef](https://www.codechef.com/problems/BM04A)