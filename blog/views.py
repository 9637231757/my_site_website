from datetime import date
from django.shortcuts import render

# Create your views here.
all_posts = [
    {  
        "slug": "hike-in-the-mountains",  # This is a string for the post slug
        "image": "Mountains.jpg",  # This is a string for the image file name
        "author": "Rohan Gaidhani",  # This is a string for the author's name
        "date": date(2025, 3, 13),  # This is a datetime object, assuming you've imported `date` from `datetime`
        "title": "Mountain Hiking",  # This is a string for the title of the post
        "excerpt": "There's nothing like the views you get while hiking in the Mountains! And I wasn't even prepared for what happened while I was enjoying the view!",  # This is a string for the post excerpt
        "content": """Trekking in Maharashtra: A Journey Through the Western Ghats
            Maharashtra, a state located on the western coast of India, is blessed
            with a diverse landscape that offers a perfect escape for nature enthusiasts
            adventure seekers, and trekkers alike. Known for its rugged hills, lush green
            valleys, forts, waterfalls, and serene lakes, Maharashtra boasts some of the most
            captivating trekking destinations in India. Whether you're a seasoned trekker or a
            beginner, the state offers trails that cater to all levels of experience."""  # This is a multi-line string for the post content
    },


    
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2025, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
         
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2025, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
] 

def get_date(post):
    return post['date']

          
def starting_page(request):
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
    return render(request, "blog/post_detail.html")
    
    
