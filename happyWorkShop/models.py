from django.db import models

# Create your models here.


class ContactUsModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    content = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + " " + self.name + "   " + self.phone + "   " + self.email + "   " + self.content
