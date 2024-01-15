import unittest
from пицца import *
from заказ import *


class TestTerminalMethods(unittest.TestCase):


    def setUp(self):
        self.terminal = Терминал()


    def test_show_menu(self):
        menu = 'PizzaHub\n1. Пицца: Пепперони | Цена: 350.00 р.\n   Тесто: тонкое Соус: томатный\n   Начинка: пепперони, сыр моцарелла\n2. Пицца: Барбекю | Цена: 450.00 р.\n   Тесто: тонкое Соус: барбекю\n   Начинка: бекон, ветчина, зелень, сыр моцарелла\n3. Пицца: Дары моря | Цена: 550.00 р.\n   Тесто: пышное Соус: тар-тар\n   Начинка: кальмары, креветки, мидии, сыр моцарелла\nДля выбора укажите цифру через <ENTER>.\nДля отмены заказа введите -1\nДля подтверждения заказа введите 0\n'
        self.assertEqual(self.terminal.показать_меню(), menu)


    def test_process_command_cancel_order(self):
        self.terminal.отображать_меню = False
        self.terminal.заказ = Заказ()
        self.terminal.обработать_команду('-1')
        self.assertEqual(self.terminal.заказ, None)


    def test_process_command_confirm_order(self):
        self.terminal.отображать_меню = False
        self.terminal.заказ = Заказ()
        self.terminal.заказ.добавить(ПиццаПепперони())
        self.assertEqual(self.terminal.обработать_команду('0'), None)


    def test_process_command_add_pizza(self):
        self.terminal.отображать_меню = False
        self.terminal.обработать_команду('1')
        self.assertEqual(len(self.terminal.заказ.заказанные_пиццы), 1)
        self.assertEqual(self.terminal.заказ.заказанные_пиццы[0].название, 'Пепперони')


    def test_process_command_invalid_input(self):
        self.terminal.отображать_меню = False
        self.assertEqual(self.terminal.обработать_команду('invalid'), None)


    def test_calculate_change(self):
        self.terminal.заказ = Заказ()
        self.terminal.заказ.добавить(ПиццаПепперони())
        self.assertEqual(self.terminal.рассчитать_сдачу(400), 50)
        with self.assertRaises(ValueError):
            self.terminal.рассчитать_сдачу(300)


    def test_accept_payment(self):
        self.terminal.заказ = Заказ()
        self.terminal.заказ.добавить(ПиццаПепперони())
        with self.assertRaises(Exception):
            self.terminal.принять_оплату()


if __name__ == '__main__':
    unittest.main()
