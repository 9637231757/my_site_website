"""from datetime import date
from django.shortcuts import render
from .models import post

# Create your views here.
all_posts = [
] 

def get_date(post):
    return post['date']

          
def starting_page(request):
    latest_post = post.objects.all().order_by("-date")[:3]
    sorted_posts = sorted(all_posts, key= get_date) 
    latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts": latest_posts
        
    })
     
    
def posts(request):
    return render(request,"blog/all-posts.html", {
        "all_posts": all_posts
    } )



def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post_detail.html",{
        "post":"identified_post"
    }) """
    

# views.py
from django.shortcuts import render
from .models import Post  # Use 'Post' instead of 'post'

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })
    
def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = Post.objects.get(slug=slug)
    return render(request, "blog/post_detail.html", {
        "post": identified_post  # Fixed the string literal issue too
    })