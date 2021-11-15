from django.shortcuts import render

from articles import models


def home_view(request, id=None):
    context = {
        "object_list": models.Article.objects.all()
    }
    return render(request, 'home.html', context)
