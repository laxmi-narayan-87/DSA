# PYPRACMCQ6

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Alice Happiness Condition - MCQ

Alice has scored $X$ marks in her test and Bob has scored $Y$ marks in the same test.
Alice is happy if she scored at least twice the marks of Bob’s score.
Print "Yes" if she is happy.
Other wise print nothing.

 **Option 1:** 

```
if (X >= 2*Y):
    print("YES")

```

 **Option 2:** 

```
if (X > 2*Y):
    print("YES")

```

 **Option 3:** 

```
if (2*Y <= X):
    print("YES")

```

 **Option 4:** 

```
if (2*Y >= X):
    print("YES")

```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-31T04:23:59.740Z  

```cpp
x,y = map(int,input().split())
# write your code here
if y>x:
    print("YES")
else:
    print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/PYPRACMCQ6)