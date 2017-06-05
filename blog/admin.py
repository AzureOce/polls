from django.contrib import admin

# Register your models here.
from blog.models import Post, Tag, Category

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
