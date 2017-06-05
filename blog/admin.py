from django.contrib import admin

# Register your models here.
from blog.models import Post, Tag, Category

admin.register(Post)
admin.register(Category)
admin.register(Tag)
