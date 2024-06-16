from django.db import models

class Contact(models.Model):
    Name=models.CharField(max_length=70)
    Email=models.CharField(max_length=50)
    Number=models.CharField(max_length=20)
    Subject=models.CharField(max_length=50)
    Message=models.CharField(max_length=1000)

    def __str__(self):
        return self.Name