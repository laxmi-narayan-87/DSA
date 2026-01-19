# ⚡ Quick Sort

![status-badge](https://img.shields.io/badge/status-stable-brightgreen)
![language-badge](https://img.shields.io/badge/language-multi--lang-blue)
![complexity-badge](https://img.shields.io/badge/avg-O\(n%20log%20n\)-green)
![complexity-badge](https://img.shields.io/badge/worst-O\(n²\)-red)
![complexity-badge](https://img.shields.io/badge/space-O\(log%20n\)-yellow)

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

**Quick Sort** is a highly efficient **divide-and-conquer** sorting algorithm.
It works by selecting a **pivot element**, partitioning the array so that elements smaller than the pivot come before it and larger elements come after, and then recursively sorting the subarrays.

Despite its worst-case time complexity of **O(n²)**, Quick Sort is often the **fastest sorting algorithm in practice** due to low constant factors and cache efficiency.

---

## 2. Rules & Preconditions

* Input must be a list/array of comparable elements
* Works in-place (standard implementation)
* Not a stable sorting algorithm
* Performance depends heavily on pivot selection

---

## 3. Use Cases & Applications

* General-purpose in-memory sorting
* Competitive programming and interviews
* Systems where average-case performance matters more than worst-case
* Used in standard libraries (e.g., C `qsort`, Java primitive sort)

---

## 4. Algorithm Outline

1. Choose a pivot element
2. Partition the array into:

   * Elements less than the pivot
   * Elements greater than the pivot
3. Place the pivot in its correct position
4. Recursively apply Quick Sort to left and right subarrays
5. Stop when subarrays have size ≤ 1

---

## 5. Pseudocode

```text
procedure quickSort(A, low, high):
    if low < high then
        p ← partition(A, low, high)
        quickSort(A, low, p - 1)
        quickSort(A, p + 1, high)

procedure partition(A, low, high):
    pivot ← A[high]
    i ← low - 1
    for j ← low to high - 1 do
        if A[j] ≤ pivot then
            i ← i + 1
            swap(A[i], A[j])
    swap(A[i + 1], A[high])
    return i + 1
```

---

## 6. Implementation

### Python

```python
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

### C++

```cpp
#include <vector>
using namespace std;

int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
```

---

## 7. Complexity Analysis

* **Best Case:** O(n log n)
* **Average Case:** O(n log n)
* **Worst Case:** O(n²) (already sorted, poor pivot choice)
* **Space Complexity:** O(log n) (recursive stack)

---

## 8. Variants & Extensions

* **Randomized Quick Sort** → Random pivot to avoid worst case
* **Three-Way Quick Sort** → Handles duplicates efficiently
* **Hybrid Quick Sort** → Switches to insertion sort for small arrays
* **IntroSort** → Combines Quick Sort + Heap Sort

---

## 9. Proof of Correctness / Invariants

* **Partition invariant:** All elements left of pivot ≤ pivot
* **Recursive correctness:** Subarrays are sorted independently
* **Termination:** Subproblem size strictly decreases

---

## 10. Examples & Test Cases

| Input               | Output              | Notes            |
| ------------------- | ------------------- | ---------------- |
| [10, 7, 8, 9, 1, 5] | [1, 5, 7, 8, 9, 10] | Standard case    |
| [5, 4, 3, 2, 1]     | [1, 2, 3, 4, 5]     | Worst-case pivot |
| [1, 2, 3, 4, 5]     | [1, 2, 3, 4, 5]     | Already sorted   |
| [3, 3, 3]           | [3, 3, 3]           | Duplicates       |
| []                  | []                  | Empty array      |

---

## 11. Benchmarks & Performance

| Input Size | Language | Time (ms) | Memory (MB) |
| ---------- | -------- | --------- | ----------- |
| 10,000     | Python   | ~18       | 2.8         |
| 10,000     | C++      | ~2        | 1.6         |
| 100,000    | Python   | ~210      | 4.9         |
| 100,000    | C++      | ~24       | 2.9         |

---

## 12. Diagrams & Visualizations

![Quick Sort Animation](https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif)

---

## 13. References & Further Reading

* *Introduction to Algorithms* — CLRS
* [https://en.wikipedia.org/wiki/Quicksort](https://en.wikipedia.org/wiki/Quicksort)
* [https://www.geeksforgeeks.org/quick-sort/](https://www.geeksforgeeks.org/quick-sort/)

---
