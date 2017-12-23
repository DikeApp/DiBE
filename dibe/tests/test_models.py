from django.test import TestCase
from ..models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User(username='test', password='testtest')
        self.user.save()

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)

    def test_to_string(self):
        self.assertEqual(self.user.username, str(self.user))
