from django.shortcuts import render
from .models import Price
from .models import Sale



def index(request):
        prices = Price.objects.order_by('price')
        sale = Sale.objects.all()
        return render(request, 'main/index.html', {'title': 'Название', 'prices': prices})
        return render(request, 'main/index.html', {'title': 'Название', 'sale': sale})


def about(request):
        return render(request, 'main/about.html')


def otz(request):
        return render(request, 'main/otz.html')





