from django.urls import path
from . import views
from .views import PostListView, post_detail
app_name="blog_site"
urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
]
