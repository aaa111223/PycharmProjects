from django.urls import path, re_path
from . import views

urlpatterns = [
    # re_path(r'^blog/(page-(\d+)/)?$', blog_articles),                  # bad
    # re_path(r'^comments/(?:page-(?P<page_number>\d+)/)?$', comments),  # good
    path('test/', views.index),

]
