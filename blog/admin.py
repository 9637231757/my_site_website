from django.contrib import admin

from .models import post,Author,Tag


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author","tag","date")
    list_display = ("title","date","author")
    prepopulated_fields = {"slug":("title")}
# Register your models here.
admin.site.register(post)
admin.site.register(Author)
admin.site.register(Tag)
