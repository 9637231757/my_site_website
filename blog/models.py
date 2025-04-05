"""from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

class post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now = True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts",null=True, blank=True)  """
# updated models.py file     
from django.db import models
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

class Post(models.Model):  # Capitalized
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    # Consider using ImageField if storing actual images:
    image = models.ImageField(upload_to='uploads/posts/', null=True, blank=True)
    #image = models.ImageField(upload_to="posts",null=True)
    date = models.DateField(auto_now_add=True)  # Changed to auto_now_add
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, 
        on_delete=models.SET_NULL, 
        related_name="posts",
        null=True, 
        blank=True
    )
    tags = models.ManyToManyField(Tag, blank=True)  # Added relationship
    
    def __str__(self):
        return f"{self.title} ({self.date})"

    class Meta:
        ordering = ['-date']  # Default ordering by date descending    

class comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commets")         