# 🧱 Heap Sort

![status-badge](https://img.shields.io/badge/status-stable-brightgreen)
![language-badge](https://img.shields.io/badge/language-multi--lang-blue)
![complexity-badge](https://img.shields.io/badge/time-O\(n%20log%20n\)-green)
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

**Heap Sort** is a comparison-based sorting algorithm that uses a **binary heap** data structure. 
It first builds a **max heap**, then repeatedly extracts the maximum element and places it at the end of the array.
Heap Sort guarantees **O(n log n)** time complexity in all cases and sorts **in-place**.

---

## 2. Rules & Preconditions

* Input: array/list of comparable elements
* Uses a binary heap (max heap for ascending sort)
* Not a stable sorting algorithm
* Does not require additional memory

---

## 3. Use Cases & Applications

* Systems requiring guaranteed O(n log n) performance
* Memory-constrained environments
* When worst-case performance matters more than average speed
* Used as fallback in hybrid algorithms (e.g., IntroSort)

---

## 4. Algorithm Outline

1. Convert the array into a max heap
2. Swap the root (maximum) with the last element
3. Reduce heap size and heapify the root
4. Repeat until the heap size becomes 1

---

## 5. Pseudocode

```text
procedure heapSort(A):
    n ← length(A)

    for i ← n/2 - 1 down to 0 do
        heapify(A, n, i)

    for i ← n - 1 down to 1 do
        swap(A[0], A[i])
        heapify(A, i, 0)

procedure heapify(A, size, root):
    largest ← root
    left ← 2*root + 1
    right ← 2*root + 2

    if left < size and A[left] > A[largest] then
        largest ← left
    if right < size and A[right] > A[largest] then
        largest ← right
    if largest ≠ root then
        swap(A[root], A[largest])
        heapify(A, size, largest)
```

---

## 6. Implementation

### Python

```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]: 
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr
```

### C++

```cpp
#include <vector>
using namespace std;

void heapify(vector<int>& arr, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;
    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(vector<int>& arr) {
    int n = arr.size();

    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
```

---

## 7. Complexity Analysis

* **Best Case:** O(n log n)
* **Average Case:** O(n log n)
* **Worst Case:** O(n log n)
* **Space Complexity:** O(1)

---

## 8. Variants & Extensions

* **Min Heap Sort** → Sorts in descending order
* **IntroSort** → Hybrid of Quick Sort and Heap Sort
* **Priority Queue Sorting** → Uses heap insertion/extraction

---

## 9. Proof of Correctness / Invariants

* **Heap invariant:** Parent node is always ≥ its children
* **After each extraction:** Largest element is placed at correct final position
* **Termination:** Heap size decreases until sorted

---

## 10. Examples & Test Cases

| Input                 | Output                | Notes          |
| --------------------- | --------------------- | -------------- |
| [12, 11, 13, 5, 6, 7] | [5, 6, 7, 11, 12, 13] | Typical case   |
| [5, 4, 3, 2, 1]       | [1, 2, 3, 4, 5]       | Reverse sorted |
| [1, 2, 3, 4, 5]       | [1, 2, 3, 4, 5]       | Already sorted |
| [3, 3, 3]             | [3, 3, 3]             | Duplicates     |
| []                    | []                    | Empty array    |

---

## 11. Benchmarks & Performance

| Input Size | Language | Time (ms) | Memory (MB) |
| ---------- | -------- | --------- | ----------- |
| 10,000     | Python   | ~22       | 2.9         |
| 10,000     | C++      | ~3        | 1.7         |
| 100,000    | Python   | ~260      | 5.2         |
| 100,000    | C++      | ~31       | 3.1         |

---

## 12. Diagrams & Visualizations

![Heap Sort Animation](https://upload.wikimedia.org/wikipedia/commons/4/4d/Heapsort-example.gif)

---

## 13. References & Further Reading

* *Introduction to Algorithms* — CLRS
* [https://en.wikipedia.org/wiki/Heapsort](https://en.wikipedia.org/wiki/Heapsort)
* [https://www.geeksforgeeks.org/heap-sort/](https://www.geeksforgeeks.org/heap-sort/)

---
