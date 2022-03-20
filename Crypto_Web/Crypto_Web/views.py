from django.http import HttpResponse
from django.shortcuts import render
import psycopg2

app_name = "Crypto_web"

con = None
con = psycopg2.connect(database='user_info', user='postgres',
    password='19960926')

cur = con.cursor()
cur.execute('SELECT * FROM users')
version = cur.fetchall()
print(version)
con.close()
### Connecting db code 

#def hello(request):
#    return HttpResponse("Hello world! This is where everything starts!!!\n M.Lai 2022/03/05")

#def homepage_hidden(request):
#    context = {}
#    context['Homepage'] = 'Hello World!' 
#    return render(request, 'homepage.html', context)

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        print(username, password)
    return render(request, 'login.html')



