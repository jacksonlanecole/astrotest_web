from django.db import models
from smart_selects.db_fields import ChainedManyToManyField


from questions.models import (
        Course,
        Objective,
        Question,
        MultipleChoiceQuestion,
        TrueFalseQuestion,
        QuestionBlock,
        )

# Create your models here.

class MasterExam(models.Model):
    course = models.ForeignKey(
            Course,
            on_delete=models.PROTECT,
            null=False,
            blank=False,
            )
    objectives = ChainedManyToManyField(
            Objective,
            chained_field='course',
            chained_model_field='course',
            horizontal=True,
            )
    multiple_choice_questions = ChainedManyToManyField(
            MultipleChoiceQuestion,
            chained_field='objectives',
            chained_model_field='objective',
            horizontal=True,
            )
    true_false_questions = ChainedManyToManyField(
            TrueFalseQuestion,
            chained_field='objectives',
            chained_model_field='objective',
            horizontal=True,
            )
    question_block_questions = ChainedManyToManyField(
            QuestionBlock,
            chained_field='objectives',
            chained_model_field='objective',
            horizontal=True,
            )


    def __str__(self):
        return self.course.title


    class Meta:
        verbose_name = 'exam'
        verbose_name_plural = 'exams'
