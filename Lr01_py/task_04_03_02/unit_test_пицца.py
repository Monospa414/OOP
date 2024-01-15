import unittest
from io import StringIO
from unittest.mock import patch

from pizza import Пицца, ПиццаПепперони, ПиццаБарбекю, ПиццаДарыМоря


class PizzaTests(unittest.TestCase):


    def test_pizza_str(self):
        pizza = Пицца()
        pizza.название = "Пепперони"
        pizza.цена = 350.00
        pizza.тесто = "тонкое"
        pizza.соус = "томатный"
        pizza.начинка = ['пепперони', 'сыр моцарелла']


        expected_output = '''Пицца: Пепперони | Цена: 350.00 р.
   Тесто: тонкое Соус: томатный
   Начинка: пепперони, сыр моцарелла'''


        self.assertEqual(str(pizza), expected_output)


    def test_pizza_prepare(self):
        pizza = Пицца()
        pizza.название = "Пепперони"
        pizza.тесто = "тонкое"
        pizza.соус = "томатный"
        pizza.начинка = ['пепперони', 'сыр моцарелла']


        with patch('sys.stdout', new=StringIO()) as fake_out:
            pizza.подготовить()
            output = fake_out.getvalue().strip()


        expected_output = '''Начинаю готовить пицуу Пепперони
 - замешиваю тонкое тесто...
 - добавляю соус: томатный...
 - и, конечно: пепперони, сыр моцарелла...'''


        self.assertEqual(output, expected_output)


    def test_pizza_bake(self):
        pizza = Пицца()


        with patch('sys.stdout', new=StringIO()) as fake_out:
            pizza.испечь()
            output = fake_out.getvalue().strip()


        expected_output = 'Выпекаю пиццу... Готово!'


        self.assertEqual(output, expected_output)


    def test_pizza_cut(self):
        pizza = Пицца()


        with patch('sys.stdout', new=StringIO()) as fake_out:
            pizza.нарезать()
            output = fake_out.getvalue().strip()


        expected_output = 'Нарезаю на аппетитные кусочки...'


        self.assertEqual(output, expected_output)


    def test_pizza_pack(self):
        pizza = Пицца()


        with patch('sys.stdout', new=StringIO()) as fake_out:
            pizza.упаковать()
            output = fake_out.getvalue().strip()


        expected_output = 'Упаковываю в фирменную упаковку и готово!'


        self.assertEqual(output, expected_output)


class PepperoniPizzaTests(unittest.TestCase):


    def test_pepperoni_pizza_init(self):
        pizza = ПиццаПепперони()


        self.assertEqual(pizza.название, 'Пепперони')
        self.assertEqual(pizza.цена, 550)
        self.assertEqual(pizza.тесто, 'тонкое')
        self.assertEqual(pizza.соус, 'томатный')
        self.assertEqual(pizza.начинка, [
            'томаты', 'колбаса салями', 'сыр моцарелла',
            'перец чили', 'чеснок', 'сушённый базелик',
            'оливковое масло'
        ])


class BarbecuePizzaTests(unittest.TestCase):


    def test_barbecue_pizza_init(self):
        pizza = ПиццаБарбекю()


        self.assertEqual(pizza.название, 'Барбекю')
        self.assertEqual(pizza.цена, 625)
        self.assertEqual(pizza.тесто, 'тонкое')
        self.assertEqual(pizza.соус, 'барбекю')
        self.assertEqual(pizza.начинка, [
            'томаты', 'говядина', 'сыр моцарелла',
            'баклажан', 'шампиньоны', 'лук сладкий',
            'солённый огурец'
        ])


class SeafoodPizzaTests(unittest.TestCase):


    def test_seafood_pizza_init(self):
        pizza = ПиццаДарыМоря()


        self.assertEqual(pizza.название, 'Дары моря')
        self.assertEqual(pizza.цена, 700)
        self.assertEqual(pizza.тесто, 'тонкое')
        self.assertEqual(pizza.соус, 'чесночный')
        self.assertEqual(pizza.начинка, [
            'семга', 'креветки', 'сыр моцарелла',
            'мидии', 'маслины', 'лук красный'
        ])


if __name__ == '__main__':
    unittest.main()
