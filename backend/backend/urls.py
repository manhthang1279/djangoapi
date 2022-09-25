from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('news.urls')),
    path('', include('library.urls')),
    path('admin/', admin.site.urls),
]
