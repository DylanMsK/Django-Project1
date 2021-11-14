from django.contrib import admin
from django.urls import path, include

from .views import home_view

urlpatterns = [
    path("", home_view),
    path("articles/", include("articles.urls"), name="articles"),
    path('admin/', admin.site.urls),
]
