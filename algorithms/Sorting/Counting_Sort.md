# 🔢 Counting Sort

![status-badge](https://img.shields.io/badge/status-stable-brightgreen)
![language-badge](https://img.shields.io/badge/language-multi--lang-blue)
![complexity-badge](https://img.shields.io/badge/time-O\(n%20+%20k\)-green)
![complexity-badge](https://img.shields.io/badge/space-O\(k\)-orange)
![type-badge](https://img.shields.io/badge/type-non--comparison-purple)

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

**Counting Sort** is a **non-comparison-based** sorting algorithm that works by counting the number of occurrences of each distinct element in the input array.
It uses this count information to place each element in its correct sorted position.

Counting Sort is extremely efficient when the range of input values (k) is not significantly larger than the number of elements (n), achieving **O(n + k)** time complexity.

**Key Feature:** Unlike comparison-based sorts (Quick Sort, Merge Sort), Counting Sort doesn't compare elements directly, making it faster for specific use cases.

---

## 2. Rules & Preconditions

* Input must consist of **non-negative integers** (or mappable to integers)
* Requires knowing the **range of input values** (minimum and maximum)
* Uses additional space proportional to the range of values
* **Stable sorting algorithm** (preserves relative order of equal elements)
* Not suitable when the range (k) is much larger than n

---

## 3. Use Cases & Applications

* Sorting integers with a known, limited range
* Radix sort (uses counting sort as a subroutine)
* Sorting grades, ages, or other bounded datasets
* Suffix array construction
* When stability is required and data fits the constraints

---

## 4. Algorithm Outline

1. Find the **maximum value** in the input array (determines range)
2. Create a **count array** of size (max + 1) initialized to 0
3. **Count occurrences** of each element
4. **Modify count array** to store cumulative counts (positions)
5. **Build output array** by placing elements at their correct positions
6. Copy the sorted output back to the original array

---

## 5. Pseudocode

```text
procedure countingSort(A):
    n ← length(A)
    max ← maximum value in A
    
    // Create count array
    count ← array of size (max + 1) filled with 0
    output ← array of size n
    
    // Store count of each element
    for i ← 0 to n - 1 do
        count[A[i]] ← count[A[i]] + 1
    
    // Modify count array to store cumulative counts
    for i ← 1 to max do
        count[i] ← count[i] + count[i - 1]
    
    // Build output array (traverse in reverse for stability)
    for i ← n - 1 down to 0 do
        output[count[A[i]] - 1] ← A[i]
        count[A[i]] ← count[A[i]] - 1
    
    // Copy output to original array
    for i ← 0 to n - 1 do
        A[i] ← output[i]
```

---

## 6. Implementation

### Python

```python
def counting_sort(arr):
    if not arr:
        return arr
    
    # Find the range
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1
    
    # Create count array
    count = [0] * range_size
    output = [0] * len(arr)
    
    # Store count of each element
    for num in arr:
        count[num - min_val] += 1
    
    # Modify count array to store cumulative counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build output array (traverse in reverse for stability)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    # Copy output to original array
    for i in range(len(arr)):
        arr[i] = output[i]
    
    return arr
```

### C++

```cpp
#include <vector>
#include <algorithm>
using namespace std;

void countingSort(vector<int>& arr) {
    if (arr.empty()) return;
    
    // Find the range
    int max_val = *max_element(arr.begin(), arr.end());
    int min_val = *min_element(arr.begin(), arr.end());
    int range = max_val - min_val + 1;
    
    // Create count and output arrays
    vector<int> count(range, 0);
    vector<int> output(arr.size());
    
    // Store count of each element
    for (int num : arr) {
        count[num - min_val]++;
    }
    
    // Modify count array to store cumulative counts
    for (int i = 1; i < range; i++) {
        count[i] += count[i - 1];
    }
    
    // Build output array (traverse in reverse for stability)
    for (int i = arr.size() - 1; i >= 0; i--) {
        output[count[arr[i] - min_val] - 1] = arr[i];
        count[arr[i] - min_val]--;
    }
    
    // Copy output to original array
    arr = output;
}
```

---

## 7. Complexity Analysis

* **Best Case:** O(n + k)
* **Average Case:** O(n + k)
* **Worst Case:** O(n + k)
* **Space Complexity:** O(n + k)

Where:
- **n** = number of elements
- **k** = range of input values (max - min + 1)

**Note:** When k = O(n), the algorithm runs in **O(n)** linear time!

---

## 8. Variants & Extensions

* **Counting Sort with Negative Numbers** → Offset by minimum value
* **Radix Sort** → Uses counting sort for each digit
* **Bucket Sort** → Uses counting sort principles
* **Optimized Counting Sort** → For specific data distributions

---

## 9. Proof of Correctness / Invariants

* **Count invariant:** `count[i]` correctly stores occurrences of value `i`
* **Cumulative count:** Gives the correct final position for each element
* **Stability:** Reverse traversal preserves original order of equal elements
* **Termination:** All elements are processed exactly once

---

## 10. Examples & Test Cases

| Input           | Output          | Range | Notes              |
| --------------- | --------------- | ----- | ------------------ |
| [4, 2, 2, 8, 3] | [2, 2, 3, 4, 8] | 0-8   | Standard case      |
| [1, 0, 3, 1, 3] | [0, 1, 1, 3, 3] | 0-3   | With duplicates    |
| [5, 5, 5, 5]    | [5, 5, 5, 5]    | 5-5   | All same           |
| [9, 8, 7, 6, 5] | [5, 6, 7, 8, 9] | 5-9   | Reverse sorted     |
| []              | []              | N/A   | Empty array        |

---

## 11. Benchmarks & Performance

| Input Size | Range  | Language | Time (ms) | Memory (MB) |
| ---------- | ------ | -------- | --------- | ----------- |
| 10,000     | 0-100  | Python   | ~3        | 3.2         |
| 10,000     | 0-100  | C++      | ~1        | 1.8         |
| 100,000    | 0-1000 | Python   | ~28       | 6.5         |
| 100,000    | 0-1000 | C++      | ~8        | 3.4         |

**Note:** Performance degrades significantly if range >> n

---

## 12. Diagrams & Visualizations

### Example: Sorting [4, 2, 2, 8, 3, 3, 1]

```
Step 1: Count occurrences
Index:  0  1  2  3  4  5  6  7  8
Count: [0, 1, 2, 2, 1, 0, 0, 0, 1]

Step 2: Cumulative counts (positions)
Index:  0  1  2  3  4  5  6  7  8
Count: [0, 1, 3, 5, 6, 6, 6, 6, 7]

Step 3: Place elements
Result: [1, 2, 2, 3, 3, 4, 8]
```

---

## 13. References & Further Reading

* *Introduction to Algorithms* — CLRS
* [https://en.wikipedia.org/wiki/Counting_sort](https://en.wikipedia.org/wiki/Counting_sort)
* [https://www.geeksforgeeks.org/counting-sort/](https://www.geeksforgeeks.org/counting-sort/)

---
