from .views import BlogPostRUD
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path(r'^(?P<pk>\d+)/$', BlogPostRUD.as_view(), name='post-rud'),
]
