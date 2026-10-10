# LeetCode 3100: Water Bottles II 

[![LeetCode](https://img.shields.io/badge/LeetCode-3100-blue)](https://leetcode.com/problems/water-bottles-ii/)

---

## Problem

You are given:

- `numBottles`: Initial full water bottles.  
- `numExchange`: Number of empty bottles required to exchange for a **new full bottle**.

Compute the **maximum number of water bottles you can drink**, with a twist: after each exchange, the number required (`numExchange`) **increases by 1**.


---

## Example

**Input:**
```python
numBottles = 9
numExchange = 3
```
**Output:**  
```
11
```
**Explanation:**
- Drink 9 → 9 empty → exchange 3 → get 1 full, numExchange = 4  
- Drink 1 → 7 empty → exchange 4 → get 1 full, numExchange = 5  
- Drink 1 → 4 empty → cannot exchange (needs 5)  
- Total drunk = 9 + 1 + 1 = 11

---

## Solution 1: Simulation + Incremental Exchange

**Idea:** Simulate drinking and exchanging bottles while incrementing `numExchange` after each exchange.

```python
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        consumed = 0
        while numBottles >= numExchange:
            consumed += numExchange
            numBottles -= numExchange
            numBottles += 1  # new bottle from exchange
            numExchange += 1  # increase exchange requirement
        return consumed + numBottles
```

**Key Idea:** Keep a running count of bottles consumed and adjust both the number of bottles and the exchange requirement dynamically.

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

---

## Solution 2: Mathematical Approach

**Idea:** Use a mathematical formula to compute the maximum exchanges feasible instead of simulating each step.

```python
import math

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        n = numBottles
        m = numExchange
        if n <= 0:
            return 0
        if m <= 0:
            raise ValueError("numExchange must be >= 1")

        # Solve quadratic equation for max number of exchanges k
        a = 1
        b = 2*m - 3
        c = 2 - 2*n
        D = b*b - 4*a*c
        sqrtD = math.isqrt(D)
        k = (-b + sqrtD) // 2

        if k < 0:
            k = 0

        def feasible(k):
            return k*m + (k-1)*(k-2)//2 <= n

        while feasible(k + 1):
            k += 1
        while k > 0 and not feasible(k):
            k -= 1

        return n + k
```

**Key Idea:** Convert the incremental exchange simulation into a solvable quadratic problem to compute the total bottles drunk efficiently.

- **Time Complexity:** O(log n) (due to feasible adjustments)
- **Space Complexity:** O(1)

---

## Tags

#simulation #math #greedy #water-bottles
