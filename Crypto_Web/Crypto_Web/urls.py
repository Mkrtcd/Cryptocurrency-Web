from django.contrib import admin
from django.urls import path
from . import views


app_name = "Crypto_web"

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hidden/', views.hello),
    path('homepage_hidden/', views.homepage_hidden),
    # path('', views.login),
    path('profile/', views.profile),
    path('signup/', views.signup),
    path('login/', views.login),
    path('activity/', views.activity),
    path('forgot-password/', views.forgotPassword),
    path('recover-password/', views.recoverPassword),
]
