# 1339. Maximum Product of Splitted Binary Tree

## Problem Statement

Given the `root` of a binary tree, split the binary tree into **two subtrees** by removing **exactly one edge** such that the **product of the sums** of the two resulting subtrees is **maximized**. 

Return the **maximum product** of the sums of the two subtrees.

Since the answer may be very large, return it **modulo `10^9 + 7`**.

> **Note:**  
> You must maximize the product **before** taking the modulo, not after.

**Problem Link:** [LeetCode 1339 - Maximum Product of Splitted Binary Tree](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/)

---

## Examples

### Example 1
```
Input:  root = [1,2,3,4,5,6]
Output:  110
```
**Explanation:**  
Removing one edge splits the tree into two subtrees with sums `11` and `10`.  
Their product is `11 × 10 = 110`.

---

### Example 2
```
Input:  root = [1,null,2,3,4,null,null,5,6]
Output: 90
```
**Explanation:**  
Removing one edge splits the tree into two subtrees with sums `15` and `6`.  
Their product is `15 × 6 = 90`.

---

## Constraints

- The number of nodes in the tree is in the range `[2, 5 × 10^4]`
- `1 <= Node.val <= 10^4`
