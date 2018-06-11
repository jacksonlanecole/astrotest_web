from django.shortcuts import render
from .models import Question
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def question_list(request):
    #if request.method == 'POST':
    questions = Question.objects.all()
    return render(request, "questions/question_list.html",
            {"questions":questions})


@login_required
def questions_main(request):
    return render(request, "questions/questions.html")
