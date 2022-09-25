from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('books-category', views.CategoryViewSet, basename='books-category')
router.register('books', views.BooksViewSet, basename='books')
router.register('borrow', views.BorrowViewSet, basename='borrowed')


urlpatterns = [
    path('', include(router.urls)),
]
