from django.test import TestCase
from rating.forms import RatingAndReviewsForm

class TestReviewRatingsForm(TestCase):
    """Tests for the Review Ratings page."""

    def setUp(self):
        self.form_input = {
            'name_of_product' : 'Some Product',
            'average_rating' : 4.7,
            'number_of_reviews' : 1000
        }

    def test_form_contains_required_fields(self):
        form = RatingAndReviewsForm()
        self.assertIn('name_of_product', form.fields)
        self.assertIn('average_rating', form.fields)
        self.assertIn('number_of_reviews', form.fields)

    def test_form_accepts_valid_inputs(self):
        form = RatingAndReviewsForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_name_of_product_must_be_less_than_51_characters_long(self):
        self.form_input['name_of_product'] = 'X' * 51
        form = RatingAndReviewsForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_name_of_product_cannot_be_blank(self):
        self.form_input['name_of_product'] = ''
        form = RatingAndReviewsForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_average_rating_cannot_be_blank(self):
        self.form_input['average_rating'] = ''
        form = RatingAndReviewsForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_average_rating_cannot_be_less_than_1(self):
        self.form_input['average_rating'] = 0.9
        form = RatingAndReviewsForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_average_rating_must_be_between_1_and_5_inclusive(self):
        self.form_input['average_rating'] = 1.0
        form = RatingAndReviewsForm(data=self.form_input)
        self.assertTrue(form.is_valid())
        self.form_input['average_rating'] = 5.0
        form = RatingAndReviewsForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_average_rating_cannot_be_more_than_5(self):
        self.form_input['average_rating'] = 5.1
        form = RatingAndReviewsForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_average_rating_must_be_to_1_decimal_place(self):
        self.form_input['average_rating'] = 1.11
        form = RatingAndReviewsForm(data=self.form_input)
        self.assertFalse(form.is_valid())
        self.form_input['average_rating'] = 1.1
        form = RatingAndReviewsForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_number_of_reviews_cannot_be_blank(self):
        self.form_input['number_of_reviews'] = ''
        form = RatingAndReviewsForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_number_of_reviews_must_be_an_integer(self):
        self.form_input['number_of_reviews'] = 1000.1
        form = RatingAndReviewsForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_number_of_reviews_cannot_be_less_than_0(self):
        self.form_input['number_of_reviews'] = -1
        form = RatingAndReviewsForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_number_of_reviews_does_not_have_an_upper_limit(self):
        self.form_input['number_of_reviews'] = 1000000
        form = RatingAndReviewsForm(data=self.form_input)
        self.assertTrue(form.is_valid())
