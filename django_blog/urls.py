"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from accounts.views import signup
from django.contrib import admin
from django.urls import path,include
from blog.views import show_blogs,read_posts,edit_posts,write_post,get_unpublished_posts
from django.views.static import serve
from django.conf import settings
from blog import urls as blog_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',hello),
    path('accounts/',include('django.contrib.auth.urls')),
    
    path('',show_blogs,name='show_blogs'),
    path('post/',include(blog_urls)),
    path('signup/', signup, name='signup'),
    path('media/<path:path>',serve,{'document_root':settings.MEDIA_ROOT}),
    
]
