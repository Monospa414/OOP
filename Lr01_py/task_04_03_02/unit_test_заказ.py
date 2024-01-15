import unittest
from unittest.mock import patch
from io import StringIO
from пицца import Пицца, Заказ  # Импортируется классы


class TestЗаказ(unittest.TestCase):
    def setUp(self):
        # Создается экземпляр Pizza для тестирования
        self.pizza1 = Пицца("Пепперони", "тонкое", "томатный", ["пепперони", "сыр моцарелла"], 350.00)
        self.pizza2 = Пицца("Барбекю", "тонкое", "барбекю", ["бекон", "ветчина", "зелень", "сыр моцарелла"], 450.00)

    def test_добавить(self):
        order = Заказ()
        order.добавить(self.pizza1)
        order.добавить(self.pizza2)
        self.assertEqual(len(order.заказанные_пиццы), 2)

    @patch("sys.stdout", new_callable=StringIO)
    def test_выполнить(self, mock_stdout):
        order = Заказ()
        order.добавить(self.pizza1)
        order.добавить(self.pizza2)

        expected_output = (
            "1. Пепперони\n"
            "1. Пицца: Пепперони | Цена: 350.00 р.\n"
            "Тесто: тонкое Соус: томатный\n"
            "Начинка: пепперони, сыр моцарелла\n"
            "2. Пицца: Барбекю | Цена: 450.00 р.\n"
            "Тесто: тонкое Соус: барбекю\n"
            "Начинка: бекон, ветчина, зелень, сыр моцарелла\n"
            "Заказ №1 готов! Приятного аппетита!\n"
        )

        with patch("time.sleep", side_effect=lambda x: None):  # Mock time.sleep to avoid actual sleep
            order.выполнить()

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_сумма(self):
        order = Заказ()
        order.добавить(self.pizza1)
        order.добавить(self.pizza2)
        self.assertEqual(order.сумма(), 800.00)


if __name__ == '__main__':
    unittest.main()
