from typing import List, Dict

from manager import FileManager


class FinanceJournal:
    """
    Класс операций с личным финансовым кошелком.
    """

    def __init__(self, incomes_filename: str, expenses_filename: str):
        """
        Инициализация объекта FinanceJournal.

        Args:
            incomes_filename (str): Имя файла для хранения данных о доходах.
            expenses_filename (str): Имя файла для хранения данных о расходах.
        """

        self.file_manager = FileManager(incomes_filename, expenses_filename)

    def show_balance(self) -> None:
        """
        Вывод текущего баланса, суммы доходов и расходов.
        """
        incomes = self.file_manager.get_incomes()
        expenses = self.file_manager.get_expenses()
        total_income = sum(incomes)
        total_expense = sum(expenses)
        balance = total_income - total_expense
        print(f"Текущий баланс: {balance}")
        print(f"Сумма доходов: {total_income}")
        print(f"Сумма расходов: {total_expense}")

    def add_record(self, record: str) -> None:
        """
        Добавление новой записи о доходе или расходе.

        Args:
            record str: Строка с данными записи.
        """
        incomes = self.file_manager.get_incomes()
        expenses = self.file_manager.get_expenses()
        total_income = sum(incomes)
        total_expense = sum(expenses)
        data = record.split("/")
        new_sum_expence = total_expense + float(data[3].split("=")[1]) \
            if data[2].split("=")[1] == "Расход" else 0

        if total_income >= new_sum_expence:
            self.file_manager.write_record(record)
        else:
            print(f"Ошибка: Сумма расходов превышает сумму доходов на "
                  f"{abs(total_income - new_sum_expence)}")
            return

    def edit_record(self, search_record: str, new_record: str) -> None:
        """
        Изменение существующей записи о доходе или расходе.

        Args:
            search_record (str): Запись, которую нужно изменить.
            new_record (Dict[str, str]): Словарь с новыми данными для записи.
        """

        self.file_manager.edit_record(search_record, new_record)

    def search_record(self, search_data: str) -> str | None:
        """
        Поиск записи по заданному критерию.

        Args:
            search_data (str): Критерий поиска.

        Returns:
            str: Найденная запись или None.
        """

        return self.file_manager.search_record(search_data)

    def search_records(self, search_data: str) -> List[str]:
        """
        Поиск записей по критериям.

        Args:
            search_data (str): Критерий поиска.

        Returns:
            str: Найденные записи.
        """
        return self.file_manager.search_records(search_data)
