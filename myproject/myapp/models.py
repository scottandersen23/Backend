# Create your models here.
    
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# User Model
class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

# Blog Content
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    featured_image = models.ImageField(upload_to='posts/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Comments and Interactions
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    moderation_status = models.CharField(max_length=10, choices=[('approved', 'Approved'), ('pending', 'Pending'), ('spam', 'Spam')], default='pending')

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

class LikeDislike(models.Model):
    INTERACTION_CHOICES = [('like', 'Like'), ('dislike', 'Dislike')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='interactions')
    interaction_type = models.CharField(max_length=10, choices=INTERACTION_CHOICES)

    class Meta:
        unique_together = ('user', 'post')

# Media Management
class Media(models.Model):
    file = models.FileField(upload_to='media/')
    upload_date = models.DateTimeField(auto_now_add=True)
    associated_post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True, related_name='media')

# SEO and Metadata
class SEOData(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='seo_data')
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    canonical_url = models.URLField(blank=True, null=True)

# Analytics and Insights
class PageView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='page_views')
    view_date = models.DateTimeField(auto_now_add=True)
    visitor_ip = models.GenericIPAddressField()

# Monetization
class Advertisement(models.Model):
    ad_name = models.CharField(max_length=100)
    ad_placement = models.CharField(max_length=50)
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)

# Newsletter/Subscriptions
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscription_date = models.DateTimeField(auto_now_add=True)
    topics = models.ManyToManyField(Tag, blank=True)

# Site Configuration
class SiteConfiguration(models.Model):
    site_title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200, blank=True, null=True)
    timezone = models.CharField(max_length=50, default='UTC')
    default_language = models.CharField(max_length=10, default='en')

# Logs
class UserActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()