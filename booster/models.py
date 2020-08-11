from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


 

class Post(models.Model):
        STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
        CATE=(
                ('education', 'education'),
        )
        title = models.CharField(max_length=250)
        slug = models.SlugField(max_length=250,unique_for_date='publish')
        cate = models.CharField(max_length=100,        choices=CATE   )
                
        
        author = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='blog_posts')
        body = models.TextField()
        image=models.ImageField( upload_to="image", height_field=None, width_field=None, max_length=None)
        publish = models.DateTimeField(default=timezone.now)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        status = models.CharField(max_length=10,        choices=STATUS_CHOICES,        default='draft')
        tags = TaggableManager()
        def get_absolute_url(self):
                return reverse('booster:detail', args=[self.id ,self.slug])      
       
        class Meta:
                ordering = ('-publish',)
                def __str__(self):
                        return self.title

       
  


class Blogdes(models.Model):        
        post=models.ForeignKey(Post,  on_delete=models.CASCADE)
        sub_title=models.CharField( max_length=250)
        description=models.TextField()
        image= models.ImageField( upload_to="image", height_field=None, width_field=None, max_length=None)


class  comment(models.Model):        
        postid=models.IntegerField()       
        body=models.CharField(max_length=250)
        name=models.CharField( max_length=150)
        email=models.EmailField( max_length=254)
        Date=models.DateTimeField( auto_now=True, auto_now_add=False)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        def __str__(self):
            return self.body
 


class suscriberr(models.Model):
        email=models.EmailField( max_length=254)
        name=models.CharField( max_length=150)

class contact(models.Model):
    name=models.CharField( max_length=50)
    company=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    message=models.TextField()
   
    def __str__(self):
        return self.name

    
    
