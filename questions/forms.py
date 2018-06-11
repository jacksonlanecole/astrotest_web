from django.forms import ModelForm, TextInput, Select, BaseInlineFormSet
from .models import Course, Book, Chapter, Objective, Source, Question, Answer

class ChapterForm(ModelForm):
    chapter = forms.ModelChoiceField(
            queryset = Chapter.objects.all(),
            widget   = Select(attrs={'class': 'chapter'}),
            )

    class Meta:
        model = Question


class ObjectiveForm(ModelForm):
    objective = forms.ModelChoiceField(
        queryset=Objective.objects.all(),
        widget=Select(attrs={'class': 'objective'}),
    )

    class Meta:
        model = Question
        #fields = ('name', '')
        #widgets = {'name': TextInput(attrs={'class': 'name'})}


class BookForm(ModelForm):
    book = forms.ModelChoiceField(
            queryset = Objective.objects.all(),
            widget = Select(attrs={'class': 'book'}),
            )

    class Meta:
        model = Question


class SourceForm(ModelForm):
    source = forms.ModelChoiceField(
            queryset = Objective.objects.all(),
            widget = Select(attrs={'class': 'source'}),
            )

    class Meta:
        model = Question
