from django.contrib import admin
from .models import Category, News, User, Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'department_name']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'date_created', 'date_updated', 'active']
    list_display_links = ['id', 'title', 'author', 'category', 'date_created', 'date_updated', 'active']
    list_filter = ['category', 'author', 'active', 'date_created']
    search_fields = ['title', 'descriptions', 'body', 'author']


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Department, DepartmentAdmin)
