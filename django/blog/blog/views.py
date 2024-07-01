from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from django.core.paginator import Paginator


@login_required(login_url="common:login")
def create(request):
    if request.method == "POST":
        # 폼에 post로 넘어오는 내용 담기
        # 이미지 담기 request.FILES
        form = PostForm(request.POST, request.FILES)
        # 폼 유효성 검증
        # 유효성 통과 하면 저장
        # 리스트로 이동
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("blog:list")
    else:
        form = PostForm()
    return render(request, "blog/create.html", {"form": form})


# @login_required(login_url="common:login")
def modify(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save
            post = form.save(commit=False)
            # post.modified_at = timezone.now()
            post.user = request.user
            post.save()
            return redirect("blog:detail", post.id)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/modify.html", {"form": form, "post": post})


def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect("blog:list")


def list(request):
    # Post 전체 조회
    page = request.GET.get("page", 1)
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(page)
    context = {"posts": page_obj, "page": page}
    return render(request, "blog/list.html", context)


def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {"post": post}
    return render(request, "blog/post.html", context)
