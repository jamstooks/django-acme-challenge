"""
    Simple test to confirm that the view shows what it should when it should
"""

from django.test import TestCase, Client
from django.conf import settings

__all__ = (
    'ViewTest',
)

SLUG = 'test'
CONTENT = 'test content'


class ViewTest(TestCase):

    def setUp(self):
        """
            Set the settings variables
        """
        settings.ACME_CHALLENGE_URL_SLUG = SLUG
        settings.ACME_CHALLENGE_TEMPLATE_CONTENT = CONTENT
        
    def testView(self):
        c = Client()
        response = c.get("/%s" % SLUG)
        self.assertEqual(response.content.decode(), CONTENT)
        response = c.get("/test2")
        self.assertEqual(response.status_code, 404)