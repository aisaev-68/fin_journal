from datetime import datetime

from journal import FinanceJournal


class FinanceApp:
    """
    Класс консольного приложения для учета финансов.
    """

    def __init__(self, incomes_filename: str, expenses_filename: str):
        """
        Инициализация объекта FinanceApp.

        Args:
            incomes_filename (str): Имя файла для хранения данных о доходах.
            expenses_filename (str): Имя файла для хранения данных о расходах.
        """
        self.journal = FinanceJournal(incomes_filename, expenses_filename)

    @staticmethod
    def validate_date(date: str) -> str | None:
        """
        Валидация даты.

        Args:
            date (str): Введенная пользователем дата.

        Returns:
            str: Валидная дата в формате 'год-месяц-день' или None, если валидация не пройдена.
        """
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return date
        except ValueError:
            print("Ошибка: Неверный формат даты. Используйте формат 'год-месяц-день' (например, '2024-05-02').")
            return None

    @staticmethod
    def validate_category(category: str) -> str | None:
        """
        Валидация категории.

        Args:
            category (str): Введенная пользователем категория.

        Returns:
            str: Валидная категория или None, если валидация не пройдена.
        """

        if category.capitalize() not in ["Расход", "Доход"]:
            print("Ошибка: категория может быть либо 'Расход', либо 'Доход'.")
            return None
        return category

    @staticmethod
    def validate_amount(amount: str) -> float | None:
        """
        Валидация суммы.

        Args:
            amount (str): Введенная пользователем сумма.

        Returns:
            str: Валидная сумма или None, если валидация не пройдена.
        """
        try:
            return float(amount)
        except ValueError:
            print("Ошибка: сумма должна быть вещественным числом.")
            return None

    def input_data(self, flag=True) -> str:
        """Ввод данных из консоли."""

        category = self.validate_category(input("Введите категорию (Доход/Расход): ").capitalize())
        while category is None:
            category = self.validate_category(input("Введите категорию (Доход/Расход): "))

        date = self.validate_date(input("Введите дату: "))
        while date is None:
            date = self.validate_date(input("Введите дату: "))

        amount = self.validate_amount(input("Введите сумму: "))
        while amount is None:
            amount = self.validate_amount(input("Введите сумму: "))
        record = f"/1={date}/2={category.capitalize()}/3={str(amount)}"
        if flag:
            description = input("Введите описание: ")
            record += f"/4={description.capitalize()}\n"

        return record

    def run(self) -> None:
        """
        Запуск приложения.
        """
        while True:
            print("\nВыберите действие:")
            print("1. Вывод баланса")
            print("2. Добавление записи")
            print("3. Редактирование записи")
            print("4. Поиск записи")
            print("5. Выход")
            choice = input("\nВведите номер действия: ")

            if choice == '1':
                print("\n---------Баланс---------")
                self.journal.show_balance()
                print("--------------------------")
            elif choice == '2':
                print("---------Добавление записи---------\n")
                data = self.input_data()
                self.journal.add_record(data)
                print("---------Запись добавлена---------\n")

            elif choice == '3':
                print("---------Редактирование записи---------")
                print("---Введите данные для поиска записи----")
                data = self.input_data(flag=False)

                print("\nПоиск...")
                search_data = self.journal.search_record(data)

                if search_data:
                    print("-------------Найдена запись-------------")
                    print("Категория: ", search_data.split("/")[2].split("=")[1])
                    print("Дата: ", search_data.split("/")[1].split("=")[1])
                    print("Сумма: ", search_data.split("/")[3].split("=")[1])
                    print("Описание: ", search_data.split("/")[4].split("=")[1])
                    print("-----------Введите новые данные---------")
                    new_record = self.input_data()
                    self.journal.edit_record(search_data, new_record)
                    message = "Запись успешно изменена."
                else:
                    message = "Запись с указанной датой и категорией не найдена."
                print(f"-------{message}-------\n")
            elif choice == '4':
                search_criteria = self.input_data(flag=False)
                matching_records = self.journal.search_records(search_criteria)
                if matching_records:
                    print("\n-----Найдены следующие записи-----")
                    for i, record in enumerate(matching_records):
                        print(f"Запись № {i}")
                        print("Категория: ", record.split("/")[2].split("=")[1])
                        print("Дата: ", record.split("/")[1].split("=")[1])
                        print("Сумма: ", record.split("/")[3].split("=")[1])
                        print("Описание: ", record.split("/")[4].split("=")[1])
                    print("--------------------------------")
                else:
                    print("Записи по указанным критериям не найдены.")
            elif choice == '5':
                print("Программа завершена.")
                break
            else:
                print("Неверный ввод. Пожалуйста, выберите действие снова.")


if __name__ == "__main__":
    app = FinanceApp("data/доходы.txt", "data/расходы.txt")
    app.run()
