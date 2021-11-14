from django.shortcuts import render

from articles.models import Article


def article_search_view(request):
    q = request.GET.get("q")
    try:
        q = int(q)
    except TypeError:
        q = None

    try:
        obj = Article.objects.get(id=q)
    except Article.DoesNotExist:
        obj = None
        pass

    context = {
        "object": obj
    }
    return render(request, "articles/search.html", context)

def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        try:
            article_obj = Article.objects.get(id=id)
        except Article.DoesNotExist:
            pass

    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context)