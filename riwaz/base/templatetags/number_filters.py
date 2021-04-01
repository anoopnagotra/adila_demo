import random

from django import template
from django.core.paginator import Page

register = template.Library()


@register.filter()
def random_number(number_list):
    try:
        if type(number_list) == Page and number_list.object_list:
            return random.choice(number_list.object_list)
        elif type(number_list) == list and number_list:
            return random.choice(number_list)
    except Exception:
        pass
    return None
