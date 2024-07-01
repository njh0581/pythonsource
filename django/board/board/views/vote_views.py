from django.shortcuts import get_object_or_404, redirect
from board.models import Question, Answer
from django.contrib import messages


def vote_question(request, qid):
    question = get_object_or_404(Question, id=qid)

    # 내가 작성한 글은 추철 못함
    if question.author == request.user:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        question.voter.add(request.user)
    return redirect("board:question_detail", qid)


def vote_answer(request, aid):
    answer = get_object_or_404(Answer, id=aid)

    if answer.author == request.user:
        messages.error(request, "본인이 작성한 답변은 추천할 수 없습니다.")
    else:
        answer.voter.add(request.user)
    return redirect("board:question_detail", answer.question.id)
