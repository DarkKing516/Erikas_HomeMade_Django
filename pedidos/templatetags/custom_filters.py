from django import template
import locale
import datetime

register = template.Library()

@register.filter
def fecha_es(value):
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    if isinstance(value, datetime.date):
        return value.strftime('%d %b %Y')
    return value
