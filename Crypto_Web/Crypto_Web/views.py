from django.http import HttpResponse
from django.shortcuts import render
import psycopg2

app_name = "Crypto_web"


#def hello(request):
#    return HttpResponse("Hello world! This is where everything starts!!!\n M.Lai 2022/03/05")

#def homepage_hidden(request):
#    context = {}
#    context['Homepage'] = 'Hello World!' 
#    return render(request, 'homepage.html', context)


def login(request):
    print("================================")
    if request.method == "POST":
        print('a')
        username = request.POST.get("email")
        password = request.POST.get('password')
        print(username, password)
    return render(request, 'login.html')


#def login(request):
    
#    email = request.POST.get('email')
#    password = request.POST.get('password')
#    print(email, password)
#
#    conn = psycopg2.connect(database="user_info", user="postgres", password="19960926", host="localhost")
#    cur = conn.cursor()
#    cur.execute("select * from users")
#    rows = cur.fetchall()
#    print(rows)
#    conn.commit()
#    conn.close()
#    return render(request, 'login.html')





def profile(request):
    return render(request, 'profile.html')
def signup(request):
    return render(request, 'signup.html')
def activity(request):
    return render(request, 'activity.html')
def forgotPassword(request):
    return render(request, 'forgot-password.html')
def recoverPassword(request):
    return render(request, 'recover-password.html')
def correctPassword(request):
    return render(request, 'correct-password.html')
def wrongPassword(request):
    return render(request, 'wrong-password.html')
