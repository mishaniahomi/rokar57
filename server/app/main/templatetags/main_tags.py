from django import template

from main.models import Banner


register = template.Library()


@register.simple_tag()
def get_banners():
    return Banner.objects.all()
