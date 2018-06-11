from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course, Book, Chapter, Objective, Source, Question, Answer

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


class QuestionInline(admin.TabularInline):
    model = Question


class AnswerInline(admin.TabularInline):
    model = Answer
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
            'custom_objective',
            'course',
            'book',
            '_objective',
            '_number_of_questions',
            )
    list_filter = (
            'course',
            'custom_objective',
            'book',
            'chapter',
            'objective_number',
            )
    search_fields = (
            'objective_text',
            )
    inlines = [
            #QuestionInline,
            ]

    def _objective(self, obj):
        return obj.__str__()

    def _number_of_questions(self, obj):
        return obj.question_set.all().count()


class SourceAdmin(admin.ModelAdmin):
    list_display = (
            'name',
            '_number_of_questions',
            )
    list_filter = (
            'name',
            )
    inlines = [
            QuestionInline,
            ]
    fields = [
            'name',
            ]

    def _number_of_questions(self, obj):
        return obj.question_set.all().count()


class QuestionAdmin(admin.ModelAdmin):
    model = Question
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
            AnswerInline,
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

admin.site.register(
        Question,
        QuestionAdmin,
        )
###############################################################################
