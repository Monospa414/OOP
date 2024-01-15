# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_10_02_02.
#
# Выполнил: Коршиков Иван
# Группа: ПИН-б-о-22-1


class ПищущаяПринадлежность:
    """Класс ПищущаяПринадлежность содержит общие атрибуты для принадлежностей.

    Дочерние классы будут их конкретизировать.
    """

    def __init__(self):
        """Конструктор класса.

        Инициализирует атрибуты принадлежности (значения по умолчанию).
        """
        self.название = "Заготовка"
        self.чернила = "шариковые"  # шариковые, гелевые, стержень
        self.корпус = "пластик"   # пластик или дерево
        self.наконечник = "стандартный"      # стандартный, игольчатый, острый
        self.количество = "1"

        self.цена = 0

    def __str__(self):
        """Вернуть информацию о пицце: название, тесто, соус, начинка.

        Формат вывода:

        Принадлежность: Ручка | Цена: 70.00 р.
        Чернила: шариковое | Корпус: пластик
        Наконечник: стандартный | Количество: 1
        """

        return f'Принадлежность: {self.название} | Цена: {self.цена:.2f} р.\n' \
               f'   Чернила: {self.чернила} | Корпус: {self.корпус}\n' \
               f'   Наконечник: {self.наконечник} | Количество: {self.количество}'

    def формирование(self):
        """Сообщить о процессе запекания пиццы.

        Формат вывода: произвольное сообщение.
        """
        print('Формируем заказ')

    def упаковать(self):
        """Сообщить о процессе упаковки.

        Формат вывода: произвольное сообщение.
        """
        print('Упаковываем в фирменную упаковку\n Готово')


class Карандаш(ПищущаяПринадлежность):
    """Класс ПиццаПепперони дополняет класс Пицца."""

    def __init__(self):
        super().__init__()

        self.название = "Карандаш"
        self.чернила = "стержень"
        self.корпус = "дерево"
        self.наконечник = "острый"
        self.количество = "1"

        self.цена = 50

class Ручка(ПищущаяПринадлежность):
    """Класс ПиццаБарбекю дополняет класс Пицца."""

    def __init__(self):
        super().__init__()

        self.название = "Ручка"
        self.чернила = "шариковая"
        self.корпус = "пластик"
        self.наконечник = "стандартный"
        self.количество = "1"

        self.цена = 70


class ГелеваяРучка(ПищущаяПринадлежность):
    """Класс ПиццаДарыМоря дополняет класс Пицца."""

    def __init__(self):
        super().__init__()

        self.название = "Гелевая ручка"
        self.чернила = "гелевая"
        self.корпус = "пластик"
        self.наконечник = "игольчатый"
        self.количество = "1"

        self.цена = 60
