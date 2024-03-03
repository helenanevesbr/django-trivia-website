from django.db import models


class Question(models.Model):
    class Difficulty(models.TextChoices):  # Like an Enum
        EASY = "E"
        MEDIUM = "M"
        HARD = "H"

    text = models.CharField('question', max_length=255)
    details = models.TextField(blank=True)
    difficulty = models.CharField(
        max_length=1,                # Char fields require a max length
        choices=Difficulty.choices,  # Creates a dropdown in forms
        blank=True,                  # Not required. If empty, value is ''.
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ("pk",)                      # This is the default but can be overridden
        verbose_name = "Question"               # This is the default but can be overridden
        verbose_name_plural = "Quiz Questions"  # Shows up in admin navigation


class Choice(models.Model):
    question = models.ForeignKey(  # Define a many-to-one relationship
        Question,                  # There are many choices for every question
        on_delete=models.CASCADE,  # If you delete a question, delete its choices
        related_name="choices"     # Get choices via q.choices (default is q.choice_set)
    )
    text = models.TextField('choice')
    is_correct = models.BooleanField(default=False)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.text