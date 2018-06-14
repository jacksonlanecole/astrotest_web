from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey

from polymorphic.models import PolymorphicModel

# Create your models here.
class Course(models.Model):
    """
    """
    ###########################################################################
    # FIELDS
    university = models.CharField(
            max_length=140,
            help_text="Where is this course being taught?",
            )
    course_code = models.CharField(
            max_length= 10,
            help_text="Enter the course code."
            )
    title = models.CharField(
            max_length=140,
            help_text="Enter the title of the course.",
            )
    ###########################################################################

    def __str__(self):
        return "(" + self.course_code + ") " + self.title

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"


class Book(models.Model):
    """
    """
    ###########################################################################
    # FOREIGNKEYS
    course = models.ForeignKey(
            Course,
            blank=False,
            null=False,
            help_text="In which course is this book used?",
            on_delete=models.PROTECT,
            )
    ###########################################################################

    ###########################################################################
    # FIELDS
    title = models.CharField(
            max_length=140,
            help_text="Enter the book title.",
            )

    author_first_name = models.CharField(
            max_length=140,
            help_text="Enter the first author's first name.",
            )

    author_last_name = models.CharField(
            max_length=140,
            help_text="Enter the first author's last name.",
            )

    publisher = models.CharField(
            max_length=140,
            help_text="(OPTIONAL) Enter the book publisher.",
            null=True,
            blank=True,
            )

    year = models.CharField(
            max_length=4,
            help_text="(OPTIONAL) Enter the published year.",
            null=True,
            blank=True,
            )
    ###########################################################################

    def __str__(self):
        return self.author_last_name + ", " + self.author_first_name + ": "\
                + self.title

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"



class Chapter(models.Model):
    """
    """
    ###########################################################################
    # FOREIGNKEYS
    course = models.ForeignKey(
            Course,
            help_text="Select a course from those listed.",
            on_delete=models.PROTECT,
            null=True, #DELETE IN PRODUCTION
            )
    book = ChainedForeignKey(
            Book,
            help_text="Select a book from those listed.",
            # BEGIN CHAIN
            chained_field='course',
            chained_model_field='course',
            show_all=False,
            auto_choose=True,
            sort=True,
            # END CHAIN
            on_delete=models.PROTECT,
            null=False,
            blank=False,
            )
    ###########################################################################

    ###########################################################################
    # FIELDS
    number = models.PositiveSmallIntegerField()
    title = models.CharField(
            max_length=400,
            )
    ###########################################################################

    def __str__(self):
        return "(" + str(self.number) + ") " + self.title

    class Meta:
        ordering = ['number']
        verbose_name = "chapter"
        verbose_name_plural = "chapters"


class Objective(models.Model):
    """
    """
    ###########################################################################
    # CHAINEDFOREIGNKEYS
    course = models.ForeignKey(
            Course,
            on_delete=models.PROTECT,
            null=True, #DELETE IN PRODUCTION
            )
    book = ChainedForeignKey(
            Book,
            help_text="Select a book from those listed.",
            # BEGIN CHAIN
            chained_field='course',
            chained_model_field='course',
            show_all=False,
            auto_choose=True,
            sort=True,
            # END CHAIN
            on_delete=models.PROTECT,
            null=True,
            blank=True,
            )
    chapter = ChainedForeignKey(
            Chapter,
            help_text="Select a book those listed above.",
            # BEGIN CHAIN
            chained_field="book",
            chained_model_field="book",
            show_all=False,
            auto_choose=True,
            sort=True,
            # END CHAIN
            on_delete=models.PROTECT,
            null=True,
            blank=True,
            default=0,
            )
    ###########################################################################

    ###########################################################################
    # FIELDS
    custom_objective = models.BooleanField(
            default=False,
            help_text="Is this question a custom objective (i.e. it is "\
            "not aligned with any book objectives)?",
            )
    objective_number = models.PositiveSmallIntegerField(
            null=True,
            blank=True,
            verbose_name = "objective number",
            )
    objective_text = models.CharField(
            max_length=400,
            )
    ###########################################################################

    def __str__(self):
        """The logic here just returns a different string based on the
        question belonging to a custom objective or not.
        """
        if self.custom_objective == True:
            return "(CO) " + self.objective_text
        elif self.book == None:
            return "(" + str(self.chapter.number) + "." \
                   + str(self.objective_number) + ")" + " " \
                   + "(...) " \
                   + self.objective_text
        else:
            return "(" + str(self.chapter.number) + "." \
                   + str(self.objective_number) + ")" + " " \
                   + "(" + (self.book.title)[:25] + "...) " \
                   + self.objective_text

    class Meta:
        ordering = [
                'chapter',
                'objective_number',
                ]
        verbose_name = "objective"
        verbose_name_plural = "objectives"


class Source(models.Model):
    """
    """
    ###########################################################################
    # FIELDS
    name = models.CharField(
            max_length=30,
            help_text="Enter the name of a new source. (e.g. book, " \
            "testbank, homework, clicker, etc.)",
            unique = True,
            verbose_name = "source name",
            )
    ###########################################################################
    def __str__(self):
        return self.name

    class Meta:
        ordering = [
                'name',
                ]
        verbose_name = "source"
        verbose_name_plural = "sources"


