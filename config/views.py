from django.shortcuts import render


def home_view(request, id=None):
    return render(request, 'home.html')
