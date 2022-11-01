from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Category, News, User


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NewsSerializer(ModelSerializer):
    # image = SerializerMethodField()
    #
    # def get_image(self, course):
    #     request = self.context['request']
    #     name = course.image.name
    #     if name.startswith('static/'):
    #         path = '%s' % name
    #     else:
    #         path = '/static/%s' % name
    #     return request.build_absolute_uri(path)

    class Meta:
        model = News
        fields = ['id', 'title', 'descriptions', 'body', 'author', 'category', 'image']


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
