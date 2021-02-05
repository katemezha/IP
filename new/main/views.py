from django.shortcuts import render
from .models import Price


def index(request):
        prices = Price.objects.all()
        sale = Sale.objects.all()
        return render(request, 'main/index.html', {'title': 'Название', 'prices': prices, 'sale': sale})


def about(request):
        return render(request, 'main/about.html')


def otz(request):
        return render(request, 'main/otz.html')





