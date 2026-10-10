"""
Array Operations — reusable examples for common array operations.

The functions operate on Python lists (dynamic arrays). Binary search requires
sorted input. rotate_array mutates the supplied list and rotates right.
"""


class ArrayOperations:
    """Basic array searching and in-place manipulation algorithms."""

    @staticmethod
    def linear_search(arr, target):
        """Return the first matching index, or -1. O(n) time, O(1) space."""
        for i, value in enumerate(arr):
            if value == target:
                return i
        return -1

    @staticmethod
    def binary_search(arr, target):
        """Search a sorted list; return an index or -1. O(log n) time."""
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    @staticmethod
    def find_max_element(arr):
        """Return the maximum value, or None for an empty list. O(n) time."""
        if not arr:
            return None
        maximum = arr[0]
        for value in arr[1:]:
            if value > maximum:
                maximum = value
        return maximum

    @staticmethod
    def reverse_array(arr):
        """Reverse a list in place and return the same list. O(n) time."""
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

    @staticmethod
    def _reverse_range(arr, left, right):
        """Reverse the inclusive range [left, right] in place."""
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    @staticmethod
    def rotate_array(arr, k):
        """
        Rotate a list right by k steps in place.

        O(n) time and O(1) auxiliary space. Negative k rotates left.
        """
        n = len(arr)
        if n == 0:
            return arr
        k %= n
        if k == 0:
            return arr
        ArrayOperations._reverse_range(arr, 0, n - 1)
        ArrayOperations._reverse_range(arr, 0, k - 1)
        ArrayOperations._reverse_range(arr, k, n - 1)
        return arr


if __name__ == "__main__":
    values = [1, 3, 5, 7, 9]
    print("Linear search for 7:", ArrayOperations.linear_search(values, 7))
    print("Binary search for 7:", ArrayOperations.binary_search(values, 7))
    print("Maximum:", ArrayOperations.find_max_element(values))
    print("Reversed:", ArrayOperations.reverse_array(values.copy()))
    print("Rotated right by 2:", ArrayOperations.rotate_array(values.copy(), 2))
