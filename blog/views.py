# views.py file code updated

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
            "comment_form": CommentForm(),
            "comments": post.comments.all()
            
        }
        return render(request, "blog/post-detail.html", context)
    
    def post(self, request, slug):
        #post = get_object_or_404(Post, slug=slug)  # Fetch post first
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)  
            comment.post = post  
            comment.save()  
            
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        else:
            print(f"Form validation failed: {comment_form.errors}")
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all()
  
        }
        return render(request, "blog/post-detail.html", context)    

class ReadLaterView(View):
    
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        
        context = {}
            
        if stored_posts is None or len(stored_posts) == 0:
             context["posts"] = []
             context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)     
            context["posts"] = posts 
            context["has_posts"] = True 
        
        return render(request, "blog/stored-posts.html", context)    
                 
    
    def post(self, request):
        stored_posts = request.session.get("stored_posts")
        
        if stored_posts is None:
            stored_posts = []
        
        post_id = int(request.POST["post_id"])
        
        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts
            
        return HttpResponseRedirect("/blog/")    
            
            
        #stored_posts.append(int(request.POST["post_id"]))     
           