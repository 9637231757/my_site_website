from django.contrib import admin

from .models import post, Author, Tag

# Register your models here.
admin.site.register(post)
admin.site.register(Author)
admin.site.register(Tag)
