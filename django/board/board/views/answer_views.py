from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from board.models import Question, Answer
from board.forms import AnswerForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


@login_required(login_url="common:login")
def answer_create(request, qid):
    """답변등록"""
    question = get_object_or_404(Question, id=qid)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            # return redirect("board:question_detail", qid=qid)
            # detail 페에지의 특정 위치
            return redirect(
                "{}#answer_{}".format(
                    resolve_url("board:question_detail", qid=qid), answer.id
                )
            )
    else:
        form = AnswerForm()

    # answer = Answer.objects.create(question=question, content=request.POST.get("content"))

    # question.answer_set.create(content=request.POST.get("content"))

    # answer = Answer(question=question, content=request.POST.get("content"))
    # answer.save()

    # 실패시 get방식으로 처리
    context = {"question": question, "form": form}
    return render(request, "board/question_detail.html", context)


@login_required(login_url="common:login")
def answer_modify(request, aid):
    answer = get_object_or_404(Answer, id=aid)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modified_at = timezone.now()
            answer.save()
            # return redirect("board:question_detail", answer.question.id)
            return redirect(
                "{}#answer_{}".format(
                    resolve_url("board:question_detail", qid=answer.question.id),
                    answer.id,
                )
            )
    else:
        form = AnswerForm()
    return render(request, "board/answer_form.html", {"form": form})


@login_required(login_url="common:login")
def answer_delete(request, aid):

    answer = get_object_or_404(Answer, id=aid)
    answer.delete()
    # question id
    return redirect("board:question_detail", answer.question.id)
