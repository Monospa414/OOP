import time
import unittest
from ПищущаяПринадлежность import *

class TestЗаказ(unittest.TestCase):
    
    def setUp(self):
        self.заказ = Заказ()
        self.принадлежность1 = Ручка("шариковое", "пластик", "стандартный", 1)
        self.принадлежность2 = Карандаш("стержень", "дерево", "острый", 1)
        
    def test_добавить(self):
        self.assertEqual(self.заказ.заказанные_принадлежности, [])
        self.заказ.добавить(self.принадлежность1)
        self.assertEqual(self.заказ.заказанные_принадлежности, [self.принадлежность1])
        self.заказ.добавить(self.принадлежность2)
        self.assertEqual(self.заказ.заказанные_принадлежности, [self.принадлежность1, self.принадлежность2])
        
    def test_сумма(self):
        self.assertEqual(self.заказ.сумма(), 0)
        self.заказ.добавить(self.принадлежность1)
        self.assertEqual(self.заказ.сумма(), 70.00)
        self.заказ.добавить(self.принадлежность2)
        self.assertEqual(self.заказ.сумма(), 120.00)
        
    def test_выполнить(self):
        expected_output = "1. Ручка\nФормируем заказ\nУпаковываем в фирменную упаковку\nГотово\n" 
                          "2. Карандаш\nФормируем заказ\nУпаковываем в фирменную упаковку\nГотово\n" 
                          "Заказ №1 готов! Спасибо за покупку!\n"
        with redirect_stdout(io.StringIO()) as f:
            self.заказ.выполнить()
            self.assertEqual(f.getvalue(), expected_output)
            
            
if __name__ == '__main__':
    unittest.main()
