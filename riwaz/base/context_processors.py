from riwaz.number.utils import InterestedNumberService
from riwaz.base.filters import get_wishlist_numbers
from django.conf import settings
import random


def numbers(request):
    context = dict()

    if hasattr(settings, 'INTERESTED_NUMBERS') and settings.INTERESTED_NUMBERS:
        context["INTERESTED_NUMBERS"] = True
        recent_interests = InterestedNumberService(request).get()
        context["interested_numbers"] = recent_interests[:settings.INTERESTED_NUMBER_CONFIG.get("MAX_CARDS_TO_SHOW", 6)]
        context["wishlist"] = get_wishlist_numbers(request)
    if hasattr(settings, 'RANDOM_CSS_CLASS_CHOICES'):
        context["RANDOM_CSS_CLASS"] = random.choice(settings.RANDOM_CSS_CLASS_CHOICES)
    return context

def constants(request):
    return {
        "GOOGLE_ANALYTICS_ID": settings.GOOGLE_ANALYTICS_ID,
        "FACEBOOK_PIXEL_ID": settings.FACEBOOK_PIXEL_ID,
    }

