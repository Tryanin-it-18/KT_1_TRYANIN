class Employee:
    def __init__(self, name, position, base_salary):
        self.name = name
        self.position = position
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary * 1.15

    def display_info(self):
        salary = self.calculate_salary()
        print(f"Имя: {self.name}")
        print(f"Должность: {self.position}")
        print(f"Базовая зарплата: {self.base_salary}")
        print(f"Итоговая зарплата: {salary:.2f}")


class Manager(Employee):
    def __init__(self, name, base_salary, subordinates_count):
        super().__init__(name, "Менеджер", base_salary)
        self.subordinates_count = subordinates_count

    def calculate_salary(self):
        return self.base_salary * 1.15 * 1.30


class Developer(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, "Разработчик", 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


def main():
    print("Введите данные для обычного сотрудника:")
    name1 = input("Имя: ")
    position1 = input("Должность: ")
    salary1 = float(input("Базовая зарплата: "))

    print("\nВведите данные для менеджера:")
    name2 = input("Имя: ")
    salary2 = float(input("Базовая зарплата: "))
    subordinates = int(input("Количество подчиненных: "))

    print("\nВведите данные для разработчика:")
    name3 = input("Имя: ")
    rate = float(input("Ставка за час: "))
    hours = float(input("Отработано часов: "))

    # Создание объектов
    employees = [
        Employee(name1, position1, salary1),
        Manager(name2, salary2, subordinates),
        Developer(name3, rate, hours)
    ]

    # Вывод результатов
    print("\n" + "=" * 50)
    print("Информация о сотрудниках:")
    print("=" * 50)

    for employee in employees:
        employee.display_info()
        print()

    # Реализация вызова метода через ссылку на базовый класс
    print("Вызов calculate_salary():")
    print("=" * 50)

    for employee in employees:
        # employee - ссылка на базовый класс Employee
        salary = employee.calculate_salary()  # Полиморфный вызов
        print(f"{employee.name} ({employee.position}): {salary:.2f} руб.")


if __name__ == "__main__":
    main()

"""
Тест 1: Обычный сотрудник с зарплатой 10000
10000 * 1.15 = 11500.00

Тест 2: Менеджер с зарплатой 10000
10000 * 1.15 * 1.30 = 14950.00

Тест 3: Разработчик с ставкой 1000 и 40 часами
1000 * 40 = 40000.00

Тест 4: Сумма всех зарплат через полиморфизм
11500 + 14950 + 40000 = 66450.00
"""
