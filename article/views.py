from django.shortcuts import render,HttpResponse

# Create your views here.
#url geldiğinde calıstırılacak fonksyionlar

def index(request):
    context={
        "numbers":[1,2,3,412,412,3415,12],
    }
    
    return render(request,"index.html",context)
def about(request):
    return render(request,"about.html")


def detail(request,id):
    return HttpResponse("Detail:" +str(id))
