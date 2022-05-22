from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import requires_csrf_token
from .forms import RatingAndReviewsForm
from .helpers import calculate_score, review_number_of_reviews, review_score

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@requires_csrf_token
def review_ratings(request):
    if request.method == 'POST':
        form = RatingAndReviewsForm(request.POST)
        if form.is_valid():
            name_of_product = form['name_of_product'].data
            average_rating = float(form['average_rating'].data)
            number_of_reviews = int(form['number_of_reviews'].data)
            score = calculate_score(average_rating, number_of_reviews)
            comment_on_score = 'Calculated score: ' + str(round(score, 2))
            comment_on_product_quality = review_score(score)
            comment_on_number_of_reviews = review_number_of_reviews(number_of_reviews)
            messages = [comment_on_product_quality, comment_on_number_of_reviews]
            return render(request, 'review_ratings.html',
                {
                    'form' : form,
                    'name_of_product' : name_of_product,
                    'comment_on_score' : comment_on_score,
                    'messages' : messages
                }
            )
    form = RatingAndReviewsForm()
    return render(request, 'review_ratings.html', {'form' : form})

def page_not_found(request, exception, template_name='404.html'):
    return render(request, template_name)
