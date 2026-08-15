# CS03A - Rating 276

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Practice problem - Tax in Chefland

In Chefland, a tax of rupees $10$ is deducted if the total income is  **strictly greater**  than rupees $100$.
Given that total income is $X$ rupees, find out how much money does the Chef take home.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains a single integer $X$ — Chef's total income.
### Output Format

For each test case, output on a new line, the amount of money that Chef takes home after deducting tax.

### Sample 1:
Input
Output

```
2
101
100

```

```
91
100
```

### Explanation:

 **Test case $1$:**  Your total income is $101$ rupees which is greater than $100$ rupees. Thus, a tax of $10$ rupees would be deducted and you get $101-10 = 91$ rupees.

 **Test case $2$:**  Your total income is $100$ rupees which is equal to $100$ rupees. Thus, no tax would be deducted and you get $100$ rupees.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T18:15:36.576Z  

```py
# Update the code below to solve the problem

t = int(input())           
for i in range(t):
    X = int(input())
    if X>100:
        print(X-10)
    else:
        print(X)
```

---

[View on CodeChef](https://www.codechef.com/problems/CS03A)