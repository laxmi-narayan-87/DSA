# GS08

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### How to accept string inputs

Lets try the same exercise with strings.

Remember that the  **input()**  function takes the parameters as strings and then we convert to integer as needed. We use map function convert input to integers. Here we just want to take input as string, so no need of map.

```
a, b = input().split()
print(a, b)

```

### Task

You need to write a program which does the following

- Accepts $2$ space separated alphanumeric strings as input in $1^{st}$ line as the variables $A$, $B$
- Accepts $3$ space separated alphanumeric strings as input in $2^{nd}$ line as the variables $C$, $D$, $E$
- Accepts $4$ space separated alphanumeric strings as input in $3^{rd}$ line as the variables $F$, $G$, $H$, $I$
- Prints out $9$ space separated strings as output in a single line to the console
### Sample 1:
Input
Output

```
abc cde
fg hi jk
l m n o
```

```
abc cde fg hi jk l m n o
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T18:19:35.678Z  

```py
# Update the '_' in the code below

A, B = input().split()
C, D, E = input().split()
F, G, H, I = input().split()
print(A, B, C, D, E, F, G, H, I)
```

---

[View on CodeChef](https://www.codechef.com/problems/GS08)