"""Algorithm to calculate the score for a review"""
def calculate_score(average_rating, number_of_reviews):
    numerator = (number_of_reviews * average_rating * 40) + number_of_reviews
    denominator = 41 * number_of_reviews
    return numerator / denominator

def review_number_of_reviews(number_of_reviews):
    if number_of_reviews >= 100 and number_of_reviews < 500:
        return f'{number_of_reviews} reviews is a small sample size. Perhaps you can get this product elsewhere or you could consider getting something similar to this product (if that\'s what you really want).'
    elif number_of_reviews < 100:
        return f'{number_of_reviews} reviews is an incredibly small sample size. These reviews could be made up! Perhaps you can get this product elsewhere or you could get something similar to this product.'
    else:
        return f'{number_of_reviews} reviews is an acceptable sample size so the assessment of this product is more likely to be accurate.'

def review_score(score):
    if score >= 4.5:
        return 'This seems like a good quality product.'
    elif score > 4.3 and score < 4.5:
        return 'This product could be good, but there will be something about it that could be mildly frustrating.'
    else:
        return 'This product is not recommended. It\'s best to save your money and your peace of mind. However, it\'s your decision whether you still want to purchase this product or not.'
