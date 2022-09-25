from rest_framework import viewsets, generics, permissions
from .models import Category, News, User
from .serializers import CategorySerializer, NewsSerializer, UserSerializer
# from rest_framework.parsers import MultiPartParser


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class UserViewSet(viewsets.ViewSet,
                  generics.CreateAPIView,
                  generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    # parser_classes = [MultiPartParser, ]

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]
