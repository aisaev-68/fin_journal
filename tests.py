import unittest
from main import FinanceApp
from journal import FinanceJournal


class TestFinanceApp(unittest.TestCase):

    def test_validate_date_valid(self):
        app = FinanceApp("data/incomes.txt", "data/expenses.txt")
        valid_date = "2024-05-04"
        self.assertEqual(app.validate_date(valid_date), valid_date)

    def test_validate_date_invalid(self):
        app = FinanceApp("data/incomes.txt", "data/expenses.txt")
        invalid_date = "2024/05/04"
        self.assertIsNone(app.validate_date(invalid_date))

    def test_validate_category_valid(self):
        app = FinanceApp("data/incomes.txt", "data/expenses.txt")
        valid_category = "Доход"
        self.assertEqual(app.validate_category(valid_category), valid_category)

    def test_validate_category_invalid(self):
        app = FinanceApp("data/incomes.txt", "data/expenses.txt")
        invalid_category = "Другое"
        self.assertIsNone(app.validate_category(invalid_category))

    def test_validate_amount_valid(self):
        app = FinanceApp("data/incomes.txt", "data/expenses.txt")
        valid_amount = "1500.0"
        self.assertEqual(app.validate_amount(valid_amount), float(valid_amount))

    def test_validate_amount_invalid(self):
        app = FinanceApp("data/incomes.txt", "data/expenses.txt")
        invalid_amount = "invalid"
        self.assertIsNone(app.validate_amount(invalid_amount))


class TestFinanceJournal(unittest.TestCase):

    def test_get_incomes(self):
        journal = FinanceJournal("data/incomes.txt", "data/expenses.txt")
        expected_incomes = [1500.0, 2000.0]
        self.assertEqual(journal._get_incomes(), expected_incomes)

    def test_get_expenses(self):
        journal = FinanceJournal("data/incomes.txt", "data/expenses.txt")
        expected_expenses = [1500.0, 2000.0]
        self.assertEqual(journal._get_expenses(), expected_expenses)


if __name__ == "__main__":
    unittest.main()