from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


options = (
    ('draft', 'Draft'),
    ('published', 'Published')
)

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):   # another model
    
    class PostObjects(models.Manager):  # instead of Objects.all() it shows the data of published one.
        def get_queryset(self):
            return super().get_queryset().filter(status='published')    
        
        
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1
    )   # published will be automatically assigned to the default category 
    
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )   # CASCADE = it deletes the post if the user is deleted
    status = models.CharField(
        max_length=10, choices=options, default='published'
    )   # options to choose it to post right away or draft instead
    
    objects = models.Manager()  # defaut manager
    post_objects = PostObjects()    # custom manager
    
    class Meta:
        ordering = ('-published',)  # data returned descending in order
    
    def __str__(self):
        return self.title