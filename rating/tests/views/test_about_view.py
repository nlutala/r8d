from django.test import TestCase
from django.urls import reverse

class TestAboutView(TestCase):
    """Tests for the About page."""

    def setUp(self):
        self.url = reverse('about')

    def test_about_url(self):
        self.assertTrue(self.url, '/about/')

    def test_about_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
