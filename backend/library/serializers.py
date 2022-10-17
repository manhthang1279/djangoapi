from rest_framework.serializers import ModelSerializer
from .models import Category, Books, Borrow


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'special_number', 'title', 'author', 'company', 'category', 'status',
                  'publishing_year', 'price', 'subject_type', 'general_number', 'classify', 'language', 'source']


class BorrowSerializer(ModelSerializer):
    class Meta:
        model = Borrow
        fields = ['id', 'borrower', 'borrowed_book', 'status']
