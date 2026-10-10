# EXGS - Rating 163

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Extra Guests

Chef planned a party, and expected $X$ people to be there.
However, more people than expected turned up, so that finally there were $Y$ people at the party!

Chef now has to ensure that there's enough food for everyone.

Chef has already ordered $X$ plates of food, each costing $100$ rupees.
For each extra guest at the party, Chef needs to order one plate of food — which now costs $150$ rupees.

How much must Chef spend in total to cover food for everyone at the party?

### Input Format
- The input consists of two space-separated integers $X$ and $Y$ — the number of people expected and the number of people who actually showed up.
### Output Format
- Output a single integer: the total cost of food.
### Constraints
- $1 \le X \lt Y \le 200$
### Sample 1:
Input
Output

```
5 10
```

```
1250
```

### Explanation:

Chef paid $100$ rupees each for $X = 5$ plates of food initially, for a total of $5\times 100 = 500$.
However, there were $10$ guests finally; meaning there were $5$ extra guests. Each extra guest requires a plate of food costing $150$ rupees, for a total of $5\times 150 = 750$ rupees.
Thus, the total cost is $500 + 750 = 1250$ rupees.

### Sample 2:
Input
Output

```
1 4
```

```
550
```

### Explanation:

Chef paid $100$ rupees each for $X = 1$ plates of food initially, for a total of $1\times 100 = 100$.
However, there were $4$ guests finally; meaning there were $3$ extra guests. Each extra guest requires a plate of food costing $150$ rupees, for a total of $3\times 150 = 450$ rupees.
Thus, the total cost is $100 + 450 = 550$ rupees.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-20T13:30:08.714Z  

```py
# cook your dish here
if __name__=="__main__":
    x,y=map(int,input().split())
    total=x*100+((y-x)*150)
    print(total)
```

---

[View on CodeChef](https://www.codechef.com/problems/EXGS)