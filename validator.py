from datetime import datetime


class Validator:
    """
    Класс для операций валидации вводимых данных.
    """

    def __init__(self):
        pass

    def validate_date(self, date: str) -> str | None:
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
            print("Ошибка: Неверный формат даты. Используйте формат 'год-месяц-день' "
                  "(например, '2024-05-02').")
            return None

    def validate_category(self, category: str) -> str | None:
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

    def validate_amount(self, amount: str) -> float | None:
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
