# POPCORN7 - Rating 99

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Popcorn Buying

Chef has gone to see a movie. Chef has $X$ ($X \ge 100$) rupees with him.

The movie ticket itself costs $100$, and Chef must buy one movie ticket to be able to see the movie.

With the money leftover, Chef will buy as many popcorn buckets as possible. A single popcorn bucket costs $50$ rupees. How many popcorn buckets will Chef be able to buy?

### Input Format
- The first and only line of input contains a single integer $X$.
### Output Format

Output the number of popcorn buckets Chef can buy after paying for the movie ticket.

### Constraints
- $100 \le X \le 250$
### Sample 1:
Input
Output

```
145

```

```
0

```

### Explanation:

Chef will have only $45$ rupees left after buying the movie ticket, which is not enough for a popcorn bucket.

### Sample 2:
Input
Output

```
225

```

```
2

```

### Explanation:

Chef will have $125$ rupees, and he can buy $2$ popcorn buckets for $100$ rupees.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-20T13:24:44.104Z  

```py
# cook your dish here
if __name__=="__main__":
    t=int(input())
    left=t-100
    pop=left//50
    print(int(pop))
```

---

[View on CodeChef](https://www.codechef.com/problems/POPCORN7)