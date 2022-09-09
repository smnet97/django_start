from django.contrib import admin
from .models import UserModel


@admin.register(UserModel)
class UserModel(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['id', 'username']
    search_fields = ['username']
