# ACTEMP - Rating 580

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T04:31:26.002Z  

```py
# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        d=list(map(int,input().split()))
        count=0
        for i in range(n):
            if d[i]>=1000:
                count+=1
        print(count)
```

---

[View on CodeChef](https://www.codechef.com/problems/ACTEMP)