from django.forms import ModelForm
from .models import Contact

#bu forms dosyasında databes'den otomatik bir html sayfası, bir form oluşturutuyorum
#ModelForm bu komutum benim verim için spesifik tablo oluşturuyor.

class ContactForm(ModelForm):
    class Meta: #Burada formumuzu iletişim modeline baglıyoruz ve bunu iletişimdeki verilerin bütün alanlarını kullanarak form oluşturmak için yapıyoryz.
        model = Contact
        fields = '__all__'