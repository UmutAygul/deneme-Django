from django.db import models

#girilen datayı kaydetmesi için gerekli fonksiyonları giriyorum.

#Models klasorunde bi veritabanı tablosu oluşturuyorum
#Python bu verileri otomatik olarak sql komutuna çeviriyor. Bunu makemigrations komutuyla sağlıyorum.


class Contact(models.Model):
    
    email = models.EmailField()      #sadece geçerli mailleri almamı sağlar.
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email