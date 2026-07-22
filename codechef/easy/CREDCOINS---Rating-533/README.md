# CREDCOINS - Rating 533

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-22T13:11:18.202Z  

```py
# cook your dish here
def check(n,a):
    co=ce=0
    for i in range(n):
        if a[i]%2==0:
            ce+=1
        else:
            co+=1 
    if ce>co:
        return "READY FOR BATTLE"
    else:
        return "NOT READY"
if __name__=="__main__":
    t=int(input())
    x=list(map(int,input().split()))
    print(check(t,x))
```

---

[View on CodeChef](https://www.codechef.com/problems/CREDCOINS)