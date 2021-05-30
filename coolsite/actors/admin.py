from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Actor, Category


class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'time_create', 'get_html_photo', 'is_published']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']
    list_editable = ['is_published']
    list_filter = ['is_published', 'time_create']
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'category', 'content', 'photo', 'get_html_photo', 'is_published')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=45')

    get_html_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Actor, ActorAdmin)
admin.site.register(Category, CategoryAdmin)


admin.site.site_title = 'Админ-панель сайта о Актерах'
admin.site.site_header = 'Админ-панель сайта о Актерах'
