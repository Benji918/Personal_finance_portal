from decimal import Decimal
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Income, Outcome, Balance


class IncomeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a test user
        user_model = get_user_model()
        cls.test_user = user_model.objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='testpassword'
        )
        # Create a test income object
        cls.test_income = Income.objects.create(
            user=cls.test_user,
            value=Decimal('1000.00'),
            date=timezone.now().date(),
            type=Income.ITypes.SAL,
            repetitive=True,
            repetition_interval=Income.RInterval.MON,
            repetition_time=1,
            repetition_end=timezone.now().date() + timezone.timedelta(days=365),
            comment='Test comment'
        )

    def test_income_object_creation(self):
        self.assertEqual(str(self.test_income), f'Income {self.test_income.id} - SALARY - {self.test_income.date.strftime("%Y/%m/%d")}')
        self.assertEqual(self.test_income.user, self.test_user)
        self.assertEqual(self.test_income.value, Decimal('1000.00'))
        self.assertEqual(self.test_income.type, Income.ITypes.SAL)
        self.assertEqual(self.test_income.repetitive, True)
        self.assertEqual(self.test_income.repetition_interval, Income.RInterval.MON)
        self.assertEqual(self.test_income.repetition_time, 1)
        self.assertEqual(self.test_income.repetition_end, self.test_income.date + timezone.timedelta(days=365))
        self.assertEqual(self.test_income.comment, 'Test comment')

    def test_income_object_update(self):
        self.test_income.value = Decimal('1500.00')
        self.test_income.save()
        updated_income = Income.objects.get(id=self.test_income.id)
        self.assertEqual(updated_income.value, Decimal('1500.00'))

    def test_income_object_deletion(self):
        self.test_income.delete()
        self.assertFalse(Income.objects.filter(id=self.test_income.id).exists())


class OutcomeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a test user
        user_model = get_user_model()
        cls.test_user = user_model.objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='testpassword'
        )
        # Create a test outcome object
        cls.test_outcome = Outcome.objects.create(
            user=cls.test_user,
            value=Decimal('500.00'),
            date=timezone.now().date(),
            type=Outcome.OTypes.GRO,
            repetitive=True,
            repetition_interval=Outcome.RInterval.WEK,
            repetition_time=1,
            repetition_end=timezone.now().date() + timezone.timedelta(weeks=52),
            comment='Test comment'
        )

    def test_outcome_object_creation(self):
        self.assertEqual(str(self.test_outcome), f'Outcome {self.test_outcome.id} - GROCERIES - {self.test_outcome.date.strftime("%Y/%m/%d")}')
        self.assertEqual(self.test_outcome.user, self.test_user)
        self.assertEqual(self.test_outcome.value, Decimal('500.00'))
        self.assertEqual(self.test_outcome.type, Outcome.OTypes.GRO)
        self.assertEqual(self.test_outcome.repetitive, True)
        self.assertEqual(self.test_outcome.repetition_interval, Outcome.RInterval.WEK)
        self.assertEqual(self.test_outcome.repetition_time, 1)
        self.assertEqual(self.test_outcome.repetition_end, self.test_outcome.date + timezone.timedelta(days=365))
        self.assertEqual(self.test_outcome.comment, 'Test comment')





class ModelTestCase(TestCase):

    def setUp(self):
        self.user_email = "testuser@example.com"
        self.user_password = "testpass123"
        User = get_user_model()
        self.user = User.objects.create_user(
            email=self.user_email, password=self.user_password)
        self.income = Income.objects.create(
            user=self.user, value=5000.00, date=timezone.now().date(),
            type=Income.ITypes.SAL, repetitive=True,
            repetition_interval=Income.RInterval.MON,
            repetition_time=1, repetition_end=timezone.now().date() + timezone.timedelta(days=365),
            comment="Test Income")
        self.outcome = Outcome.objects.create(
            user=self.user, value=2000.00, date=timezone.now().date(),
            type=Outcome.OTypes.REN, repetitive=True,
            repetition_interval=Outcome.RInterval.MON,
            repetition_time=1, repetition_end=timezone.now().date() + timezone.timedelta(days=365),
            comment="Test Outcome")
        self.balance = Balance.objects.create(
            user=self.user, value=5000.00, date=timezone.now().date(),
            type=Balance.BType.CUR, comment="Test Balance")

    def test_income_model(self):
        self.assertEqual(str(self.income), f'Income {self.income.id} - {self.income.get_type_display()} - {self.income.date.strftime("%Y/%m/%d")}')
        self.assertTrue(isinstance(self.income, Income))
        self.assertTrue(self.income.repetitive)
        self.assertEqual(self.income.repetition_interval, Income.RInterval.MON)
        self.assertEqual(self.income.repetition_time, 1)
        self.assertEqual(self.income.repetition_end, timezone.now().date() + timezone.timedelta(days=365))
        self.assertEqual(self.income.comment, "Test Income")

    def test_outcome_model(self):
        self.assertEqual(str(self.outcome), f'Outcome {self.outcome.id} - {self.outcome.get_type_display()} - {self.outcome.date.strftime("%Y/%m/%d")}')
        self.assertTrue(isinstance(self.outcome, Outcome))
        self.assertTrue(self.outcome.repetitive)
        self.assertEqual(self.outcome.repetition_interval, Outcome.RInterval.MON)
        self.assertEqual(self.outcome.repetition_time, 1)
        self.assertEqual(self.outcome.repetition_end, timezone.now().date() + timezone.timedelta(days=365))
        self.assertEqual(self.outcome.comment, "Test Outcome")

    def test_balance_model(self):
        self.assertEqual(str(self.balance), f'Balance {self.balance.id} - {self.balance.get_type_display()}')
        self.assertTrue(isinstance(self.balance, Balance))
        self.assertEqual(self.balance.value, 5000.00)
        self.assertEqual(self.balance.type, Balance.BType.CUR)
        self.assertEqual(self.balance.comment, "Test Balance")