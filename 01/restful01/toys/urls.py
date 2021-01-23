from django.urls import re_path
from .views import toy_list, toy_detail

urlpatterns = [
    re_path(r'^toys/(?P<pk>[0-9]+)$', toy_detail),
    re_path(r'^toys/?$', toy_list),
]
