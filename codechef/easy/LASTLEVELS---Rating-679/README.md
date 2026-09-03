# LASTLEVELS - Rating 679

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### The Last Levels

Chef is playing a videogame, and is getting close to the end. He decides to finish the rest of the game in a single session.

There are $X$ levels remaining in the game, and each level takes Chef $Y$ minutes to complete. To protect against eye strain, Chef also decides that every time he completes $3$ levels, he will take a $Z$ minute break from playing. Note that there is no need to take this break if the game has been completed.

How much time (in minutes) will it take Chef to complete the game?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of input will contain three space-separated integers $X$, $Y$, and $Z$.
### Output Format

For each test case, output on a new line the answer — the length of Chef's gaming session.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X \leq 100$
- $5 \leq Y \leq 100$
- $5 \leq Z \leq 15$
### Sample 1:
Input
Output

```
4
2 12 10
3 12 10
7 20 8
24 45 15

```

```
24
36
156
1185
```

### Explanation:

 **Test case 1: 2 12 10** 

- X = 2 (2 levels remain)
- Y = 12 (each level takes 12 minutes)
- Z = 10 (Chef would take a 10-minute break every 3 levels, but since there are only 2 levels, no break is needed)

Since there are only 2 levels, and no break is needed (because Chef takes a break only after every 3 levels).

The total time = X × Y = 2 × 12 = 24 minutes.

 **Test case 3: 7 20 8** 

- X = 7 (7 levels remain)
- Y = 20 (each level takes 20 minutes)
- Z = 8 (Chef takes an 8-minute break after every 3 levels)

Now, let's break this down:
Chef completes the first 3 levels: 3 x 20 = 60 minutes.
After completing these 3 levels, Chef takes an 8-minute break.
Chef completes another 3 levels: 3 x 20 = 60 minutes.
After completing these 3 levels, Chef takes another 8-minute break.
Now, Chef completes the remaining 1 level: 1 x 20 = 20 minutes.

So, the total time = 60 + 8 + 60 + 8 + 20 = 156 minutes.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T13:00:42.954Z  

```py
# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x,y,z=map(int,input().split())
        m=x//3
        if (x%3==0):
            m=m-1
        total_time= (x*y)+(m*z)
        print(total_time)
```

---

[View on CodeChef](https://www.codechef.com/problems/LASTLEVELS)