from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('news-category', views.CategoryViewSet, basename='news-category')
router.register('news', views.NewsViewSet, basename='news')
router.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
