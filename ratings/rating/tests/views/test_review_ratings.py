from django.test import TestCase
from django.urls import reverse
from rating.forms import RatingAndReviewsForm

class TestReviewRatingsView(TestCase):
    """Tests for the Review Ratings page."""

    def setUp(self):
        self.url = reverse('review_ratings')
        self.form_input = {
            'name_of_product' : 'Some Product',
            'average_rating' : 4.7,
            'number_of_reviews' : 1000
        }

    def test_review_rating_url(self):
        self.assertTrue(self.url, '/review-a-rating/')

    def test_review_rating_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_ratings.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, RatingAndReviewsForm))
