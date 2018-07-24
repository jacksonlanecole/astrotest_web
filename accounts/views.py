from django.shortcuts import render, redirect
from django.template import RequestContext
#from django.contrib.auth.forms import UserCreationForm
from .models import User
from .admin import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, "accounts/index.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password1']
            user = authenticate(request, email = email, password = password)
            login(request, user)
            return redirect('/')

    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, "registration/register.html", context)


def login_user(request):
    logout(request)
    email = password = ''
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')

    return render(request, 'registration/login.html',)
