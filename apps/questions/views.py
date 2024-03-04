from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponse
from .models import(
    Question,
    Choice
)

def question_view(request,pk):
    question = get_object_or_404(Question, pk=pk)
    context = {"question": question}
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