from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentsForm
from django.utils import timezone


# Create your views here.
def getposts(request):
   posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
   return render(request, "blogposts.html", {'posts': posts})
   
def add_post(request):
  if request.method == "POST":
      form = PostForm(request.POST, request.FILES)
      if form.is_valid():
          post = form.save(commit=False)
          post.author = request.user
          post.created_date = timezone.now()
          post.save()
          return redirect(viewpost, post.pk)
  else:
      # GET Request so just give them a blank form
      form = PostForm()    
   
  return render(request, "postform.html", { 'form': form })
  
# def viewpost(request, id):
#     post = get_object_or_404(Post, pk=id)
#     post.views += 1 # clock up the number of post views
#     post.save()
#     return render(request, "viewpost.html", {'post': post})


def editpost(request, id):
    post = get_object_or_404(Post, pk=id)
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(getposts)
        
    else:
        form = PostForm(instance=post)
    
    form = PostForm(instance = post)
    return render(request, "postform.html", { 'form': form})
    
def viewpost(request, id):
    this_post = get_object_or_404(Post, pk=id)
    comments = Comment.objects.filter(post=this_post)
    form = CommentsForm()
    return render(request, "viewpost.html", {'post': this_post, 'comments': comments, 'form': form})
    
# def addcomment(request, post_id):
    # post = get_object_or_404(Post, pk=post_id)
    # form = CommentsForm(request.POST)
    
    # if form.is_valid():
    #     comment = form.save(commit=False)
    #     comment.author = request.user
    #     comment.post = post
    #     comment.save()
def addcomment(request):
    return redirect('index')
        
 
 
