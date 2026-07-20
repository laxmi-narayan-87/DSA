# SALARY1

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Monthly Earnings

Chef earns a fixed base salary of $S$ rupees every month.
In addition, he receives a bonus of $B$ rupees for every five-star rating he gets from customers.
This month, Chef received $R$ five-star ratings.
Find Chef's total  **earnings**  for the month.

### Input Format

A single line containing three space-separated integers:

- $S$ — Chef's base salary.
- $B$ — Bonus received for each five-star rating.
- $R$ — Number of five-star ratings received.
### Output Format

Print a single integer — Chef's total earnings.

### Constraints
- $1 \le S, B, R \le 10^4$
### Sample 1:
Input
Output

```
10000 250 12
```

```
13000
```

### Explanation:

Chef earns a base salary of $10000$ rupees and receives a bonus of $250 \times 12 = 3000$ rupees.
Therefore, his total earnings are $10000 + 3000 = 13000$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-20T12:41:03.023Z  

```py
# cook your dish here

def earning(s,b,r):
    total = s+b*r
    return total

if __name__=="__main1__":
    s,b,r= map(int,input().split())
    print(earning(s,b,r))
    
if __name__=="__main__":
    s,b,r=map(int,input().split())
    total=s+b*r
    print(total)
```

---

[View on CodeChef](https://www.codechef.com/problems/SALARY1)