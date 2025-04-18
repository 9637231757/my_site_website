
from django.urls import path
#from blog.views import ReadLaterView
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>/", views.SinglePostsView.as_view(), name="post-detail-page"),
    path("read-later/", views.ReadLaterView.as_view(), name="read-later")
] 

