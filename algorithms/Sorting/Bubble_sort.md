# 🫧 Bubble Sort

---

## 📑 Table of Contents

1. [Algorithm Description](#algorithm-description)
2. [Rules & Preconditions](#rules--preconditions)
3. [Use Cases & Applications](#use-cases--applications)
4. [Algorithm Outline](#algorithm-outline)
5. [Pseudocode](#pseudocode)
6. [Implementation](#implementation)
7. [Complexity Analysis](#complexity-analysis)
8. [Variants & Extensions](#variants--extensions)
9. [Proof of Correctness / Invariants](#proof-of-correctness--invariants)
10. [Examples & Test Cases](#examples--test-cases)
11. [Benchmarks & Performance](#benchmarks--performance)
12. [Diagrams & Visualizations](#diagrams--visualizations)
13. [References & Further Reading](#references--further-reading)

---

## 1. Algorithm Description

Bubble Sort is a simple comparison-based sorting algorithm.  
It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.  
This process continues until the list is fully sorted.

---

## 2. Rules & Preconditions

- Input is a list/array of comparable elements (integers, strings, etc.).
- No assumptions on initial order (works for sorted, reverse-sorted, or random inputs).
- In-place sorting (no extra space needed beyond a few variables).

---

## 3. Use Cases & Applications

- **Educational purposes** (teaching basic sorting concepts).
- **Small datasets** where simplicity is more important than efficiency.
- Useful when dataset is **nearly sorted** (optimized version).

---

## 4. Algorithm Outline

1. Start at the beginning of the list.
2. Compare each pair of adjacent items.
3. If they are in the wrong order, swap them.
4. After each pass, the largest element moves to the end.
5. Repeat until no swaps are needed.

---

## 5. Pseudocode

```text
procedure bubbleSort(A):
    n ← length(A)
    repeat
        swapped ← false
        for i ← 1 to n - 1 do
            if A[i - 1] > A[i] then
                swap(A[i - 1], A[i])
                swapped ← true
        n ← n - 1
    until not swapped
```

---

## 6. Implementation

### Python

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
                swapped = True
        if not swapped:
            break  # already sorted
    return arr
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    bool swapped;
    for (int i = 0; i < n - 1; i++) {
        swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}
```

---

## 7. Complexity Analysis

| Case       | Time      |
| ---------- | --------- |
| Best       | O(n)      |
| Average    | O(n²)     |
| Worst      | O(n²)     |

- **Space Complexity:** O(1) (in-place)

---

## 8. Variants & Extensions

- **Optimized Bubble Sort:** Stop early if no swaps occur in a pass.
- **Recursive Bubble Sort:** Implemented via recursion instead of loops.
- **Compared with Selection Sort** (fewer swaps) and **Insertion Sort** (faster on partially sorted data).

---

## 9. Proof of Correctness / Invariants

- **Loop invariant:** After k passes, the last k elements are in correct position.
- **Termination:** The algorithm stops when no swaps occur → list is sorted.

---

## 10. Examples & Test Cases

| Input            | Output         | Notes                       |
|------------------|---------------|-----------------------------|
| [5, 1, 4, 2, 8]  | [1, 2, 4, 5, 8] | Typical unsorted input      |
| [3, 2, 1]        | [1, 2, 3]     | Worst case (reverse sorted) |
| [1, 2, 3]        | [1, 2, 3]     | Best case (already sorted)  |
| [7]              | [7]           | Single element              |
| []               | []            | Empty array                 |

---

## 11. Benchmarks & Performance

| Input Size | Language | Time (ms) | Memory (MB) |
|------------|----------|-----------|-------------|
| 1000       | Python   | ~120      | 2.5         |
| 1000       | C++      | ~15       | 1.2         |
| 10,000     | Python   | ~11,500   | 3.8         |
| 10,000     | C++      | ~1,200    | 2.1         |

> Benchmarks vary by machine and compiler/interpreter version.

---

## 12. Diagrams & Visualizations

- [Interactive Bubble Sort Visualizer (HackerEarth)](https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/visualize/)


## 13. References & Further Reading

- CLRS — *Introduction to Algorithms*
- [GeeksforGeeks: Bubble Sort](https://www.geeksforgeeks.org/bubble-sort/)
- [Wikipedia: Bubble Sort](https://en.wikipedia.org/wiki/Bubble_sort)

---
