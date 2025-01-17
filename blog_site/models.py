from django.db import models
from django.urls import reverse
from django.utils import timezone

STATUS_CHOICES={
    "draft":"Draft","published":"Published"
}


class publishedManager(models.Manager):
    def get_queryset(self):
        return super(publishedManager,self).get_queryset().filter(status="published")


class Post(models.Model):
    title=models.CharField(max_length=200,null=False)
    slug=models.SlugField(max_length=200,unique_for_date="publish")
    author=models.CharField(max_length=200,blank=False,null=False)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=100,choices=STATUS_CHOICES)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return f"{self.title}"

    objects=models.Manager()
    published=publishedManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug])





posts=Post.objects.filter(status='published')
p_posts=Post.published.all()

