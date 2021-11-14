from django.urls import path

from articles import views


app_name = "articles"
urlpatterns = [
    path("", views.article_search_view, name="search"),
    path("<int:id>/", views.article_detail_view, name="detail"),
]
