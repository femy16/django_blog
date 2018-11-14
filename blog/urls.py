from django.urls import path
from blog.views import show_blogs,read_posts,edit_posts,write_post,get_unpublished_posts

urlpatterns=[
    
    path('unpublished',get_unpublished_posts,name='get_unpublished_posts'),
    path('read_post/<int:id>',read_posts,name='read_posts'),
    path('edit_post/<int:id>',edit_posts,name='edit_posts'),
    # path('edit_post/<int:id>/publish/',publish_posts,name='edit_posts'),
    path('write_post/',write_post,name='write_post'),
    
    
    
    
    ]