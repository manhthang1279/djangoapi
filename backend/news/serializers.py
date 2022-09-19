from rest_framework.serializers import ModelSerializer
from .models import Category, News


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'descriptions',
            'body',
            'image',
            'active'
        ]