from django.contrib import admin

from .models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','slug','publish','created','updated')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('author','body','title')
    prepopulated_fields = {"slug":("title",)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

