import unittest
from main import FinanceApp
from manager import FileManager


class TestFinanceApp(unittest.TestCase):

    def test_validate_date_valid(self):
        app = FinanceApp("data/incomes.txt", "data/expenses.txt")
        valid_date = "2024-05-04"
        self.assertEqual(app.validator.validate_date(valid_date), valid_date)

    def test_validate_date_invalid(self):
        app = FinanceApp("data/incomes.txt", "data/expenses.txt")
        invalid_date = "2024/05/04"
        self.assertIsNone(app.validator.validate_date(invalid_date))

    def test_validate_category_valid(self):
        app = FinanceApp("data/incomes.txt", "data/expenses.txt")
        valid_category = "Доход"
        self.assertEqual(app.validator.validate_category(valid_category), valid_category)

    def test_validate_category_invalid(self):
        app = FinanceApp("data/incomes.txt", "data/expenses.txt")
        invalid_category = "Другое"
        self.assertIsNone(app.validator.validate_category(invalid_category))

    def test_validate_amount_valid(self):
        app = FinanceApp("data/incomes.txt", "data/expenses.txt")
        valid_amount = "1500.0"
        self.assertEqual(app.validator.validate_amount(valid_amount), float(valid_amount))

    def test_validate_amount_invalid(self):
        app = FinanceApp("data/incomes.txt", "data/expenses.txt")
        invalid_amount = "invalid"
        self.assertIsNone(app.validator.validate_amount(invalid_amount))


class TestFinanceJournal(unittest.TestCase):

    def setUp(self):

        with open("data/incomes.txt", "w") as incomes_file:
            incomes_file.write("/1=2024-04-30/2=Доход/3=1500.0/4=Зарплата аванс\n")
            incomes_file.write("/1=2024-04-30/2=Доход/3=2000.0/4=Зарплата\n")

        with open("data/expenses.txt", "w") as expenses_file:
            expenses_file.write("/1=2024-04-30/2=Расход/3=1500.0/4=Покупка продуктов\n")
            expenses_file.write("/1=2024-04-30/2=Расход/3=2000.0/4=Покупка чего то\n")

    def tearDown(self):
        import os
        os.remove("data/incomes.txt")
        os.remove("data/expenses.txt")

    def test_get_incomes(self):
        journal = FileManager("data/incomes.txt", "data/expenses.txt")
        expected_incomes = [1500.0, 2000.0]
        self.assertEqual(journal.get_incomes(), expected_incomes)

    def test_get_expenses(self):
        journal = FileManager("data/incomes.txt", "data/expenses.txt")
        expected_expenses = [1500.0, 2000.0]
        self.assertEqual(journal.get_expenses(), expected_expenses)


if __name__ == "__main__":
    unittest.main()
