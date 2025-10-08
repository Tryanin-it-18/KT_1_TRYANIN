import pickle


class Node:
    """Узел односвязного списка для стека"""

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """Стек на основе односвязного списка"""

    def __init__(self):
        self.top = None

    def push(self, value):
        """Добавление элемента в стек"""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Удаление и возврат верхнего элемента"""
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        """Просмотр верхнего элемента без удаления"""
        if self.top is None:
            return None
        return self.top.value

    def is_empty(self):
        """Проверка пустоты стека"""
        return self.top is None


class StackIterator:
    """Итератор для просмотра стека снизу вверх"""

    def __init__(self, stack):
        self.stack = stack
        self.current = self._get_bottom()

    def _get_bottom(self):
        """Находит дно стека"""
        if self.stack.top is None:
            return None

        # Создаем временный стек для обращения порядка
        temp_stack = Stack()
        current = self.stack.top
        while current:
            temp_stack.push(current.value)
            current = current.next

        # Теперь temp_stack содержит элементы в обратном порядке
        return temp_stack.top

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value


def main():
    # Ввод последовательности
    sequence = input("Введите последовательность (цифры и + через пробел): ").split()

    # Создание стека и заполнение его элементами
    stack = Stack()
    for item in sequence:
        stack.push(item)

    # Извлечение чисел до первого знака "+"
    extracted_numbers = []
    current = stack.pop()

    while current is not None and current != '+':
        if current.isdigit():  # Проверяем, что это цифра
            extracted_numbers.append(int(current))
        current = stack.pop()

    # Если мы извлекли '+', возвращаем его обратно в стек
    if current == '+':
        stack.push(current)

    # Вычисление суммы извлеченных чисел
    sum_extracted = sum(extracted_numbers)

    # Вывод результатов
    print(f"\nИзвлеченные числа: {extracted_numbers}")
    print(f"Сумма извлеченных чисел: {sum_extracted}")

    # Получение текущей вершины стека
    top_value = stack.peek()
    top_pointer = id(stack.top) if stack.top else None

    print(f"Текущая вершина стека: {top_value}")
    print(f"Указатель на вершину стека: {top_pointer}")

    # Сохранение в двоичный файл
    data_to_save = {
        'extracted_numbers': extracted_numbers,
        'sum_extracted': sum_extracted,
        'top_value': top_value,
        'top_pointer': top_pointer
    }

    with open('rez.dat', 'wb') as file:
        pickle.dump(data_to_save, file)
    print("Данные сохранены в файл rez.dat")

    # Демонстрация работы итератора
    print("\nПросмотр стека снизу вверх:")
    iterator = StackIterator(stack)
    for item in iterator:
        print(item, end=" ")
    print()


if __name__ == "__main__":
    main()

# ТЕСТЫ
"""
Тест 1
Вход: "1 2 3 2 + 6 + + 4"
Ожидается:
  Извлеченные числа: [4]
  Сумма: 4
  Вершина стека: +
  Просмотр снизу: 1 2 3 2 + 6 + +

Тест 2
Вход: "5 3 1 + 2 4"
Ожидается:
  Извлеченные числа: [4, 2]
  Сумма: 6
  Вершина стека: +
  Просмотр снизу: 5 3 1 +

Тест 3
Вход: "1 2 3 4 5"
Ожидается:
  Извлеченные числа: [5, 4, 3, 2, 1]
  Сумма: 15
  Вершина стека: None
  Просмотр снизу: (пусто)

Тест 4
Вход: "+ + + +"
Ожидается:
  Извлеченные числа: []
  Сумма: 0
  Вершина стека: +
  Просмотр снизу: + + +
"""