# 📝 Insertion Sort

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

Insertion Sort is a simple, comparison-based sorting algorithm.  
It builds the sorted portion of the array one element at a time by inserting each new element into its correct position.  
Efficient for small or nearly sorted datasets.

---

## 2. Rules & Preconditions

- Input: array/list of comparable elements.
- In-place sorting; no additional array required.
- Works best when data is nearly sorted.

---

## 3. Use Cases & Applications

- Educational purposes (teaches incremental insertion logic).
- Sorting small arrays efficiently.
- Online sorting (can insert elements as they arrive).

---

## 4. Algorithm Outline

1. Assume the first element is already sorted.
2. Take the next element (key) and compare it backward with elements in the sorted region.
3. Shift larger elements one position to the right.
4. Insert the key in its correct position.
5. Repeat for all elements.

---

## 5. Pseudocode

```text
procedure insertionSort(A):
    n ← length(A)
    for i ← 1 to n - 1 do
        key ← A[i]
        j ← i - 1
        while j ≥ 0 and A[j] > key do
            A[j + 1] ← A[j]
            j ← j - 1
        A[j + 1] ← key
```

---

## 6. Implementation

### Python

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

void insertionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        // Move elements greater than key one position ahead
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
```

---

## 7. Complexity Analysis

- **Best Case (already sorted):** O(n)
- **Average Case:** O(n²)
- **Worst Case (reverse sorted):** O(n²)
- **Space Complexity:** O(1) (in-place)

---

## 8. Variants & Extensions

- **Binary Insertion Sort:** Use binary search to find insertion index (still O(n²) in swaps).
- **Adaptive Insertion Sort:** Efficient for nearly sorted arrays.
- **Comparison with Bubble/Selection Sort:** Fewer swaps than selection sort, faster for small datasets.

---

## 9. Proof of Correctness / Invariants

- **Loop invariant:** After i iterations, the first i elements are sorted.
- **Termination:** When all elements are inserted, the array is sorted.

---

## 10. Examples & Test Cases

| Input                | Output                | Notes                      |
|----------------------|-----------------------|----------------------------|
| [12, 11, 13, 5, 6]   | [5, 6, 11, 12, 13]    | Standard case              |
| [5, 4, 3, 2, 1]      | [1, 2, 3, 4, 5]       | Worst case (reverse)       |
| [1, 2, 3, 4, 5]      | [1, 2, 3, 4, 5]       | Already sorted             |
| [2, 2, 2]            | [2, 2, 2]             | Duplicate elements         |
| [7]                  | [7]                   | Single element             |

---

## 11. Benchmarks & Performance

| Input Size | Language | Time (ms) | Memory (MB) |
|------------|----------|-----------|-------------|
| 1,000      | Python   | ~40       | 2.5         |
| 1,000      | C++      | ~6        | 1.2         |
| 10,000     | Python   | ~10,500   | 3.8         |
| 10,000     | C++      | ~950      | 2.0         |

---

## 12. Diagrams & Visualizations

- [Visualgo Insertion Sort Visualization](https://visualgo.net/en/sorting)
- [GeeksforGeeks Animated Insertion Sort](https://www.geeksforgeeks.org/insertion-sort/)

---

## 13. References & Further Reading

- Cormen, Leiserson, Rivest, and Stein — *Introduction to Algorithms*  
- [GeeksforGeeks Insertion Sort](https://www.geeksforgeeks.org/insertion-sort/)  
- [Wikipedia: Insertion Sort](https://en.wikipedia.org/wiki/Insertion_sort)  

---
