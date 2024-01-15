import unittest

class TestStackMethods(unittest.TestCase):


    def setUp(self):
        self.stack = Stack()


    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)
        self.stack.push(1)
        self.assertEqual(self.stack.is_empty(), False)


    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)


    def test_pop(self):
        with self.assertRaises(IndexError):
            self.stack.pop()
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.size(), 1)


    def test_peek(self):
        with self.assertRaises(IndexError):
            self.stack.peek()
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.size(), 2)


    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)


if __name__ == '__main__':
    unittest.main()
