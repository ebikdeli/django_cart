from django import template

import decimal

register = template.Library()

@register.filter(name='multiple')
def multiple(value, arg):
    if isinstance(value, decimal.Decimal):
        value = float(value)
    return value * arg
