# 🔀 Merge Sort

![status-badge](https://img.shields.io/badge/status-stable-brightgreen)
![language-badge](https://img.shields.io/badge/language-multi--lang-blue)
![complexity-badge](https://img.shields.io/badge/time-O\(n%20log%20n\)-green)
![complexity-badge](https://img.shields.io/badge/space-O\(n\)-orange)

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

**Merge Sort** is a divide-and-conquer sorting algorithm that recursively splits an array into smaller subarrays, sorts them, and then merges the sorted subarrays to produce the final sorted output.
It guarantees **O(n log n)** time complexity in all cases and is a **stable** sorting algorithm.

---

## 2. Rules & Preconditions

* Input: array or list of comparable elements
* Requires additional memory for merging
* Not an in-place algorithm (standard implementation)
* Preserves the relative order of equal elements (stable)

---

## 3. Use Cases & Applications

* Sorting large datasets
* External sorting (disk-based sorting)
* When guaranteed performance is required
* Used internally by languages (e.g., Python's Timsort is merge-based)

---

## 4. Algorithm Outline

1. Divide the array into two halves
2. Recursively apply merge sort to both halves
3. Merge the two sorted halves into one sorted array
4. Repeat until the base case of a single element is reached

---

## 5. Pseudocode

```text
procedure mergeSort(A):
    if length(A) ≤ 1 then
        return A

    mid ← length(A) / 2
    left ← mergeSort(A[0.. mid-1])
    right ← mergeSort(A[mid..end])

    return merge(left, right)

procedure merge(left, right):
    result ← empty list
    while left and right are not empty do
        if left[0] ≤ right[0] then
            append left[0] to result
            remove left[0]
        else
            append right[0] to result
            remove right[0]
    append remaining elements
    return result
```

---

## 6. Implementation

### Python

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### C++

```cpp
#include <vector>
using namespace std;

void merge(vector<int>& arr, int l, int m, int r) {
    vector<int> left(arr.begin() + l, arr.begin() + m + 1);
    vector<int> right(arr. begin() + m + 1, arr.begin() + r + 1);

    int i = 0, j = 0, k = l;
    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j])
            arr[k++] = left[i++];
        else
            arr[k++] = right[j++];
    }

    while (i < left.size()) arr[k++] = left[i++];
    while (j < right.size()) arr[k++] = right[j++];
}

void mergeSort(vector<int>& arr, int l, int r) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);
    merge(arr, l, m, r);
}
```

---

## 7. Complexity Analysis

* **Best Case:** O(n log n)
* **Average Case:** O(n log n)
* **Worst Case:** O(n log n)
* **Space Complexity:** O(n)

---

## 8. Variants & Extensions

* **Bottom-Up Merge Sort** → Iterative version
* **In-Place Merge Sort** → Reduced space but complex
* **Timsort** → Hybrid of merge sort and insertion sort
* **External Merge Sort** → Used for huge datasets

---

## 9. Proof of Correctness / Invariants

* **Invariant:** Each recursive call sorts its subarray correctly
* **Merge step correctness:** Always selects the smallest remaining element
* **Termination:** Recursion stops at single-element arrays

---

## 10. Examples & Test Cases

| Input              | Output             | Notes          |
| ------------------ | ------------------ | -------------- |
| [38, 27, 43, 3, 9] | [3, 9, 27, 38, 43] | Typical case   |
| [5, 4, 3, 2, 1]    | [1, 2, 3, 4, 5]    | Reverse sorted |
| [1, 2, 3, 4, 5]    | [1, 2, 3, 4, 5]    | Already sorted |
| []                 | []                 | Empty array    |
| [7]                | [7]                | Single element |

---

## 11. Benchmarks & Performance

| Input Size | Language | Time (ms) | Memory (MB) |
| ---------- | -------- | --------- | ----------- |
| 10,000     | Python   | ~45       | 4.2         |
| 10,000     | C++      | ~6        | 2.5         |
| 100,000    | Python   | ~520      | 8.1         |
| 100,000    | C++      | ~65       | 4.6         |

---

## 12. Diagrams & Visualizations

![Merge Sort Animation](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

---

## 13. References & Further Reading

* *Introduction to Algorithms* — CLRS
* [https://en.wikipedia.org/wiki/Merge_sort](https://en.wikipedia.org/wiki/Merge_sort)
* [https://www.geeksforgeeks.org/merge-sort/](https://www.geeksforgeeks.org/merge-sort/)

---
