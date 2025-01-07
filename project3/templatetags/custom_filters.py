from django import template

register = template.Library()

@register.filter
def excerpt_words(value, word_limit):
    words = value.split()
    if len(words) > word_limit:
        return ' '.join(words[:word_limit]) + '...'
    return value
