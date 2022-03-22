from django.http import HttpResponse
from django.shortcuts import render

app_name = "Crypto_web"


def hello(request):
    return HttpResponse("Hello world! This is where everything starts!!!\n M.Lai 2022/03/05")

def homepage_hidden(request):
    context = {}
    context['Homepage'] = 'Hello World!' 
    return render(request, 'homepage.html', context)

def login(request):
    return render(request, 'login.html')
def profile(request):
    return render(request, 'profile.html')
def signup(request):
    return render(request, 'signup.html')
def activity(request):
    return render(request, 'activity.html')
def activity(request):
    return render(request, 'forgot-password.html')
def activity(request):
    return render(request, 'recover-password.html')

