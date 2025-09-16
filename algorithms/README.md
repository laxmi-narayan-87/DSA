# Algorithms

This directory contains implementations and explanations of fundamental algorithms used in computer science and software development.

## Overview

An algorithm is a finite sequence of well-defined instructions used to solve a computational problem. Understanding algorithms is essential for writing efficient code and solving complex problems.

## Categories

### Sorting Algorithms
Algorithms that arrange elements in a specific order.

- **[Sorting](./sorting/)** - Bubble, Selection, Insertion, Merge, Quick, Heap Sort

### Searching Algorithms
Algorithms that find specific elements or patterns.

- **[Searching](./searching/)** - Linear, Binary, Depth-First, Breadth-First Search

### Graph Algorithms
Algorithms that operate on graph data structures.

- **[Graph Algorithms](./graph-algorithms/)** - Shortest path, minimum spanning tree, traversals

### Dynamic Programming
Optimization technique that solves problems by breaking them into subproblems.

- **[Dynamic Programming](./dynamic-programming/)** - Memoization, tabulation, classic DP problems

### Greedy Algorithms
Algorithms that make locally optimal choices at each step.

- **[Greedy](./greedy/)** - Activity selection, fractional knapsack, Huffman coding

### Divide and Conquer
Algorithms that break problems into smaller subproblems.

- **[Divide and Conquer](./divide-and-conquer/)** - Merge sort, quick sort, binary search

## Algorithm Design Techniques

### 1. Brute Force
- Try all possible solutions
- Simple but often inefficient
- Good for small input sizes

### 2. Greedy Method
- Make locally optimal choices
- Efficient but may not give global optimum
- Works well for optimization problems

### 3. Divide and Conquer
- Break problem into smaller subproblems
- Solve subproblems recursively
- Combine solutions

### 4. Dynamic Programming
- Solve overlapping subproblems once
- Store solutions for reuse
- Bottom-up or top-down approach

### 5. Backtracking
- Systematic trial and error
- Abandon partial solutions that can't lead to complete solution
- Used in constraint satisfaction problems

## Complexity Analysis

Understanding algorithm efficiency is crucial:

### Time Complexity
- **O(1)** - Constant time
- **O(log n)** - Logarithmic time
- **O(n)** - Linear time
- **O(n log n)** - Linearithmic time
- **O(n²)** - Quadratic time
- **O(2ⁿ)** - Exponential time

### Space Complexity
- Memory used relative to input size
- Includes auxiliary space and input space
- Important for memory-constrained environments

## Common Algorithm Patterns

### Two Pointers
- Use two pointers moving toward each other
- Efficient for array problems
- Examples: Two sum, palindrome check

### Sliding Window
- Maintain a window of elements
- Move window based on conditions
- Examples: Maximum subarray, substring problems

### Fast and Slow Pointers
- Two pointers moving at different speeds
- Useful for cycle detection
- Examples: Linked list cycle, finding middle element

### Binary Search Pattern
- Eliminate half of search space each iteration
- Works on sorted data
- Examples: Search in sorted array, find peak element

## Learning Path

1. **Master Basic Sorting**: Understand comparison-based sorting
2. **Learn Searching**: Binary search and its variants
3. **Study Graph Algorithms**: BFS, DFS, shortest path
4. **Practice Dynamic Programming**: Start with simple problems
5. **Explore Advanced Topics**: Network flow, string algorithms

## Resources

- **Books**: "Introduction to Algorithms" by CLRS
- **Online**: LeetCode Algorithm Study Plan
- **Practice**: HackerRank Algorithm Domain