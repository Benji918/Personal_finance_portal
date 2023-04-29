from django.test import TestCase
from django.contrib.auth.models import User
from django.conf import settings
from .models import SavingsAccount, Deposit, Withdrawal, SavingsGoal


class SavingsAccountModelTestCase(TestCase):
    def setUp(self):
        self.user = settings.AUTH_USER_MODEL.objects.create_user(
            username='testuser', password='testpass'
        )
        self.savings = SavingsAccount.objects.create(
            user=self.user,
            name='Test Savings Account',
            balance=500.00,
            description='This is a test savings account.'
        )
        self.savings.save()

    def test_savings_account_slug(self):
        self.assertEqual(self.savings.slug, 'test-savings-account')

    def test_savings_account_str(self):
        self.assertEqual(str(self.savings), 'SavingsAccount name - Test Savings Account')


class DepositModelTestCase(TestCase):
    def setUp(self):
        self.user = settings.AUTH_USER_MODEL.objects.create_user(
            username='testuser', password='testpass'
        )
        self.savings = SavingsAccount.objects.create(
            user=self.user,
            name='Test Savings Account',
            balance=500.00,
            description='This is a test savings account.'
        )
        self.savings.save()
        self.deposit = Deposit.objects.create(
            user=self.user,
            name='Test Deposit',
            amount=200.00,
            savings=self.savings,
            description='This is a test deposit.'
        )
        self.deposit.save()

    def test_deposit_slug(self):
        self.assertEqual(self.deposit.slug, 'test-deposit')

    def test_deposit_str(self):
        self.assertEqual(str(self.deposit), 'Deposit name - Test Deposit')


class WithdrawalModelTestCase(TestCase):
    def setUp(self):
        self.user = settings.AUTH_USER_MODEL.objects.create_user(
            username='testuser', password='testpass'
        )
        self.savings = SavingsAccount.objects.create(
            user=self.user,
            name='Test Savings Account',
            balance=500.00,
            description='This is a test savings account.'
        )
        self.savings.save()
        self.withdrawal = Withdrawal.objects.create(
            user=self.user,
            name='Test Withdrawal',
            amount=100.00,
            savings=self.savings,
            description='This is a test withdrawal.'
        )
        self.withdrawal.save()

    def test_withdrawal_slug(self):
        self.assertEqual(self.withdrawal.slug, 'test-withdrawal')

    def test_withdrawal_str(self):
        self.assertEqual(str(self.withdrawal), 'Withdrawal name - Test Withdrawal')


class SavingsGoalModelTestCase(TestCase):
    def setUp(self):
        self.user = settings.AUTH_USER_MODEL.objects.create_user(
            username='testuser', password='testpass'
        )
        self.savings = SavingsAccount.objects.create(
            user=self.user,
            name='Test Savings Account',
            balance=500.00,
            description='This is a test savings account.'
        )
        self.savings.save()
        self.goal = SavingsGoal.objects.create(
            user=self.user,
            name='Test Savings Goal',
            amount=1000.00,
            savings=self.savings,
            description='This is a test savings goal.'
        )
        self.goal.save()

    def test_savings_goal_slug(self):
        self.assertEqual(self.goal.slug, 'test-savings-goal')

    def test_savings_goal_str(self):
        self.assertEqual(str(self.goal), 'SavingsGoal name - Test Savings Goal')
