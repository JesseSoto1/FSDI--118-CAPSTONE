from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, CommentForm


# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')

    context = {
        'posts': posts
    }

    return render(request, 'posts/post_list.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author =request.user
            comment.save()

            return redirect("post_detail", pk=post.pk)
        else:
            form = CommentForm()

    # context = {
    #     'post': post
    # }

    return render(request, 'posts/post_detail.html',{"post":post, "form":form,})



def home(request):
    posts = Post.objects.filter(author = request.user)

    context = {
        'posts': posts
    }

    return render(request,'posts/home.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')

    else:
        form = PostForm()

        return render(request, 'posts/create_post.html', {'form': form})
