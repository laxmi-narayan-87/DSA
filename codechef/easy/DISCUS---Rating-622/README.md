# DISCUS - Rating 622

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Discus Throw

In discus throw, a player is given $3$ throws and the throw with the  **longest distance**  is regarded as their final score.

You are given the distances for all $3$ throws of a player. Determine the final score of the player.

### Input Format
- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, three integers $A, B,$ and $C$ denoting the distances in each throw.
### Output Format

For each test case, output the final score of the player.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq A,B,C \leq 100$
### Sample 1:
Input
Output

```
3
10 15 8
32 32 32
82 45 54

```

```
15
32
82

```

### Explanation:

 **Test Case $1$:**  The longest distance is achieved in the second throw, which is equal to $15$ units. Thus, the answer is $15$.

 **Test Case $2$:**  In all throws, the distance is $32$ units. Thus, the final score is $32$.

 **Test Case $3$:**  The longest distance is achieved in the first throw which is equal to $82$ units. Thus, the answer is $82$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-20T06:40:04.145Z  

```py
# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        a,b,c=map(int,input().split())
        print(max(a,b,c))
```

---

[View on CodeChef](https://www.codechef.com/problems/DISCUS)