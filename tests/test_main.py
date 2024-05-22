import unittest
from main import Stack, check_balance


class TestMain(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.assertEqual(self.stack.push(1), [1])
        self.assertEqual(self.stack.push(2), [1, 2])
        self.assertEqual(self.stack.push(3), [1, 2, 3])

    def test_check_balance(self):
        for i, string in enumerate([
            '(((([{}]))))',
            '[([])((([[[]]])))]{()}',
            '{{[()]}}'
        ]):
            with self.subTest(i=i):
                actual = check_balance(string)
                self.assertEqual(actual, True)

    def test_check_balance_fail(self):
        for i, string in enumerate([
            '}{}',
            '{{[(])]}}'
            '[[{())}]'
        ]):
            with self.subTest(i=i):
                actual = check_balance(string)
                self.assertEqual(actual, False)


if __name__ == '__main__':
    unittest.main()
