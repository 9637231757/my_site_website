from django.contrib import admin
from .models import Comment
from .models import Post,Author,Tag


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author","tag","date")
    list_display = ("title","date","author")
    prepopulated_fields = {"slug":("title")}
    
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")       
    
# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
