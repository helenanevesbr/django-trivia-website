from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponse
from .models import(
    Question,
    Choice
)

def question_view(request,pk):
    question = get_object_or_404(Question, pk=pk)
    context = {"question": question}
    request.session['last_question_pk'] = pk
    return render(request, "questions/question.html", context=context)


def new_game(request):
    request.session['last_question_pk'] = 0
    request.session['correct'] = 0
    request.session['total'] = Question.objects.count()

    return redirect('questions:question')


def next_question(request):
    last_pk = request.session.get('last_question_pk', 0)

    question = Question.objects.filter(pk__gt=last_pk).first()
    if question:
        return redirect('questions:question', pk=question.pk)
    else:
        return redirect('questions:complete')
    

def answer_view(request, question_pk, choice_pk):
    question = get_object_or_404(Question, pk=question_pk)
    choice = get_object_or_404(Choice, question=question, pk=choice_pk)
    context = {"question": question, "selected_choice": choice}

    if choice.is_correct:
        request.session['correct'] += 1

    return render(request, "questions/answer.html", context=context)


def complete(request):
    context = {
        "correct": request.session.get('correct', 0),
        "total": request.session.get('total', 0)
    }
    return render(request, "questions/complete.html", context=context)

