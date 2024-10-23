import re
from django import template
from django.utils.html import strip_tags

register = template.Library()

@register.filter(name='strip_html')
def strip_html(value):
    """
    HTML etiketlerini temizler ve sadece düz metni döndürür.
    """
    return strip_tags(value)
