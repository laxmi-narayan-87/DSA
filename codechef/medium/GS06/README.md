# GS06

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### How to accept multiple inputs in a line

Sometimes we have to accept multiple inputs in a single line.

The way to accept multiple integers in a single line is to use the  **split**  and  **map**  function.

- split function breaks the input based on the separator - by default, it splits inputs separated by spaces in a single line into different inputs which you can assign to different variables
- map function converts each input into the defined datatype

The syntax for the same is as follows -

```
a, b, c = map(int, input().split())   # assigns integer input values to variables a, b and c

# In this code, we take input using input(), then split it using input().split().
# Once the input is split, we convert each value into a integer using map.

```

### Task

Now lets try and solve the following

- Accept 3 space separated integers given in a line into 3 variables - $A$, $B$ and $C$
- Print them out to a single line on the console

Code the solution in the IDE and then click  **Submit**  to continue.

### Sample 1:
Input
Output

```
1 2 3
```

```
1 2 3
```

### Sample 2:
Input
Output

```
1 23 456
```

```
1 23 456
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-31T11:08:43.958Z  

```py
# Replace the underscores with the correct value

A, B, C = map(int, input().split())
print(A, B, C)
```

---

[View on CodeChef](https://www.codechef.com/problems/GS06)