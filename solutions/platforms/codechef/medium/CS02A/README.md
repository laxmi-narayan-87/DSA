# CS02A

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T18:13:40.580Z  

```py
# Update the '_' below to solve the problem

t = int(input())
for i in range(t):
    n = int(input())
    
    # Condition 1
    if n%3 == 0:
        print('Divisible by 3')
    else:
        print('Not divisible by 3')
    
    #Condition 2
    if n%2 != 0:
        print('Odd')
    else:
        print('Even')
```

---

[View on CodeChef](https://www.codechef.com/problems/CS02A)