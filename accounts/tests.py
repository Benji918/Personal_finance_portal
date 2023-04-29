from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from .models import Profile, SMSCode

class CustomUserModelTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='testuser@example.com',
            first_name='Test',
            last_name='User',
            password='testpass123'
        )
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='admin@example.com',
            password='adminpass123'
        )
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class ProfileModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            first_name='Test',
            last_name='User',
            password='testpass123'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            bio='Test bio',
            avatar=SimpleUploadedFile("test_avatar.jpg", b"file_content", content_type="image/jpeg")
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.bio, 'Test bio')
        self.assertTrue(self.profile.avatar)

    def test_profile_thumbnail_created(self):
        self.assertIn('profile_avatars', self.profile.avatar.url)
        response = self.client.get(reverse('profile_detail', kwargs={'pk': self.user.pk}))
        self.assertContains(response, '<img')
        self.assertContains(response, 'profile_avatars')

class SMSCodeModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            first_name='Test',
            last_name='User',
            password='testpass123'
        )
        self.sms_code = SMSCode.objects.create(user=self.user)

    def test_sms_code_creation(self):
        self.assertEqual(self.sms_code.user, self.user)
        self.assertTrue(self.sms_code.number)

    def test_sms_code_saved(self):
        self.sms_code.save()
        self.assertRegex(self.sms_code.number, r'^\d{6}$')

