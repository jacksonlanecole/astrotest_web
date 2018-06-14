from django.shortcuts import render
from .models import Question, Objective
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def question_list(request):
    #if request.method == 'POST':
    objectives = Objective.objects.all()
    #questions = Question.objects.all()
    return render(request, "questions/question_list.html",
            {"objectives":objectives})


@login_required
def questions_main(request):
    return render(request, "questions/questions.html")
