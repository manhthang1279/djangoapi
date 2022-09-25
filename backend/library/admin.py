from django.contrib import admin
from .models import Category, Books, Borrow


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']


class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'special_number', 'title', 'author', 'company',
                    'publishing_year', 'category', 'status']
    list_display_links = ['id', 'special_number', 'title', 'author', 'company',
                          'publishing_year', 'category', 'status']
    list_filter = ['author', 'company', 'category', 'status']
    search_fields = ['title', 'author', 'company', 'category']


class BorrowAdmin(admin.ModelAdmin):
    list_display = ['borrower', 'borrowed_book']
    list_display_links = ['borrower', 'borrowed_book']
    list_filter = ['borrower', 'borrowed_book']
    search_fields = ['borrower', 'borrowed_book']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Borrow, BorrowAdmin)
