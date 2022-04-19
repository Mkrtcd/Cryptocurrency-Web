import email
from django.http import HttpResponse
from django.shortcuts import render
import psycopg2

app_name = "Crypto_web"

def login(request):
    print("================================")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get('password')
        print(email, password)
    try:
        conn = psycopg2.connect(database="Crypto_app", user="hzha3299", 
                        password="Cs981020", host="cryptodatabase.ccftjy90se8y.ap-southeast-2.rds.amazonaws.com")
        cur = conn.cursor()
        postgres_select_query = ("SELECT * FROM users WHERE email = %s")
        cur.execute(postgres_select_query, (email,))
        rows = cur.fetchall()
        print(rows[0][0], rows[0][2])
        email_in_db, pw_in_db = rows[0][0], rows[0][2]
        conn.commit()
        conn.close()
        print(email_in_db, pw_in_db, type(email_in_db), type(pw_in_db))
        print(email, password, type(email), type(password))
        if email_in_db == email and pw_in_db == password:
            return render(request, 'correct_password.html')
        else:
            return render(request, 'wrong-password.html')
    except:
        return render(request, 'login.html')

def signup(request):
    print("================================")
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(username, email, password)
    
        conn = psycopg2.connect(database="Crypto_app", user="hzha3299", 
                        password="Cs981020", host="cryptodatabase.ccftjy90se8y.ap-southeast-2.rds.amazonaws.com")
        cur = conn.cursor()
        postgres_insert_query = ("INSERT INTO users (username, email, pw) VALUES (%s,%s,%s)")
        record_to_insert = (username, email, password)
        try:
            cur.execute(postgres_insert_query, record_to_insert)
            conn.commit()
            conn.close()
            return render(request, 'reg_success.html')
        except:
            return render(request, 'reg_notsuccess.html')
    else:
        return render(request, 'signup.html')

def forgotPassword(request):
    return render(request, 'forgot_password.html')



def profile(request):
    return render(request, 'profile.html')
def activity(request):
    return render(request, 'activity.html')

def recoverPassword(request):
    return render(request, 'recover_password.html')
def correctPassword(request):
    return render(request, 'correct_password.html')
def wrongPassword(request):
    return render(request, 'wrong_password.html')
def regSuccess(request):
    return render(request, 'reg_success.html')
def regNotSuccess(request):
    return render(request, 'reg_notsuccess.html')
def transfer(request):
    return render(request, 'transfer.html')
def receive(request):
    return render(request, 'receive.html')
def trade(request):
    return render(request, 'trade.html')
def email_not_exist(request):
    return render(request, 'email_not_exist.html')