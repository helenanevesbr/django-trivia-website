from django.urls import path
from .views import (
    new_game,
    next_question,
    question_view
)

app_name = 'questions'

urlpatterns = [
    path("new/", view=new_game, name="new"),
    path("question/", view=next_question, name="question"),
    path("question/<int:pk>", view=question_view, name="question")
]