# BM04A

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T18:08:30.795Z  

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