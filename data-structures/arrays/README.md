# Arrays

Arrays are one of the most fundamental data structures in computer science. They provide a way to store multiple elements of the same type in contiguous memory locations.

## Overview

An array is a collection of elements stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to a base value.

## Key Characteristics

- **Fixed Size**: Arrays have a predetermined size (in most languages)
- **Homogeneous Elements**: All elements are of the same data type
- **Random Access**: Elements can be accessed directly using an index
- **Contiguous Memory**: Elements are stored in adjacent memory locations

## Operations and Complexity

| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| Access    | O(1)           | Direct access using index |
| Search    | O(n)           | Linear search through elements |
| Insertion | O(n)           | May require shifting elements |
| Deletion  | O(n)           | May require shifting elements |

## Types of Arrays

### 1. Static Arrays
- Fixed size determined at compile time
- Memory allocated on the stack
- Cannot be resized during runtime

### 2. Dynamic Arrays
- Size can change during runtime
- Memory allocated on the heap
- Examples: Python lists, Java ArrayList, C++ vector

## Common Problems

1. **Two Sum**: Find two numbers that add up to a target
2. **Maximum Subarray**: Find the contiguous subarray with maximum sum
3. **Rotate Array**: Rotate elements to the right by k steps
4. **Merge Sorted Arrays**: Combine two sorted arrays
5. **Remove Duplicates**: Remove duplicate elements in-place

## Advantages

- **Fast Access**: O(1) time to access any element
- **Memory Efficient**: No extra memory needed for pointers
- **Cache Friendly**: Elements stored contiguously
- **Simple**: Easy to understand and implement

## Disadvantages

- **Fixed Size**: Static arrays cannot be resized
- **Expensive Insertion/Deletion**: May require shifting elements
- **Memory Waste**: May allocate more memory than needed

## Implementation Examples

Check the `implementation/` folder for examples in various programming languages:
- Python: `array_operations.py`
- Java: `ArrayOperations.java`
- C++: `array_operations.cpp`
- JavaScript: `array_operations.js`

## Practice Problems

See the `problems/` folder for curated practice problems ranging from easy to hard difficulty levels.

## Resources

- [GeeksforGeeks: Arrays](https://www.geeksforgeeks.org/array-data-structure/)
- [LeetCode: Array Problems](https://leetcode.com/tag/array/)
- [HackerRank: Arrays](https://www.hackerrank.com/domains/data-structures/arrays)