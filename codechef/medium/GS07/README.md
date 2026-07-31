# GS07

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### How to accept multiple integers on separate lines

Let's make this a little bit more complicated.

You need to write a program which does the following

- Accepts $2$ integers as input in 1st line as the variables $A$, $B$
- Accepts $3$ integers as input in the 2nd line as the variables $C$, $D$ and $E$
- Accepts $4$ integers as input in the 3rd line as the variables $F$, $G$, $H$ and $I$
- Prints out $9$ integers as output in a single line to the console

Code the solution in the IDE and then click  **Submit**  to continue.

### Sample 1:
Input
Output

```
1 2
3 4 5
6 7 8 9
```

```
1 2 3 4 5 6 7 8 9
```

### Sample 2:
Input
Output

```
12 34
567 789 101112
13 14 15 16
```

```
12 34 567 789 101112 13 14 15 16
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-31T11:15:22.580Z  

```py
# Update the '_' in the code below

A, B = map(int, input().split())
C, D, E = map(int, input().split())
F, G, H, I = map(int,input().split())
print(A, B, C, D, E, F, G, H, I)
```

---

[View on CodeChef](https://www.codechef.com/problems/GS07)