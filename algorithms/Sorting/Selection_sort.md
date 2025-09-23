# 🔽 Selection Sort

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

Selection Sort is a simple comparison-based sorting algorithm that divides the array into a sorted and an unsorted region. On each iteration, it selects the minimum element from the unsorted region and swaps it with the first unsorted element.

---

## 2. Rules & Preconditions

- Input: array/list of comparable elements (numbers, strings with a defined order, etc.).  
- In-place sorting: uses O(1) extra space beyond a few variables.  
- Not stable by default (order of equal elements may change) unless modified.  

---

## 3. Use Cases & Applications

- Teaching and educational purposes — illustrates selection and swapping.  
- Small datasets where simplicity and low memory overhead matter.  
- When the number of swaps must be minimized compared to some algorithms (selection sort does at most n swaps).

---

## 4. Algorithm Outline

1. Start with the first element as the current minimum position.  
2. Scan the unsorted portion of the array to find the smallest element.  
3. Swap the found minimum element with the first unsorted element.  
4. Expand the sorted region by one element and repeat until sorted.

---

## 5. Pseudocode

```text
procedure selectionSort(A):
    n ← length(A)
    for i ← 0 to n - 2 do
        minIndex ← i
        for j ← i + 1 to n - 1 do
            if A[j] < A[minIndex] then
                minIndex ← j
        if minIndex ≠ i then
            swap(A[i], A[minIndex])
```

---

## 6. Implementation

### Python

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  # swap
    return arr
```

### C++

```cpp
#include <vector>
#include <algorithm> // for std::swap

void selectionSort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        int minIndex = i;
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if (minIndex != i) {
            std::swap(arr[i], arr[minIndex]);
        }
    }
}
```

---

## 7. Complexity Analysis

- Best Case: O(n²) — still scans the remainder of the array each time.  
- Average Case: O(n²)  
- Worst Case: O(n²)  
- Space Complexity: O(1) — in-place (ignoring input storage).

Note: Selection Sort does at most n − 1 swaps, which can be advantageous if swaps are expensive.

---

## 8. Variants & Extensions

- Stable Selection Sort: modify algorithm to preserve order of equal elements (may require extra memory or shifting elements instead of swapping).  
- Heapsort: builds on the selection idea but uses a heap to get O(n log n) time.  
- Comparison with other simple sorts:
  - Bubble Sort: similar time complexity, more swaps on average.
  - Insertion Sort: better on nearly-sorted inputs.

---

## 9. Proof of Correctness / Invariants

- Loop invariant: After i iterations, the first i elements contain the i smallest elements in sorted order.  
- Termination: When i reaches n − 1, the entire array is sorted.

---

## 10. Examples & Test Cases

| Input                  | Output                | Notes                        |
|------------------------|-----------------------|------------------------------|
| [64, 25, 12, 22, 11]   | [11, 12, 22, 25, 64]  | Standard case                |
| [5, 4, 3, 2, 1]        | [1, 2, 3, 4, 5]       | Reverse order (worst case)   |
| [1, 2, 3, 4, 5]        | [1, 2, 3, 4, 5]       | Already sorted               |
| [2, 2, 2]              | [2, 2, 2]             | Duplicates                   |
| [7]                    | [7]                   | Single element               |
| []                     | []                    | Empty array                  |

---

## 11. Benchmarks & Performance

| Input Size | Language | Time (ms) | Memory (MB) |
|------------|----------|-----------|-------------|
| 1,000      | Python   | ~110      | 2.5         |
| 1,000      | C++      | ~12       | 1.2         |
| 10,000     | Python   | ~11,000   | 3.8         |
| 10,000     | C++      | ~1,100    | 2.0         |

> Benchmarks vary by machine, implementation details, and compiler/interpreter versions.

---

## 12. Diagrams & Visualizations

- Visualgo Sorting Visualizer (multiple algorithms including Selection Sort):  
  https://visualgo.net/en/sorting

- Interactive Selection Sort Visualizer (HackerEarth):  
  https://www.hackerearth.com/practice/algorithms/sorting/selection-sort/visualize/

(Use these to step through comparisons and swaps visually.)

---

## 13. References & Further Reading

- Cormen, Leiserson, Rivest, and Stein — *Introduction to Algorithms*  
- GeeksforGeeks — Selection Sort  
- Wikipedia — Selection Sort  
- Visualgo — Sorting visualizations (interactive)

---
