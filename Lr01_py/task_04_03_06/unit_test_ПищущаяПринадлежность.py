import unittest
from unittest.mock import patch
from Заказ import Заказ

class TestЗаказ(unittest.TestCase):
    def setUp(self):
        self.order = Заказ()

    def test_добавить(self):
        item = "Принадлежность"
        self.order.добавить(item)
        self.assertEqual(len(self.order.заказанные_принадлежности), 1)
        self.assertEqual(self.order.заказанные_принадлежности[0], item)

    def test_сумма(self):
        items = ["Принадлежность 1", "Принадлежность 2"]
        self.order.заказанные_принадлежности = items
        self.assertEqual(self.order.сумма(), len(items))

    @patch('builtins.print')
    def test_выполнить(self, mock_print):
        items = ["Принадлежность 1", "Принадлежность 2"]
        self.order.заказанные_принадлежности = items
        self.order.выполнить()

        calls = [call(f'{i + 1}. {item}') for i, item in enumerate(items)]
        calls.append(call(f'Заказ №{self.order.номер_заказа} готов! Спасибо за покупку!'))
        mock_print.assert_has_calls(calls)

if __name__ == '__main__':
    unittest.main()
