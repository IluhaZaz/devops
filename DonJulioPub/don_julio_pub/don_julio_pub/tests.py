from django.test import TestCase
from django.urls import reverse

class BasicTests(TestCase):
    def test_healthcheck(self):
        response = self.client.get('/ping/')
        self.assertEqual(response.status_code, 200)
    
    def test_settings_loaded(self):
        from django.conf import settings
        self.assertTrue(settings.DEBUG is not None)
    
    def test_database_config(self):
        from django.conf import settings
        self.assertEqual(settings.DATABASES['default']['ENGINE'], 'django.db.backends.postgresql')