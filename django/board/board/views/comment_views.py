from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from board.models import Question, Answer, Comment
from board.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages


@login_required(login_url="common:login")
def comment_create_question(request, qid):
    question = get_object_or_404(Question, id=qid)
    if request.method == "POST":
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.question = question
        comment.author = request.user
        comment.save()
        # return redirect("board:question_detail", qid)
        return redirect(
            "{}#comment_{}".format(
                resolve_url("board:question_detail", qid),
                comment.id,
            )
        )
    else:
        form = CommentForm()
    return render(request, "board/comment_form.html", {"form": form})


def comment_modify_question(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.modified_at = timezone.now()
            comment.save()
            # return redirect("board:question_detail", comment.question.id)
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:question_detail", comment.question.id),
                    comment.id,
                )
            )
    else:
        form = CommentForm()
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="common:login")
def comment_delete_question(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    comment.delete()
    return redirect("board:question_detail", comment.question.id)


@login_required(login_url="common:login")
def comment_create_answer(request, aid):
    answer = get_object_or_404(Answer, id=aid)
    if request.method == "POST":
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.answer = answer
        comment.author = request.user
        comment.save()
        # return redirect("board:question_detail", answer.question.id)
        return redirect(
            "{}#comment_{}".format(
                resolve_url("board:question_detail", answer.question.id),
                comment.id,
            )
        )
    else:
        form = CommentForm()
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="common:login")
def comment_modify_answer(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.modified_at = timezone.now()
            comment.save()
            # return redirect("board:question_detail", comment.answer.question.id)
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:question_detail", comment.answer.question.id),
                    comment.id,
                )
            )
    else:
        form = CommentForm()
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="common:login")
def comment_delete_answer(request, cid):
    comment = get_object_or_404(Comment, id=cid)
    comment.delete()
    return redirect("board:question_detail", comment.answer.question.id)


def vote_question(request, qid):
    question = get_object_or_404(Question, id=qid)

    # 내가 작성한 글은 추철 못함
    if question.author == request.user:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        question.voter.add(request.user)
    return redirect("board:question_detail", qid)
