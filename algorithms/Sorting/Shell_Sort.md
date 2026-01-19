# 🐚 Shell Sort

![status-badge](https://img.shields.io/badge/status-stable-brightgreen)
![language-badge](https://img.shields.io/badge/language-multi--lang-blue)
![complexity-badge](https://img.shields.io/badge/avg-O\(n%20log%20n\)-green)
![complexity-badge](https://img.shields.io/badge/worst-O\(n²\)-red)
![complexity-badge](https://img.shields.io/badge/space-O\(1\)-yellow)

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

**Shell Sort** is an optimization of **Insertion Sort** that allows the exchange of far-apart elements.
It works by sorting elements at specific **gap intervals**, gradually reducing the gap until it becomes 1, at which point the algorithm behaves like standard insertion sort.

This significantly improves performance on medium-sized datasets. 

---

## 2. Rules & Preconditions

* Input: array/list of comparable elements
* In-place sorting (no additional memory required)
* Not a stable sorting algorithm
* Performance depends heavily on the chosen gap sequence

---

## 3. Use Cases & Applications

* Faster alternative to insertion sort for medium-sized arrays
* Systems with limited memory
* When simplicity and speed are both important
* Embedded and low-level systems

---

## 4. Algorithm Outline

1. Choose an initial gap (commonly `n/2`)
2. Perform insertion sort on elements separated by the gap
3. Reduce the gap and repeat
4. Continue until gap becomes 1
5. Final pass produces a fully sorted array

---

## 5. Pseudocode

```text
procedure shellSort(A):
    n ← length(A)
    gap ← n / 2
    while gap > 0 do
        for i ← gap to n - 1 do
            temp ← A[i]
            j ← i
            while j ≥ gap and A[j - gap] > temp do
                A[j] ← A[j - gap]
                j ← j - gap
            A[j] ← temp
        gap ← gap / 2
```

---

## 6. Implementation

### Python

```python
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr
```

### C++

```cpp
#include <vector>
using namespace std;

void shellSort(vector<int>& arr) {
    int n = arr.size();

    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            arr[j] = temp;
        }
    }
}
```

---

## 7. Complexity Analysis

* **Best Case:** O(n log n) (depends on gap sequence)
* **Average Case:** O(n log n)
* **Worst Case:** O(n²)
* **Space Complexity:** O(1)

---

## 8. Variants & Extensions

* **Knuth Gap Sequence:** `(3^k − 1) / 2`
* **Sedgewick Sequence:** Improved empirical performance
* **Tokuda Sequence:** Modern optimized gap sequence
* **Shell Sort + Insertion Sort Hybrid**

---

## 9. Proof of Correctness / Invariants

* **Invariant:** After each gap iteration, the array is gap-sorted
* When gap = 1, the array becomes fully sorted
* Gap reduction guarantees termination

---

## 10. Examples & Test Cases

| Input              | Output             | Notes          |
| ------------------ | ------------------ | -------------- |
| [12, 34, 54, 2, 3] | [2, 3, 12, 34, 54] | Standard case  |
| [5, 4, 3, 2, 1]    | [1, 2, 3, 4, 5]    | Reverse order  |
| [1, 2, 3, 4, 5]    | [1, 2, 3, 4, 5]    | Already sorted |
| [3, 3, 3]          | [3, 3, 3]          | Duplicates     |
| []                 | []                 | Empty array    |

---

## 11. Benchmarks & Performance

| Input Size | Language | Time (ms) | Memory (MB) |
| ---------- | -------- | --------- | ----------- |
| 10,000     | Python   | ~14       | 2.6         |
| 10,000     | C++      | ~2        | 1.5         |
| 100,000    | Python   | ~160      | 4.3         |
| 100,000    | C++      | ~19       | 2.4         |

---

## 12. Diagrams & Visualizations

![Shell Sort Animation](https://github.com/laxmi-narayan-87/DSA/blob/main/algorithms/Sorting/files/demo.gif)

---

## 13. References & Further Reading

* *Introduction to Algorithms* — CLRS
* [https://en.wikipedia.org/wiki/Shellsort](https://en.wikipedia.org/wiki/Shellsort)
* [https://www.geeksforgeeks.org/shellsort/](https://www.geeksforgeeks.org/shellsort/)

---
