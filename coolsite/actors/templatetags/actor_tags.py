from django import template
from actors.models import Category


register = template.Library()


@register.simple_tag()
def get_categories(filter=None):

    if not filter:
        return Category.objects.all()

    return Category.objects.filter(slug=filter)


@register.inclusion_tag('actors/list_categories.html')
def show_categories(sort=None, category_selected=0):

    if not sort:
        categories = Category.objects.all()

    else:
        categories = Category.objects.order_by(sort)

    return {'categories': categories, 'category_selected': category_selected}
