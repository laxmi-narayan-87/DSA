"""
Array Operations - Basic implementations and examples

This module demonstrates fundamental array operations including:
- Basic array manipulations
- Searching algorithms
- Common array problems
"""

class ArrayOperations:
    """Class containing various array operation implementations."""
    
    @staticmethod
    def linear_search(arr, target):
        """
        Perform linear search to find target element.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            arr (list): Input array to search
            target: Element to find
            
        Returns:
            int: Index of target element, -1 if not found
        """
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1
    
    @staticmethod
    def binary_search(arr, target):
        """
        Perform binary search on sorted array.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Args:
            arr (list): Sorted input array
            target: Element to find
            
        Returns:
            int: Index of target element, -1 if not found
        """
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
    
    @staticmethod
    def find_max_element(arr):
        """
        Find maximum element in array.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            arr (list): Input array
            
        Returns:
            int/float: Maximum element in array
        """
        if not arr:
            return None
            
        max_element = arr[0]
        for element in arr[1:]:
            if element > max_element:
                max_element = element
                
        return max_element
    
    @staticmethod
    def reverse_array(arr):
        """
        Reverse array in-place.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            arr (list): Array to reverse
            
        Returns:
            list: Reversed array
        """
        left, right = 0, len(arr) - 1
        
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
        return arr
    
    @staticmethod
    def rotate_array(arr, k):
        """
        Rotate array to the right by k steps.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            arr (list): Array to rotate
            k (int): Number of steps to rotate
            
        Returns:
            list: Rotated array
        """
        n = len(arr)
        if n == 0:
            return arr
            
        k = k % n  # Handle cases where k > n
        
        # Reverse entire array
        ArrayOperations.reverse_array(arr)
        # Reverse first k elements
        ArrayOperations.reverse_array(arr[:k])
        # Reverse remaining elements
        ArrayOperations.reverse_array(arr[k:])
        
        return arr


# Example usage and test cases
if __name__ == "__main__":
    # Test array operations
    test_array = [1, 3, 5, 7, 9, 11, 13, 15]
    
    print("Original array:", test_array)
    
    # Linear search
    index = ArrayOperations.linear_search(test_array, 7)
    print(f"Linear search for 7: index {index}")
    
    # Binary search
    index = ArrayOperations.binary_search(test_array, 7)
    print(f"Binary search for 7: index {index}")
    
    # Find maximum
    max_element = ArrayOperations.find_max_element(test_array)
    print(f"Maximum element: {max_element}")
    
    # Test with a copy for rotation
    rotation_array = test_array.copy()
    ArrayOperations.rotate_array(rotation_array, 3)
    print(f"Array rotated by 3: {rotation_array}")
    
    # Test reverse
    reverse_array = [1, 2, 3, 4, 5]
    ArrayOperations.reverse_array(reverse_array)
    print(f"Reversed [1,2,3,4,5]: {reverse_array}")