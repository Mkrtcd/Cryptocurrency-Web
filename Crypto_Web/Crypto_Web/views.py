from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world! This is where everything starts!!!\n M.Lai 2022/03/05")

def homepage(request):
    return HttpResponse("This is supposed to be the homepage of our web!!!")    