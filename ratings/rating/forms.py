from django import forms

class RatingAndReviewsForm(forms.Form):
    name_of_product = forms.CharField(
        label='Name of Product',
        max_length=50
    )
    average_rating = forms.DecimalField(
        label='Average Rating',
        min_value=1.0,
        max_value=5.0,
        decimal_places=1
    )
    number_of_reviews = forms.IntegerField(label='Number of Reviews', min_value=0)
