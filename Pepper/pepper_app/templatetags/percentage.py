from django import template
from math import floor

register = template.Library()


@register.simple_tag
def discount(original, retail):
    return '-' + str(floor(retail * 100 / original)) + '%'
