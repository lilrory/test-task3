from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'menu_name', 'url', 'named_url']
    list_filter = ['menu_name']
    search_fields = ['name', 'menu_name']
