from django.contrib import admin
from django.urls import path
from contact import views 

appname="contact"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact_view, name='contact'),
]


