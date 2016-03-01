"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from foad.factories import FoadUserFactory
from foad.models import FoadUser

class FoadUserTestCase(TestCase):

    def test_foad_user_create(self):
        user = FoadUserFactory.create()
        self.assertEqual(1, FoadUser.objects.count())

    def test_change_password(self):
        user = FoadUserFactory.create()
        old_password = user.password
        user.change_password()
        self.assertNotEqual(old_password, user.password)

    def test_reset_password(self):
        user = FoadUserFactory.create()
        old_password = user.password
        user.reset_password()
        self.assertNotEqual(old_password, user.password)