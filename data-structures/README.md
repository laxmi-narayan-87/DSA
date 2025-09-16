# Data Structures

This directory contains implementations and explanations of fundamental data structures used in computer science and software development.

## Overview

Data structures are ways of organizing and storing data so that it can be accessed and modified efficiently. Different data structures are suitable for different kinds of applications, and some are highly specialized for specific tasks.

## Categories

### Linear Data Structures
Data structures where elements are arranged in a sequential order.

- **[Arrays](./arrays/)** - Collection of elements stored at contiguous memory locations
- **[Linked Lists](./linked-lists/)** - Linear collection of elements where each element points to the next
- **[Stacks](./stacks/)** - Last In First Out (LIFO) data structure
- **[Queues](./queues/)** - First In First Out (FIFO) data structure

### Non-Linear Data Structures
Data structures where elements are not arranged in sequential order.

- **[Trees](./trees/)** - Hierarchical data structure with root and child nodes
- **[Graphs](./graphs/)** - Collection of vertices connected by edges
- **[Heaps](./heaps/)** - Complete binary tree with heap property
- **[Hash Tables](./hash-tables/)** - Data structure that maps keys to values

## Learning Path

1. **Start with Arrays**: Foundation for understanding memory and indexing
2. **Move to Linked Lists**: Introduction to pointers and dynamic memory
3. **Learn Stacks and Queues**: Essential for algorithm implementations
4. **Explore Trees**: Understand hierarchical relationships
5. **Study Graphs**: Complex relationships and connections
6. **Master Advanced Structures**: Heaps, hash tables, and specialized structures

## Implementation Guidelines

Each data structure folder contains:
- `README.md` - Detailed explanation and theory
- `implementation/` - Code implementations in various languages
- `problems/` - Related practice problems
- `examples/` - Usage examples and applications

## Complexity Analysis

Understanding the time and space complexity of operations is crucial:

| Data Structure | Access | Search | Insertion | Deletion | Space |
|---------------|--------|--------|-----------|----------|-------|
| Array         | O(1)   | O(n)   | O(n)      | O(n)     | O(n)  |
| Linked List   | O(n)   | O(n)   | O(1)      | O(1)     | O(n)  |
| Stack         | O(n)   | O(n)   | O(1)      | O(1)     | O(n)  |
| Queue         | O(n)   | O(n)   | O(1)      | O(1)     | O(n)  |
| Binary Tree   | O(n)   | O(n)   | O(n)      | O(n)     | O(n)  |
| Hash Table    | N/A    | O(1)*  | O(1)*     | O(1)*    | O(n)  |

*Average case, worst case may vary

## Resources

- **Books**: "Data Structures and Algorithm Analysis" by Mark Allen Weiss
- **Online**: GeeksforGeeks Data Structures Tutorial
- **Practice**: LeetCode Data Structure problems