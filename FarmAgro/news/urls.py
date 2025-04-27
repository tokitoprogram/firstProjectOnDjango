

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from .views import *



urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title': 'ff'}), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),


]

