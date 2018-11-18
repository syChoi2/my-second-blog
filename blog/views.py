from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .models import TheqooInfoList
from .crawling import Crawling
from django.utils import timezone
from .form import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html',{'posts':posts})
    # render(요청, template, 매개변수)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'blog/post_detail.html', {'post' : post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail",post_id=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})


def post_edit(request, post_id):
    post = get_object_or_404(Post,pk = post_id)
    if request.method =="POST":
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail",post_id = post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html',{'form':form})	


def theqoo_list(request, page_num):
    url = "https://theqoo.net/hot?filter_mode=normal"
    ex = Crawling(url)
    html = ex.get_html(url)
    # ex.parse_html(html)
    # info_list = TheqooInfoList.objects
    info_list = ex.parse_html(html)
    return render(request, 'blog/theqoo_list.html', {'info_list': info_list})

