from django.db import models

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Таймер на ответ")
    required_score_to_pass = models.IntegerField(help_text="Необходимое количество правильных ответов")

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        return self.question_set.all()[:self.number_of_questions]

    class Meta:
        verbose_name = "Викторины"