from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,permission_required
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
# def hello(request):
#     return render(request,"blog/get_index.html")
def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


def user_can_edit_post(request, post):
    wrote_the_post = post.author == request.user
    is_editor = is_in_group(request.user, 'editors')
    superuser = request.user.is_superuser
    return wrote_the_post or superuser or is_editor
    
def show_blogs(request):
    posts = Post.objects.filter(published_date__lte= timezone.now())
    print(posts)
    return render(request, "blog/get_index.html", {'posts': posts})
def read_posts(request,id):
    
    post=Post.objects.get(pk=id)
    post.views+=1
    post.save()
    can_edit = user_can_edit_post(request, post)
    # is_editor=request.user.groups.filter(name='editors').exists()
    # can_edit=post.author==request.user or request.user.is_superuser or is_editor
    can_publish=is_in_group(request.user,'publishers')
    return render(request, "blog/read_post.html", {'post': post, 'can_edit':can_edit,'can_publish':can_publish})


@login_required
def write_post(request):
    if request.method=="POST":
         form = PostForm(request.POST,request.FILES)
         post=form.save(commit=False)
         post.author=request.user
         post.save()
         return redirect(read_posts,post.id)
    else:
        form=PostForm()
        return render(request,"blog/post_form.html",{'form':form})
def edit_posts(request,id):
    post=Post.objects.get(pk=id)
    if request.method=="POST":
         form = PostForm(request.POST,request.FILES, instance=post)
         form.save()
         return redirect("/read_post/{0}".format(id))
    else:
        form=PostForm(instance=post)
        return render(request,"blog/post_form.html",{'form':form})
        
def get_unpublished_posts(required,id):
    posts=Post.objects.filter(published_date__gte=timezone.now())
    return render(request,"blog/get_index.html",{'posts':posts})
    
@permission_required('blog.can_publish')
def publish_post(request, id):
   post = get_object_or_404(Post , pk=id)
   post.published_date = timezone.now()
   post.save()
   return redirect(read_post, post.id)
        
        
        