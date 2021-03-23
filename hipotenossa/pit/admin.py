from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post
from .models import User



@admin.register(Post, User)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","slug", "author", "created")