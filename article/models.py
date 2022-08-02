from django.db import models

# Create your models here.


class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    # kullanıcı silinirse user'a özgü her şey silinecek
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    created_date= models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma tarihi")
    #veritabanına eklenilen şey direk atanmış olacak
    # article şeklinde bir model oluşturmuş oldum şuan
    def __str__(self):
        return self.title


