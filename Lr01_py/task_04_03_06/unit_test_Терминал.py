Вот пример юнит-теста для класса Терминал:

import unittest
from io import StringIO
import sys
from ПищущаяПринадлежность import *
from Заказ import *


class TerminalTestCase(unittest.TestCase):
    def setUp(self):
        self.terminal = Терминал()


    def test_показать_меню(self):
        expected_output = """Офис Маг
Добро пожаловать!


Меню:
1. Принадлежность: Карандаш | Цена: 50.00 р.
   Чернила: стержень | Корпус: дерево
   Наконечник: острый | Количество: 1
2. Принадлежность: Ручка | Цена: 70.00 р.
   Чернила: шариковое | Корпус: пластик
   Наконечник: стандартный | Количество: 1
3. Принадлежность: Гелевая ручка | Цена: 60.00 р.
   Чернила: гелевые | Корпус: пластик
   Наконечник: игольчатый | Количество: 1
Для выбора укажите цифру через <ENTER>.
Для отмены заказа введите -1
Для подтверждения заказа введите 0"""
        captured_output = StringIO()
        sys.stdout = captured_output
        self.terminal.показать_меню()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)


    def test_обработать_команду_отмена(self):
        self.terminal.заказ = Заказ()
        self.terminal.обработать_команду("-1")
        self.assertIsNone(self.terminal.заказ)


    def test_обработать_команду_подтверждение(self):
        self.terminal.заказ = Заказ()
        captured_output = StringIO()
        sys.stdout = captured_output
        self.terminal.обработать_команду("0")
        sys.stdout = sys.__stdout__
        self.assertIn("Заказ подтвержен.", captured_output.getvalue())
        self.assertIsNone(self.terminal.заказ)


    def test_обработать_команду_добавление(self):
        self.terminal.обработать_команду("1")
        self.assertIsInstance(self.terminal.заказ, Заказ)
        self.assertEqual(len(self.terminal.заказ.заказанные_принадлежности), 1)


    def test_обработать_команду_неверная(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.terminal.обработать_команду("4")
        sys.stdout = sys.__stdout__
        self.assertIn("Не могу распознать команду!", captured_output.getvalue())


    def test_рассчитать_сдачу(self):
        self.terminal.заказ = Заказ()
        self.terminal.заказ.добавить(Карандаш())
        self.assertEqual(self.terminal.рассчитать_сдачу(100), 50)


    def test_рассчитать_сдачу_недостаточно(self):
        self.terminal.заказ = Заказ()
        self.terminal.заказ.добавить(Карандаш())
        with self.assertRaises(ValueError):
            self.terminal.рассчитать_сдачу(10)


    def test_принять_оплату(self):
        self.terminal.заказ = Заказ()
        self.terminal.заказ.добавить(Карандаш())
        captured_output = StringIO()
        sys.stdout = captured_output
        sys.stdin = StringIO("100")
        self.terminal.принять_оплату()
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        self.assertIn("Вы внесли 100.00 р. Сдача: 50.00 р.", captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
