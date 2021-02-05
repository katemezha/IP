from django.db import models


class Price(models.Model):
    title = models.CharField('Name', max_length=50)
    price = models.CharField('Price', max_length=50)
    img = models.CharField('Img', max_length=50)

class Sale(models.Model):
    title = models.CharField('Name', max_length=50)
    price = models.CharField('Price', max_length=50)
    img = models.CharField('Img', max_length=50)



    def __str__(self):
        return self.title