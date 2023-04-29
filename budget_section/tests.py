from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from datetime import date
from .models import Budget, Category, Transaction, BudgetTransaction


class BudgetModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.budget = Budget.objects.create(
            name='Test Budget',
            amount=1000.00,
            start_date=date.today(),
            user=self.user
        )

    def test_budget_str(self):
        self.assertEqual(str(self.budget), self.budget.name)

    def test_budget_slug(self):
        expected_slug = slugify(self.budget.name)
        self.assertEqual(self.budget.slug, expected_slug)

    def test_budget_amount(self):
        self.assertEqual(self.budget.amount, 1000.00)


class CategoryModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(
            name='Test Category',
            description='Test category description',
            user=self.user
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_category_slug(self):
        expected_slug = slugify(self.category.name)
        self.assertEqual(self.category.slug, expected_slug)


class TransactionModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.budget = Budget.objects.create(
            name='Test Budget',
            amount=1000.00,
            start_date=date.today(),
            user=self.user
        )
        self.category = Category.objects.create(
            name='Test Category',
            user=self.user
        )
        self.transaction = Transaction.objects.create(
            title='Test Transaction',
            amount=100.00,
            category=self.category,
            budget=self.budget,
            date=date.today(),
            user=self.user
        )

    def test_transaction_str(self):
        self.assertEqual(str(self.transaction), self.transaction.title)

    def test_transaction_slug(self):
        expected_slug = slugify(self.transaction.title)
        self.assertEqual(self.transaction.slug, expected_slug)

    def test_transaction_amount(self):
        self.assertEqual(self.transaction.amount, 100.00)


class BudgetTransactionModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.budget = Budget.objects.create(
            name='Test Budget',
            amount=1000.00,
            start_date=date.today(),
            user=self.user
        )
        self.category = Category.objects.create(
            name='Test Category',
            user=self.user
        )
        self.transaction = Transaction.objects.create(
            title='Test Transaction',
            amount=100.00,
            category=self.category,
            budget=self.budget,
            date=date.today(),
            user=self.user
        )
        self.budget_transaction = BudgetTransaction.objects.create(
            budget=self.budget,
            transaction=self.transaction,
            user=self.user
        )

    def test_budget_transaction_str(self):
        expected_str = f"{self.budget.name} - {self.transaction.title}"
        self.assertEqual(str(self.budget_transaction), expected_str)

