from django.contrib import admin
from .models import PostModel, CategoryModel
from modeltranslation.admin import TranslationAdmin


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    link_display_list = ['id', 'name']


class PostModelTranslationAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'body']
    list_display_links = ['id', 'title']
    list_filter = ['created_at']
    search_fields = ['title', 'body']
    readonly_fields = ['post_view', ]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(PostModel, PostModelTranslationAdmin)
