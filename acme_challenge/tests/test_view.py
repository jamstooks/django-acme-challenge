"""
    Simple test to confirm that the view shows what it should when it should
"""

from django.test import TestCase, Client
from django.conf import settings

__all__ = (
    'ViewTest',
)

class ViewTest(TestCase):

    def setUp(self):
        """
            Set the settings variables
        """
        settings.ACME_CHALLENGE_URL_SLUG = "test"
        settings.ACME_CHALLENGE_TEMPLATE_CONTENT = "test content"
        
    def testView(self):
        c = Client()
        response = c.get("/test")
        self.assertEqual(response.content, "test content")
        response = c.get("/test2")
        self.assertEqual(response.status_code, 404)