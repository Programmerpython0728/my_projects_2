from django.contrib import admin
from .models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title",'slug','author','body',)
    list_filter = ('created','updated','status','author',)
    search_fields=('title','status')
    prepopulated_fields = {'slug':("title",)}
    raw_id_fields = ('author',)
    date_hierarchy = ('publish',)
    ordering=('satus',"publish")
