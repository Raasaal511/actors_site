from django.core.cache import cache
from django.db.models import Count

from actors.models import Category

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
]


class DataMixin:
    paginate_by = 4

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')

        if not cats:
            category = Category.objects.annotate(Count('actor'))
            cache.set('categories', cats, 60)

        user_menu = menu.copy()

        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['categories'] = category

        if 'category_selected' not in context:
            context['category_selected'] = 0

        return context
