from django.contrib import admin
from django.urls import path
from . import views


app_name = "Crypto_web"

urlpatterns = [
    path('profile/', views.profile),
    path('signup/', views.signup),
    path('login/', views.login),
    path('activity/', views.activity),
    path('forgot-password/', views.forgotPassword),
    path('recover-password/', views.recoverPassword),
    path('correct-password/', views.correctPassword),
    path('wrong-password/', views.wrongPassword),
]
