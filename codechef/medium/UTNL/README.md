# UTNL

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Unlock the Next Level

Chef is playing a game.

The next level unlocks when Chef has at least  **$X$**  experience points (XP). Currently, Chef has  **$Y$**  XP.

- If the next level is already unlocked, print UNLOCKED.
- Otherwise, print how many more XP Chef needs to unlock it.
### Input Format
- A single line containing two integers, $X$ and $Y$ — the XP needed to unlock the next level and Chef's current XP.
### Output Format
- Print UNLOCKED if Chef already has enough XP.
- Otherwise, print a single integer representing the additional XP required.
### Constraints
- $1 \le X, Y \le 1000$
### Sample 1:
Input
Output

```
100 75
```

```
25
```

### Explanation:

Chef needs  **$100$**  XP to unlock the next level but currently has  **$75$**  XP. So, Chef needs  **$25$**  more XP.

### Sample 2:
Input
Output

```
250 320
```

```
UNLOCKED
```

### Explanation:

Chef already has enough XP to unlock the next level.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-27T13:37:46.428Z  

```py
# cook your dish here
if __name__=="__main__":
    x,y=map(int,input().split())
    if x>=y:
        print("UNLOCKED")
    else:
        print(x-y)
```

---

[View on CodeChef](https://www.codechef.com/problems/UTNL)