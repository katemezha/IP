from django.shortcuts import render
from .models import Price


def index(request):
        prices = Price.objects.all()
        return render(request, 'main/index.html', {'title': 'Название', 'prices': prices})


def about(request):
        return render(request, 'main/about.html')


def otz(request):
        return render(request, 'main/otz.html')





