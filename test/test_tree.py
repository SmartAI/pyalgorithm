import unittest
import sys
import io
from algorithm.tree import BST, pre_traver


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
        pre_traver(tree.root)
        self.assertEqual(self.capture_out.getvalue().strip(), '\n'.join("2 5 10 15 20 25".split()))


if __name__ == '__main__':
    unittest.main(buffer=True)
