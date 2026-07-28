# MINPIZZA - Rating 541

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-28T10:42:26.969Z  

```py
# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x=int(input())
        if x>5000:
            print(x-500)
        elif  5000>=x>1000:
            print(x-100)
        elif 1000>=x>100:
            print(x-25)
        else:
            print(x)
```

---

[View on CodeChef](https://www.codechef.com/problems/MINPIZZA)