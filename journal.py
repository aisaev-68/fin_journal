import os
from typing import List, Dict


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
        self.incomes_filename = incomes_filename
        self.expenses_filename = expenses_filename

        if not os.path.exists(self.incomes_filename):
            with open(self.incomes_filename, 'w') as f:
                pass

        if not os.path.exists(self.expenses_filename):
            with open(self.expenses_filename, 'w') as f:
                pass

    def show_balance(self) -> None:
        """
        Вывод текущего баланса, суммы доходов и расходов.
        """
        incomes = self._get_incomes()
        expenses = self._get_expenses()
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
        incomes = self._get_incomes()
        expenses = self._get_expenses()
        total_income = sum(incomes)
        total_expense = sum(expenses)
        data = record.split("/")
        new_sum_expence = total_expense + float(data[3].split("=")[1]) \
            if data[2].split("=")[1] == "Расход" else 0

        if total_income >= new_sum_expence:

            filename = self.incomes_filename if data[2].split("=")[1] == "Доход" \
                else self.expenses_filename

            with open(filename, 'a') as file:
                file.write(record)

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
        filename = self.incomes_filename if search_record.split("/")[2].split("=")[1] == "Доход" \
            else self.expenses_filename
        with open(filename, 'r+') as file:
            lines = file.readlines()
            for line in lines:
                if search_record in line:
                    file.seek(0)
                    ind = lines.index(line)
                    lines[ind] = new_record
                    file.writelines(lines)
                    file.truncate()
                    break

    def search_record(self, search_data: str) -> str | None:
        """
        Поиск записи по заданному критерию.

        Args:
            search_criteria (str): Критерий поиска.

        Returns:
            str: Найденная запись или None.
        """

        filename = self.incomes_filename \
            if search_data.split("/")[2].split("=")[1] == "Доход" \
            else self.expenses_filename
        with open(filename, 'r') as file:
            lines = file.readlines()
            found_line = None
            for line in lines:
                if search_data in line:
                    found_line = line
                    break
            return found_line if found_line else None

    def search_records(self, search_data: str) -> List[str]:
        """
        Поиск записей по критериям.

        Args:
            search_criteria (str): Критерий поиска.

        Returns:
            str: Найденные записи.
        """

        filename = self.incomes_filename \
            if search_data.split("/")[2].split("=")[1] == "Доход" \
            else self.expenses_filename
        with open(filename, 'r') as file:
            lines = file.readlines()
            found_lines = []
            data = search_data.split("/")
            for line in lines:
                if data[1].split("=")[1] == line.split("/")[1].split("=")[1] \
                        or data[3].split("=")[1] == line.split("/")[3].split("=")[1]:
                    found_lines.append(line)

            return found_lines

    def _get_incomes(self) -> List[float]:
        """
        Получение списка доходов.

        Returns:
            List[float]: Список доходов.
        """
        incomes = []

        with open(self.incomes_filename, 'r') as file:
            lines = file.readlines()
        for line in lines:
            fields = line.strip().split("/")
            if len(fields) == 5:
                amount = float(fields[3].split("=")[1])
                if fields[2].split("=")[1] == "Доход":
                    incomes.append(amount)

        return incomes

    def _get_expenses(self) -> List[float]:
        """
        Получение списка расходов.

        Returns:
            List[float]: Список расходов.
        """

        expenses = []

        with open(self.expenses_filename, 'r') as file:
            lines = file.readlines()
        for line in lines:
            fields = line.strip().split("/")
            if len(fields) == 5:
                amount = float(fields[3].split("=")[1])
                if fields[2].split("=")[1] == "Расход":
                    expenses.append(amount)
        return expenses
