import unittest
import sys
import io
from algorithm.linkedlist import LinkedList


class TestLinedList(unittest.TestCase):
    def setUp(self):
        self.cap = io.StringIO()
        sys.stdout = self.cap

    def test_reverse(self):
        llist = LinkedList()
        llist.push(1)
        llist.push(2)
        llist.push(3)
        llist.push(4)
        llist.push(5)
        llist.push(6)
        llist.reverse()
        llist.print()
        self.assertEqual(self.cap.getvalue().strip(), "1\n2\n3\n4\n5\n6")

    def test_reverse_one(self):
        llist = LinkedList()
        llist.push(1)
        llist.reverse()
        llist.print()
        self.assertEqual(self.cap.getvalue().strip(), "1")

if __name__ == '__main__':
    unittest.main()