class Question(PolymorphicModel):
    """
    """
    ###########################################################################
    # FOREIGNKEYS
    course = models.ForeignKey(
            Course,
            on_delete=models.PROTECT,
            null=True,
            blank=True,
            )
    source = models.ForeignKey(
            Source,
            on_delete=models.PROTECT,
            )
    #book = ChainedForeignKey(
    #        Book,
    #        help_text="Select a book from above.",
    #        # BEGIN CHAIN
    #        chained_field='course',
    #        chained_model_field='course',
    #        show_all=False,
    #        auto_choose=True,
    #        sort=True,
    #        # END CHAIN
    #        on_delete=models.PROTECT,
    #        null=True,
    #        blank=True,
    #        )
    #chapter = ChainedForeignKey(
    #        Chapter,
    #        help_text="Select a chapter from above.",
    #        # BEGIN CHAIN
    #        chained_field='book',
    #        chained_model_field='book',
    #        show_all=False,
    #        auto_choose=True,
    #        sort=True,
    #        # END CHAIN
    #        on_delete=models.PROTECT,
    #        null=True,
    #        blank=True,
    #        )
    objective = ChainedForeignKey(
            Objective,
            help_text="(REQUIRED) Select an objective. If your objective is "\
                    "a custom objective, those will be prefixed by (CO).",
            # BEGIN CHAIN
            chained_field='course',
            chained_model_field='course',
            show_all=True,
            auto_choose=True,
            sort=True,
            # END CHAIN
            on_delete=models.PROTECT,
            null=False,
            blank=False,
            )
    ###########################################################################

    ###########################################################################
    # FIELDS
    question_text = models.TextField(
            help_text="Enter the question here! LaTeX formatting is "\
            "accepted... It's just going to be turned into LaTeX "\
            "anyways!",
            unique = True,
            )
    image = models.ImageField(
            help_text="",
            null=True,
            blank=True,
            )
    DIFFICULTY_CHOICES = (
            (1, '1 (Easy)'),
            (2, '2 (Moderate)'),
            (3, '3 (Difficult)'),
            )
    difficulty = models.PositiveSmallIntegerField(
            choices=DIFFICULTY_CHOICES,
            default=1,
            )
    index = models.PositiveSmallIntegerField(
            default=50,
            blank=True,
            null=True,
            help_text="I'm not really sure why this is needed...",
            )
    created_date = models.DateField(
            auto_now=True,
            )
    ###########################################################################

    def __str__(self):
        return self.question_text

    class Meta:
        abstract = False
        verbose_name = "question"
        verbose_name_plural = "questions"


class MultipleChoiceQuestion(Question):
    question_type = "MC"
    scrambleable = models.BooleanField(
            help_text="(REQUIRED) Select this box if the order of the answers in "\
            "the question does not matter.",
            null=False,
            blank=False,
            )

    class Meta:
        verbose_name = "multiple choice question"
        verbose_name_plural = "multiple choice questions"


class MultipleChoiceAnswer(models.Model):
    """
    """
    ###########################################################################
    # FOREIGNKEYS
    question = models.ForeignKey(
            MultipleChoiceQuestion,
            on_delete=models.PROTECT,
            related_name='answers',
            )
    ###########################################################################

    ###########################################################################
    # FIELDS
    answer_text = models.CharField(
            max_length=255,
            )
    correct = models.BooleanField(
            'Correct answer',
            default=False,
            )
    ###########################################################################

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"


class TrueFalseQuestion(Question):
    question_type = "TF"
    answer = models.NullBooleanField(
            help_text="Select box if True, leave unselected if false.",
            )

    class Meta:
        verbose_name = "True/False question"
        verbose_name_plural = "True/False questions"



class QuestionBlock(Question):

    class Meta:
        verbose_name = "question block"
        verbose_name_plural = "question blocks"


class QuestionBlockQuestion(models.Model):
    """
    """
    ###########################################################################
    # FOREIGNKEYS
    master_question = models.ForeignKey(
            QuestionBlock,
            on_delete=models.PROTECT,
            null=False,
            blank=False,
            )
    ###########################################################################

    ###########################################################################
    # FIELDS
    question_text = models.TextField(
            help_text="Enter the question here! LaTeX formatting is "\
            "accepted... It's just going to be turned into LaTeX "\
            "anyways!",
            unique = True,
            )
    image = models.ImageField(
            help_text="",
            null=True,
            blank=True,
            )
    DIFFICULTY_CHOICES = (
            (1, '1 (Easy)'),
            (2, '2 (Moderate)'),
            (3, '3 (Difficult)'),
            )
    difficulty = models.PositiveSmallIntegerField(
            choices=DIFFICULTY_CHOICES,
            default=1,
            )
    created_date = models.DateField(
            auto_now=True,
            )
    ###########################################################################

    def __str__(self):
        return self.question_text

    class Meta:
        abstract = True
        verbose_name = "question block question"
        verbose_name_plural = "question block questions"

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = "question block: question"
        verbose_name_plural = "question block: questions"


class QuestionBlockQuestionAnswer(models.Model):
    ###########################################################################
    # FOREIGNKEYS
    question_block_question = models.ForeignKey(
            QuestionBlockQuestion,
            on_delete=models.PROTECT,
            null=False,
            blank=True,
            )
    ###########################################################################

    ###########################################################################
    # FIELDS
    answer_text = models.CharField(
            max_length=255,
            )
    correct = models.BooleanField(
            'Correct answer',
            default=False,
            )
    ###########################################################################

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"

