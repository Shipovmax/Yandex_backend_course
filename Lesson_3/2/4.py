class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days
        # Защищённый атрибут — для внутреннего использования
        self._employee_id = self.__generate_employee_id()

    def consume_vacation(self, days):
        if days > self.remaining_vacation_days:
            raise ValueError("Недостаточно отпускных дней")
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f"Остаток отпускных дней: {self.remaining_vacation_days}."

    # Приватный метод — только для использования внутри класса
    def __generate_employee_id(self):
        return hash(str(self.first_name) + str(self.second_name) + str(self.gender))



class FullTimeEmployee(Employee):
    def __init__(self, first_name, second_name, gender, salary):
        super().__init__(first_name, second_name, gender)
        # Приватный атрибут — доступ только внутри класса
        self.__salary = salary

    def get_unpaid_vacation(self, start_date, days):
        return (f"Начало неоплачиваемого отпуска: {start_date}, "
                f"продолжительность: {days} дней.")

    # Приватный метод — только для использования внутри класса
    def __get_vacation_salary(self):
        # Отпускные = 80% от зарплаты
        return float(self.__salary * 0.8)

    # Публичный метод для получения отпускных (использует приватный метод)
    def get_vacation_pay(self):
        return self.__get_vacation_salary()



class PartTimeEmployee(Employee):
    vacation_days = 14

    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)
        self.remaining_vacation_days = PartTimeEmployee.vacation_days



# Пример использования
# Создаём сотрудника на полной ставке с зарплатой 50 000 руб.
full_time_employee = FullTimeEmployee('Иван', 'Иванов', 'м', 50000)

# Создаём сотрудника на частичной ставке
part_time_employee = PartTimeEmployee('Анна', 'Петрова', 'ж')

# Проверяем работу методов
print(f"ID сотрудника (защищённый атрибут): {full_time_employee._employee_id}")
print(full_time_employee.get_unpaid_vacation('2025-01-01', 14))
print(f"Отпускные (80% от зарплаты): {full_time_employee.get_vacation_pay()} руб.")
part_time_employee.consume_vacation(5)
print(part_time_employee.get_vacation_details())

# Попытка прямого доступа к приватным атрибутам/методам (вызовет ошибку)
# print(full_time_employee.__salary)  # AttributeError
# print(full_time_employee.__get_vacation_salary())  # AttributeError
