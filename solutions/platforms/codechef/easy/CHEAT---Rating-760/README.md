# CHEAT - Rating 760

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-27T07:23:01.777Z  

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

[View on CodeChef](https://www.codechef.com/problems/CHEAT)