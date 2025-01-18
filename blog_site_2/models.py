from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES={
        "draft":"Draft","published":'published',
    }
    title=models.CharField(max_length=200,blank=False,null=False)
    slug=models.SlugField(max_length=200,null=False,blank=filter)
    author=models.CharField(max_length=200,null=False,blank=False)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=200,choices=STATUS_CHOICES)
    class Meta:
        ordering=("-publish",)

    def __str__(self):
        return f"{self.title},{self.status}"


    objects=models.Manager()
    published=PublishedManager()

    def get_absolute_url(self):
        return  reverse("blog:post_detail", args=[self.publish.year,
                                                 self.publish.month,
                                                 self.publish.day,
                                                 self.slug])
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


posts=Post.objects.filter(satus='published')
p_posts=Post.published.all()
