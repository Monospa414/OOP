class Stack:
    def __init__(self):
        """
        Инициализация пустого стека.
        """
        self.items = []

    def is_empty(self):
        """
        Проверяет, пуст ли стек.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Добавляет элемент на вершину стека.
        :param item: Элемент, который нужно добавить.
        """
        self.items.append(item)

    def pop(self):
        """
        Удаляет и возвращает элемент с вершины стека.
        :return: Элемент с вершины стека.
        :raises IndexError: Если стек пуст.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст, невозможно выполнить операцию 'pop'.")

    def peek(self):
        """
        Возвращает элемент с вершины стека без его удаления.
        :return: Элемент с вершины стека.
        :raises IndexError: Если стек пуст.
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст, невозможно выполнить операцию 'peek'.")

    def size(self):
        """
        Возвращает количество элементов в стеке.
        """
        return len(self.items)

    def __str__(self):
        """
        Возвращает строковое представление стека в удобном для человека виде.
        """
        return str(self.items)

# Пример использования класса Stack:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Стек:", stack)  # Вывод: Стек: [1, 2, 3]

top_element = stack.pop()
print("Извлеченный элемент:", top_element)  # Вывод: Извлеченный элемент: 3

print("Размер стека:", stack.size())  # Вывод: Размер стека: 2
