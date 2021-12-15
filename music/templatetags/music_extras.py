import re

from django import template
from django.utils.text import slugify


register = template.Library()


@register.filter
def text_to_node_id(text):

    '''
        initially used inflect package, but could not easily account for vernacular intracacies like nineties instead of ninetys
        easy enough to do a few find and replaces instead
    '''
    text = text.replace("50's", "fifties"   )
    text = text.replace("60's", "sixties")
    text = text.replace("90's", "nineties")
    text = slugify(text)

    return text
