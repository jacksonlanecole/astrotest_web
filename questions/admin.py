from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (Course, Book, Chapter, Objective, Source,)
from .models import MultipleChoiceQuestion, MultipleChoiceAnswer
from .models import TrueFalseQuestion
from .models import QuestionBlock, QuestionBlockQuestion

# Register your models here.
###############################################################################
# INLINES
class CourseInline(admin.TabularInline):
    model = Course


class BookInline(admin.TabularInline):
    model = Book


class ChapterInline(admin.TabularInline):
    model = Chapter


class SourceInline(admin.TabularInline):
    model = Source


class ObjectiveInline(admin.TabularInline):
    model = Objective


class MultipleChoiceAnswerInline(admin.TabularInline):
    model = MultipleChoiceAnswer


class QuestionBlockQuestionInline(admin.TabularInline):
    model = QuestionBlockQuestion
###############################################################################

###############################################################################
# CUSTOM ADMIN
class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = (
            'title',
            'course_code',
            'university',
            )
    list_filter = (
            'university',
            )
    search_fields = [
            'university',
            'course_code',
            'title',
            ]
    inlines = [
            #BookInline,
            ]
    fields = [
            'university',
            'course_code',
            'title',
            ]


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = (
            'title',
            'author_last_name',
            'author_first_name',
            'publisher',
            'year',
            'course',
            )
    list_filter = (
            'course',
            'publisher',
            'year',
            )
    search_fields = (
            'title',
            'author_last_name',
            'course'
            )
    inlines = [
            #ChapterInline,
            ]
    fields = [
            'title',
            'author_last_name',
            'author_first_name',
            'publisher',
            'year',
            'course',
            ]


class ChapterAdmin(admin.ModelAdmin):
    model = Chapter
    list_display = (
            'title',
            'number',
            'book',
            )
    inlines = [
            #ObjectiveInline,
            ]
    list_filter = (
            'course',
            'book',
            )
    search_fields = (
            'title',
            )


class ObjectiveAdmin(admin.ModelAdmin):
    model = Objective
    list_display = (
            '_objective',
            'custom_objective',
            'course',
            'book',
            '_total_questions',
            '_multiple_choice_questions',
            '_TF_questions',
            )
    list_filter = (
            'course',
            'custom_objective',
            'book',
            )
    search_fields = (
            'objective_text',
            )
    inlines = [
            #QuestionInline,
            ]

    def _objective(self, obj):
        return obj.__str__()

    def _total_questions(self, obj):
        return (obj.multiplechoicequestion_set.all().count()
                + obj.truefalsequestion_set.all().count())

    def _multiple_choice_questions(self, obj):
        return obj.multiplechoicequestion_set.all().count()


    def _TF_questions(self, obj):
        return obj.multiplechoicequestion_set.all().count()


class SourceAdmin(admin.ModelAdmin):
    list_display = (
            'name',
            '_number_of_questions',
            )
    list_filter = (
            'name',
            )
    inlines = [
            #QuestionInline,
            ]
    fields = [
            'name',
            ]

    def _number_of_questions(self, obj):
        return obj.question_set.all().count()


class MultipleChoiceQuestionAdmin(admin.ModelAdmin):
    model = MultipleChoiceQuestion
    list_display = (
            'question_text',
            'objective',
            'difficulty',
            'created_date',
            )
    list_filter = [
            'objective',
            'difficulty',
            'scrambleable',
            'created_date',
            ]
    search_fields = (
            'question_text',
            'objective',
            )
    inlines = [
            MultipleChoiceAnswerInline,
            ]
    fields = [
            'course',
            'book',
            'chapter',
            'objective',
            'question_text',
            'scrambleable',
            'difficulty',
            'source',
            'index',
            ]


class TrueFalseQuestionAdmin(admin.ModelAdmin):
    model = TrueFalseQuestion
    list_display = (
            'question_text',
            'objective',
            'difficulty',
            'created_date',
            )
    list_filter = [
            'course',
            'book',
            'objective',
            'difficulty',
            'created_date',
            ]
    search_fields = (
            'question_text',
            'objective',
            )
    inlines = [
            ]
    fields = [
            'course',
            'book',
            'chapter',
            'objective',
            'question_text',
            'answer',
            'difficulty',
            'source',
            'index',
            ]


class QuestionBlockAdmin(admin.ModelAdmin):
    model = QuestionBlockQuestion
    list_display = (
            'question_text',
            'objective',
            '_number_of_questions',
            )
    list_filter = [
            'course',
            'book',
            'objective',
            'difficulty',
            ]
    search_fields = (
            'question_text',
            'objective',
            )
    inlines = [
            QuestionBlockQuestionInline,
            ]
    fields = [
            'course',
            'book',
            'chapter',
            'objective',
            'question_text',
            'index',
            ]

    def _number_of_questions(self, obj):
        return obj.questionblockquestion_set.all().count()
###############################################################################

###############################################################################
# REGISTRATION
admin.site.register(
        Course,
        CourseAdmin,
        )

admin.site.register(
        Book,
        BookAdmin,
        )

admin.site.register(
        Chapter,
        ChapterAdmin,
        )

admin.site.register(
        Source,
        SourceAdmin,
        )

admin.site.register(
        Objective,
        ObjectiveAdmin,
        )
########################################
## QUESTIONS
admin.site.register(
        MultipleChoiceQuestion,
        MultipleChoiceQuestionAdmin,
        )

admin.site.register(
        TrueFalseQuestion,
        TrueFalseQuestionAdmin,
        )

admin.site.register(
        QuestionBlock,
        QuestionBlockAdmin,
        )
########################################
###############################################################################
