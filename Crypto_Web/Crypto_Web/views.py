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
                                password="Cs981020",
                                host="cryptodatabase.ccftjy90se8y.ap-southeast-2.rds.amazonaws.com")
        cur = conn.cursor()
        postgres_select_query = ("SELECT * FROM users WHERE email = %s")
        cur.execute(postgres_select_query, (email,))
        rows = cur.fetchall()
        if rows == []:
            return render(request, 'email_not_exist.html')
        email_in_db, pw_in_db = rows[0][0], rows[0][2]
        conn.commit()
        conn.close()
        if email_in_db == email and pw_in_db == password:
            request.session['is_login'] = True
            request.session['user_id'] = email
            request.session.set_expiry(600)
            return render(request, 'correct_password.html')

            # request.session['email'] = email

        elif email_in_db == email and pw_in_db != password:
            return render(request, 'wrong_password.html')
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
                                password="Cs981020",
                                host="cryptodatabase.ccftjy90se8y.ap-southeast-2.rds.amazonaws.com")
        postgres_insert_query = ("INSERT INTO users (username, email, pw) VALUES (%s,%s,%s)")
        record_to_insert = (username, email, password)
        try:
            cur = conn.cursor()
            cur.execute(postgres_insert_query, record_to_insert)
            conn.commit()
            conn.close()
            return render(request, 'reg_success.html')
        except:
            return render(request, 'reg_notsuccess.html')
    else:
        return render(request, 'signup.html')

def forgotPassword(request):
    print("================================")
    if request.method == "POST":
        email = request.POST.get("email")
        pw_1 = request.POST.get("password")
        pw_2 = request.POST.get("new_password")
        print(email, pw_1, pw_2)
        if pw_1 != pw_2:
            return render(request, 'forgot_password.html')
    try:
        conn = psycopg2.connect(database="Crypto_app", user="hzha3299",
                                password="Cs981020",
                                host="cryptodatabase.ccftjy90se8y.ap-southeast-2.rds.amazonaws.com")
        cur = conn.cursor()
        postgres_select_query = ("SELECT * FROM users WHERE email = %s")
        cur.execute(postgres_select_query, (email,))
        rows = cur.fetchall()
        if rows == []:
            return render(request, 'email_not_exist.html')
        email_in_db = rows[0][0]
        conn.commit()
        conn.close()
        if email == email_in_db:
            conn = psycopg2.connect(database="Crypto_app", user="hzha3299",
                                    password="Cs981020",
                                    host="cryptodatabase.ccftjy90se8y.ap-southeast-2.rds.amazonaws.com")
            cur = conn.cursor()
            postgres_select_query = ("UPDATE users SET pw = %s WHERE email = %s")
            cur.execute(postgres_select_query, (pw_1, email))
            conn.commit()
            conn.close()
            return render(request, 'login.html')
    except:
        return render(request, 'forgot_password.html')
    else:
        return render(request, 'forgot_password.html')


# def index(request):
#     # 获取session中username
#     email = request.session.get('email', '')
#     if not email:
#
#     print("没有登录啦")
#     return render(request, 'activity.html', {
#         'email': email})


def profile(request):
    return render(request, 'profile.html')


def activity(request):
    return render(request, 'activity.html')


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


# def receive(request):
#    return render(request, 'receive.html')
def trade(request):
    return render(request, 'trade.html')


def email_not_exist(request):
    return render(request, 'email_not_exist.html')

def homepage(request):
    return render(request, 'homepage.html')