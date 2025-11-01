class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f"Остаток отпускных дней: {self.remaining_vacation_days}."


class FullTimeEmployee(Employee):
    def get_unpaid_vacation(self, start_date_of_not_payment_vacation, days_of_vacation):
        return (
            f"Начало неоплачиваемого отпуска: {start_date_of_not_payment_vacation}, "
            f"продолжительность: {days_of_vacation} дней."
        )


class PartTimeEmployee(Employee):
    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)
        self.remaining_vacation_days = PartTimeEmployee.vacation_days
        PartTimeEmployee.vacation_days = 14


# Пример использования:
full_time_employee = FullTimeEmployee("Роберт", "Крузо", "м")
print(full_time_employee.get_unpaid_vacation("2023-07-01", 5))
part_time_employee = PartTimeEmployee("Алёна", "Пятницкая", "ж")
print(part_time_employee.get_vacation_details())
