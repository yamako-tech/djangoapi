from django.contrib import admin
from .models import Todo, Post

admin.site.register(Post)
admin.site.register(Todo)