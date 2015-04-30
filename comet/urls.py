from django.conf.urls import patterns, url
from comet import views

urlpatterns = [
    url(r'^$', views.task_view),
    url(r'^(?P<task_id>[0-9]+)/$', views.task_del),
]
