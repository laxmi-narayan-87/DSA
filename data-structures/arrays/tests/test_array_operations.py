import sys
import unittest
from pathlib import Path

IMPLEMENTATION_DIR = Path(__file__).resolve().parents[1] / "implementation"
sys.path.insert(0, str(IMPLEMENTATION_DIR))
from array_operations import ArrayOperations


class TestArrayOperations(unittest.TestCase):
    def test_linear_search(self):
        self.assertEqual(ArrayOperations.linear_search([4, 8, 4], 4), 0)
        self.assertEqual(ArrayOperations.linear_search([4, 8], 3), -1)
        self.assertEqual(ArrayOperations.linear_search([], 3), -1)

    def test_binary_search(self):
        self.assertEqual(ArrayOperations.binary_search([1, 3, 5, 7], 5), 2)
        self.assertEqual(ArrayOperations.binary_search([1, 3, 5, 7], 2), -1)
        self.assertEqual(ArrayOperations.binary_search([], 2), -1)

    def test_find_max_element(self):
        self.assertEqual(ArrayOperations.find_max_element([-5, -2, -9]), -2)
        self.assertIsNone(ArrayOperations.find_max_element([]))

    def test_reverse_mutates_input(self):
        values = [1, 2, 3, 4]
        result = ArrayOperations.reverse_array(values)
        self.assertIs(result, values)
        self.assertEqual(values, [4, 3, 2, 1])
        self.assertEqual(ArrayOperations.reverse_array([]), [])

    def test_rotate_right(self):
        values = [1, 2, 3, 4, 5]
        result = ArrayOperations.rotate_array(values, 2)
        self.assertIs(result, values)
        self.assertEqual(values, [4, 5, 1, 2, 3])

    def test_rotate_edge_cases(self):
        self.assertEqual(ArrayOperations.rotate_array([], 4), [])
        self.assertEqual(ArrayOperations.rotate_array([7], 99), [7])
        self.assertEqual(ArrayOperations.rotate_array([1, 2, 3], 0), [1, 2, 3])
        self.assertEqual(ArrayOperations.rotate_array([1, 2, 3], 3), [1, 2, 3])
        self.assertEqual(ArrayOperations.rotate_array([1, 2, 3], -1), [2, 3, 1])
        self.assertEqual(ArrayOperations.rotate_array([1, 2], 5), [2, 1])


if __name__ == "__main__":
    unittest.main()
