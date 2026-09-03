# VALENTINE - Rating 690

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T13:16:00.348Z  

```py
# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x1,y1,x2,y2=map(int,input().split())
        print(max(abs(x1-x2),abs(y1-y2)))
```

---

[View on CodeChef](https://www.codechef.com/problems/VALENTINE)