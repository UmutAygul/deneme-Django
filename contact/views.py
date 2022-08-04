from django.shortcuts import render
from .forms import ContactForm

#forms.py den formumu contact klası için özel olarak oluşturdukltan sonra
#views.py de artık kullanabilir hale getiriyorum.


#submit edilen form data http post komutu ile, view functiona gonderilecek
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():#mail adresi uygun mu check ediliyor. ver ardından
            form.save()#data buraya kaydediliyor (form verisi)
            return render(request, 'oldu.html')#datanın gönderildiliğini bildirmek amacıyla bir html sayfasına yönlendiriyorum.
    form = ContactForm()
    context = {'form': form} #bu oluşturulan sözlük ile dinamik olark front end de oluşturulan veri var.
    return render(request, 'contact.html', context)#render fonksiyonu ile context'i views'ten contact_view'ın cagrıldığı yere return ediyoruz 


def index(request):
    context={
        "numbers":[1,1,2,3,5,8,13,21,34,55,89,144],
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

