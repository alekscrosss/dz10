# templatetags/quote_extras.py
from django.db.models import Count
from django import template
from ..models import Tag

register = template.Library()

@register.simple_tag
def get_top_tags():
    return Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]
