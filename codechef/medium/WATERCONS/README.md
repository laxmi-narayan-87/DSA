# WATERCONS

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Water Intake Check - MCQ

Recently, Chef visited his doctor. The doctor advised Chef to drink  **at least**  $2000$ ml of water each day.

Chef drank $X$ ml of water today. Select the options where Chef followed the doctor's advice.

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-31T05:01:44.946Z  

```cpp
t = int(input())
for i in range(0,t):
    x,y = map(int,input().split())
    # write your code here
    if x+y>6:
        print("YES")
    else:
        print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/WATERCONS)