from django.shortcuts import render,HttpResponse

# Create your views here.
#url geldiğinde calıstırılacak fonksyionlar

def index(request):
    return render(request,"article/index.html")




