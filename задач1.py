class Quadrilateral:

    def __init__(self, side1, side2, side3, side4):

        # Проверка валидности входных данных
        if not all(isinstance(side, (int, float)) for side in [side1, side2, side3, side4]):
            raise ValueError("Все стороны должны быть числами")

        if not all(side > 0 for side in [side1, side2, side3, side4]):
            raise ValueError("Все стороны должны быть положительными числами")

        # Проверка существования четырехугольника (неравенство четырехугольника)
        if (side1 >= side2 + side3 + side4 or
                side2 >= side1 + side3 + side4 or
                side3 >= side1 + side2 + side4 or
                side4 >= side1 + side2 + side3):
            raise ValueError("Четырехугольник с такими сторонами не существует")

        # Сохраняем длины сторон
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    def perimeter(self):
        """Метод для вычисления периметра четырехугольника"""
        return self.side1 + self.side2 + self.side3 + self.side4


class Rectangle(Quadrilateral):
    """наследуется от Quadrilateral"""

    def __init__(self, length, width):
        """
        Конструктор прямоугольника
        Принимает 2 числа - длину и ширину
        """
        # Проверка валидности входных данных
        if not all(isinstance(side, (int, float)) for side in [length, width]):
            raise ValueError("Длина и ширина должны быть числами")

        if not all(side > 0 for side in [length, width]):
            raise ValueError("Длина и ширина должны быть положительными числами")

        # Вызываем конструктор базового класса
        # В прямоугольнике противоположные стороны равны
        super().__init__(length, width, length, width)

        # Дополнительные атрибуты для прямоугольника
        self.length = length
        self.width = width


class Square(Rectangle):
    """(наследуется от Rectangle)"""

    def __init__(self, side):
        """
        Конструктор квадрата
        Принимает 1 число - длину стороны
        """
        # Проверка валидности входных данных
        if not isinstance(side, (int, float)):
            raise ValueError("Сторона должна быть числом")

        if side <= 0:
            raise ValueError("Сторона должна быть положительным числом")

        # Вызываем конструктор базового класса
        # В квадрате все стороны равны, поэтому передаем side дважды
        super().__init__(side, side)

        # Дополнительный атрибут для квадрата
        self.side = side


# Демонстрация работы с вводом с клавиатуры
if __name__ == "__main__":
    print("=== Создание фигур с вводом данных с клавиатуры ===")

    # Создание четырехугольника (4 числа)
    try:
        print("\n--- Создание четырехугольника (введите 4 стороны) ---")
        side1_input = float(input("Введите первую сторону четырехугольника: "))
        side2_input = float(input("Введите вторую сторону четырехугольника: "))
        side3_input = float(input("Введите третью сторону четырехугольника: "))
        side4_input = float(input("Введите четвертую сторону четырехугольника: "))
        user_quad = Quadrilateral(side1_input, side2_input, side3_input, side4_input)
        print(f"✓ Четырехугольник создан! Периметр: {user_quad.perimeter()}")
    except ValueError as e:
        print(f"✗ Ошибка: {e}")

    # Создание прямоугольника (2 числа)
    try:
        print("\n--- Создание прямоугольника (введите 2 стороны) ---")
        length_input = float(input("Введите длину прямоугольника: "))
        width_input = float(input("Введите ширину прямоугольника: "))
        user_rectangle = Rectangle(length_input, width_input)
        print(f"✓ Прямоугольник создан! Периметр: {user_rectangle.perimeter()}")
    except ValueError as e:
        print(f"✗ Ошибка: {e}")

    # Создание квадрата (1 число)
    try:
        print("\n--- Создание квадрата (введите 1 сторону) ---")
        side_input = float(input("Введите длину стороны квадрата: "))
        user_square = Square(side_input)
        print(f"✓ Квадрат создан! Периметр: {user_square.perimeter()}")
    except ValueError as e:
        print(f"✗ Ошибка: {e}")

# ТЕСТЫ

"""
=== Тестирование класса Quadrilateral ===

Тест 1: Создание четырехугольника с корректными данными
quad = Quadrilateral(2, 3, 4, 5)
ожидается: периметр = 14

Тест 2: Проверка на отрицательные числа
quad_bad = Quadrilateral(2, -3, 4, 5)
ожидается: ValueError с сообщением "Все стороны должны быть положительными числами"

Тест 3: Проверка на нечисловые значения
quad_bad = Quadrilateral(2, "3", 4, 5)
ожидается: ValueError с сообщением "Все стороны должны быть числами"

Тест 4: Проверка на нулевые значения
quad_bad = Quadrilateral(2, 0, 4, 5)
ожидается: ValueError с сообщением "Все стороны должны быть положительными числами"

Тест 5: Проверка существования четырехугольника (невозможный случай)
quad_bad = Quadrilateral(10, 1, 1, 1)
ожидается: ValueError с сообщением "Четырехугольник с такими сторонами не существует"

Тест 6: Проверка граничного случая
quad_bad = Quadrilateral(8, 1, 1, 1)
ожидается: ValueError с сообщением "Четырехугольник с такими сторонами не существует"

=== Тестирование класса Rectangle ===

Тест 7: Создание прямоугольника с корректными данными
rect = Rectangle(4, 6)
ожидается: периметр = 20

Тест 8: Проверка периметра прямоугольника
rect_test = Rectangle(3, 5)
ожидается: периметр = 16 (2*(3+5))

Тест 9: Проверка на отрицательные числа в прямоугольнике
rect_bad = Rectangle(-4, 6)
ожидается: ValueError с сообщением "Длина и ширина должны быть положительными числами"

Тест 10: Проверка на нечисловые значения в прямоугольнике
rect_bad = Rectangle(4, "6")
ожидается: ValueError с сообщением "Длина и ширина должны быть числами"

=== Тестирование класса Square ===

Тест 11: Создание квадрата с корректными данными
square = Square(5)
ожидается: периметр = 20

Тест 12: Проверка периметра квадрата
square_test = Square(4)
ожидается: периметр = 16 (4*4)

Тест 13: Проверка на отрицательные числа в квадрате
square_bad = Square(-5)
ожидается: ValueError с сообщением "Сторона должна быть положительным числом"

Тест 14: Проверка на нечисловые значения в квадрате
square_bad = Square("5")
ожидается: ValueError с сообщением "Сторона должна быть числом"

Тест 15: Проверка наследования
square = Square(5)
ожидается: 
isinstance(square, Rectangle) = True
isinstance(square, Quadrilateral) = True
isinstance(Rectangle(1,2), Quadrilateral) = True

Тест 16: Проверка с дробными числами
square_float = Square(3.5)
ожидается: периметр = 14.0

Тест 17: Проверка атрибутов
square = Square(5)
ожидается: square.side = 5, square.length = 5, square.width = 5
"""