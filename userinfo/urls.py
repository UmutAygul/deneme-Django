from django.contrib import admin
from django.urls import path
from userinfo import views


app_name="userinfo"

urlpatterns = [
    path('register/',views.register, name="register"),
    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout"),
    #pathleri burada tanıtılıyor
]







