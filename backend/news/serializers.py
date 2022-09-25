from rest_framework.serializers import ModelSerializer
from .models import Category, News, User


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'descriptions', 'body', 'author', 'category']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user
