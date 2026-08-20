# SEATNUMBER - Rating 613

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-20T05:15:59.994Z  

```py
# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,x=map(int,input().split())
        if x%n==0:
            print("YES")
        else:
            print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/SEATNUMBER)