# views.py
# views file updated
"""from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post  # Use 'Post' instead of 'post'
from django.views.generic import ListView
from .forms import CommentForm
from django.views import View


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    
    
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"
        
        
class SinglePostsView(View):
    template_name = "blog/post-detail.html"
    model = Post
    
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post":post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request,"blog/post-detail.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        if  comment_form.is_valid():
            comment_form.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
             
            post = Post.objects.get(slug=slug)
            context = {
            "post":post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form
        }
        return render(request,"blog/post-detail.html", context)"""
    
    
# views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.views.generic import ListView
from .forms import CommentForm
from django.views import View


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"
        

class SinglePostsView(View):
    template_name = "blog/post-detail.html"
    model = Post  
    
    def get(self, request, slug):  
        post = get_object_or_404(Post, slug=slug)  
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request, "blog/post-detail.html", context)
    
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)  # Fetch post first
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)  
            comment.post = post  
            comment.save()  
            
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        # If form is invalid, re-render the page with the form errors
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form  
        }
        return render(request, "blog/post-detail.html", context)    