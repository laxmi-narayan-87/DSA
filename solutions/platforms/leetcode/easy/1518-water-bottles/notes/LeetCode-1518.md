# LeetCode 1518: Water Bottles

[![LeetCode](https://img.shields.io/badge/LeetCode-1518-orange)](https://leetcode.com/problems/water-bottles/)

---

## Problem

You have `numBottles` full water bottles. You can exchange `numExchange` empty bottles for one full bottle.  

Return the **maximum number of water bottles you can drink**.

---

## Examples

**Input:** numBottles = 9, numExchange = 3  
**Output:** 13  
**Explanation:**  
Drink 9 bottles → 9 empty → 3 new full bottles → drink 3 → 3 empty → 1 new full → drink 1  
Total = 9 + 3 + 1 = 13

**Input:** numBottles = 15, numExchange = 4  
**Output:** 19

---

## Approaches

### Approach 1: Simulation (Loop)

**Idea:** Track full and empty bottles at each step. Drink full, exchange empties, repeat.

```python
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        consumed = numBottles
        empty = numBottles
        while empty >= numExchange:
            new_full = empty // numExchange
            consumed += new_full
            empty = empty % numExchange + new_full
        return consumed
```
*Time Complexity: O(log numBottles)*  
*Space Complexity: O(1)*

---

### Approach 2: Mathematical Formula

**Idea:** Each exchange reduces the number of empty bottles, forming a geometric pattern.  
Final number of bottles: `numBottles + floor((numBottles-1)/(numExchange-1))`

```python
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)
```
*Time Complexity: O(1)*  
*Space Complexity: O(1)*

---

### Approach 3: Recursive Simulation

**Idea:** Recursively consume bottles and exchange empties.

```python
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numBottles < numExchange:
            return numBottles
        new_full = numBottles // numExchange
        remaining = numBottles % numExchange
        return new_full + self.numWaterBottles(new_full + remaining, numExchange)
```
*Time Complexity: O(log numBottles)*  
*Space Complexity: O(log numBottles) due to recursion stack*

---

## Key Insights

- **Simulation** mirrors the problem rules.
- **Mathematical formula** allows O(1) computation.
- **Recursive approach** is elegant but uses extra stack space.

---

## Tags

#math #simulation #greedy #easy
