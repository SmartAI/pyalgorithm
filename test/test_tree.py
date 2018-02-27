import unittest
import sys
import io
from algorithm.tree import BST, travel, binary_search


class TestBST(unittest.TestCase):
    def setUp(self):
        self.capture_out = io.StringIO()
        sys.stdout = self.capture_out

    def test_bst(self):
        tree = BST()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(25)
        tree.insert(20)
        tree.insert(2)
        travel(tree.root)
        self.assertEqual(self.capture_out.getvalue().strip(), '\n'.join("2 5 10 15 20 25".split()))


class TestBinarySearch(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(0, binary_search([1], 1, 0, 0))

    def test_equals_ext(self):
        self.assertEqual(2, binary_search([0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3], 1, 0, 10))

    def test_not_found(self):
        self.assertEqual(-1, binary_search([0, 1, 2, 3, 4], 5, 0, 4))

    def test_bound_end(self):
        self.assertEqual(4, binary_search([0, 1, 2, 3, 4], 4, 0, 4))

    def test_bound_low(self):
        self.assertEqual(0, binary_search([0, 1, 2, 3, 4], 0, 0, 4))

if __name__ == '__main__':
    unittest.main(buffer=True)
