from django.test import TestCase
from mail.models import Mail
import unittest


class MailTestCase(unittest.TestCase):
    def setUp(self):
        for _ in range(400):
            Mail.objects.create(name='Test', email='Test@test.com', message_text='This is a test message')
            Mail.objects.create(name='Test.', email='Test@test.ru', message_text='This is a test message...')

    def test_email(self):
        email_1 = Mail.objects.get(email='Test@test.ru')
        email_2 = Mail.objects.get(email='Test@test.com')
        self.assertEquals(email_1, 'Test@test.ru')
        self.assertEquals(email_2, 'Test@test.com')


if __name__ == '__main__':
    unittest.main()
