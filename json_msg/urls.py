from django.urls import path

from.views import push_json

urlpatterns = [
    path("", push_json, name="home"),
]