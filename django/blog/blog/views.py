from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from .models import Post, Comment
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

from django.core.paginator import Paginator
from django.http import JsonResponse


def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # if post.user == request.user:
    #     messages.error(request, "본인이 작성한 글은 추천할수 없습니다")
    # else:
    is_liked = post.likes.filter(id=request.user.id).exists()
    is_liked_change = False
    if is_liked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        is_liked_change = True
    return JsonResponse({"likes": post.likes.count(), "is_liked": is_liked_change})


@login_required(login_url="common:login")
def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        content = request.POST.get("content").strip()

        # comment = Comment.objects.create(user=request.user,post=post,content=content)
        comment = Comment(user=request.user, post=post, content=content)
        comment.save()
        return redirect("blog:detail", post_id)
    return redirect("blog:detail", post_id)


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
            # 태그 저장
            form.save_m2m()
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
    is_liked = False
    # 로그인 유저가 해당 게시물에 좋아요 했는지 여부
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    context = {"post": post, "is_liked": is_liked}
    return render(request, "blog/post.html", context)
