from django.urls import path
from .views import (
    new_game,
    next_question,
    question_view,
    answer_view,
    complete
)

app_name = 'questions'

urlpatterns = [
    path("new/", view=new_game, name="new"),
    path("question/", view=next_question, name="question"),
    path("complete", view=complete, name="complete"),
    path("question/<int:pk>", view=question_view, name="question"),
    path("question/<int:question_pk>/choice/<int:choice_pk>", view=answer_view, name="answer"),
]

