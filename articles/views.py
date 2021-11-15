from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from articles import models, forms


def article_search_view(request):
    q = request.GET.get("q")
    try:
        q = int(q)
    except TypeError:
        q = None

    try:
        obj = models.Article.objects.get(id=q)
    except models.Article.DoesNotExist:
        obj = None
        pass

    context = {
        "object": obj
    }
    return render(request, "articles/search.html", context)

@login_required
def article_create_view(reqeust):
    form = forms.ArticleForm(reqeust.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        obj = form.save()
        context["form"] = forms.ArticleForm(reqeust.POST or None)
        context["object"] = obj
        context["created"] = True
    return render(reqeust, "articles/create.html", context)

def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        try:
            article_obj = models.Article.objects.get(id=id)
        except models.Article.DoesNotExist:
            pass

    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context)