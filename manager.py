import os
from typing import List


class FileManager:
    """
    Класс для управления файлами.
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

    def get_incomes(self) -> List[float]:
        """
        Получение списка доходов из файла.

        Args:
            filename (str): Имя файла с данными о доходах.

        Returns:
            List[float]: Список доходов.
        """
        filename = self.incomes_filename
        incomes = []
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                lines = file.readlines()
            for line in lines:
                fields = line.strip().split("/")
                if len(fields) == 5 and fields[2].split("=")[1] == "Доход":
                    amount = float(fields[3].split("=")[1])
                    incomes.append(amount)
        return incomes

    def get_expenses(self) -> List[float]:
        """
        Получение списка расходов из файла.

        Args:
            filename (str): Имя файла с данными о расходах.

        Returns:
            List[float]: Список расходов.
        """
        filename = self.expenses_filename
        expenses = []
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                lines = file.readlines()
            for line in lines:
                fields = line.strip().split("/")
                if len(fields) == 5 and fields[2].split("=")[1] == "Расход":
                    amount = float(fields[3].split("=")[1])
                    expenses.append(amount)
        return expenses

    def write_record(self, record: str) -> None:
        """
        Запись данных в файл.

        Args:
            record (str): Строка с данными для записи.
        """
        data = record.split("/")
        filename = self.incomes_filename if data[2].split("=")[1] == "Доход" \
            else self.expenses_filename
        with open(filename, 'a') as file:
            file.write(record)

    def edit_record(self, search_record: str, new_record: str) -> None:
        """
        Изменяет данные файла.

        Args:
            search_record (str): Строка с данными для поиска.
            new_record: Новые данные для изменения записи.
        """
        filename = self.incomes_filename \
            if search_record.split("/")[2].split("=")[1] == "Доход" \
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
            search_data (str): Критерий поиска.

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
            search_data (str): Критерий поиска.

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
