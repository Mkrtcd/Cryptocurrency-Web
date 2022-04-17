from django.contrib import admin
from django.urls import path
from . import views


app_name = "Crypto_web"

urlpatterns = [
    path('profile/', views.profile),
    path('signup/', views.signup),
    path('login/', views.login),
    path('activity/', views.activity),
    path('forgot_password/', views.forgotPassword),
    path('recover_password/', views.recoverPassword),
    path('correct_password/', views.correctPassword),
    path('wrong_password/', views.wrongPassword),
    path('reg_success/', views.regSuccess),
    path('reg_notsuccess/', views.regNotSuccess),
    path('transfer/', views.transfer),
    path('receive/', views.receive),
    path('trade/', views.trade),
]
