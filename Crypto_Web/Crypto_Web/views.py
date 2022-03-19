from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
app_name = "Crypto_web"


def hello(request):
    return HttpResponse("Hello world! This is where everything starts!!!\n M.Lai 2022/03/05")

def homepage_hidden(request):
    context = {}
    context['Homepage'] = 'Hello World!' 
    return render(request, 'homepage.html', context)

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        print(username, password)
    return render(request, 'login.html')

@csrf_exempt
def login_post(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get('password')
        print(username, password)
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')

