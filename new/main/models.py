from django.db import models


class Price(models.Model):
    title = models.CharField('Name', max_length=50)
    price = models.CharField('Price', max_length=50)
    img = models.CharField('Img', max_length=50)


class Sale(models.Model):
    title = models.CharField('Name', max_length=50)
    price = models.CharField('New_price', max_length=50)
    img = models.CharField('Img', max_length=50)


def __str__(self):
    return self.title


class Otz(models.Model):
    name = models.CharField('Name', max_length=50)
    otz = models.CharField('Otz', max_length=50)


class Users(models.Model):
    name = models.CharField('Name', max_length=50)
    number = models.CharField('Number', max_length=50)


class Statistic(models.Model):
    orders_number = models.CharField('Orders', max_length=50)
    clients_number = models.CharField('Clients', max_length=50)


class Salesname(models.Model):
    name = models.CharField('Sale_name', max_length=50)
    date = models.CharField('Date', max_length=50)


class Saleproduct(models.Model):
    name = models.CharField('Name', max_length=50)
    sale = models.CharField('Yes_No', max_length=50)


class Favorite(models.Model):
    number = models.CharField('nnn', max_length=50)
    Name = models.CharField('Name', max_length=50)


class Basket(models.Model):
    name = models.CharField('Name', max_length=50)
    number = models.CharField('Number', max_length=50)


class Errors(models.Model):
    name = models.CharField('Name', max_length=50)
    number = models.CharField('Number', max_length=50)


class Usersname(models.Model):
    name = models.CharField('Name', max_length=50)
    number = models.CharField('Number', max_length=50)