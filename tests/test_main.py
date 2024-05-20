import unittest
from main import Stack


class TestMain(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.assertEqual(self.stack.push(1), [1])
        self.assertEqual(self.stack.push(2), [1, 2])
        self.assertEqual(self.stack.push(3), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
