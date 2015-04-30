from django.conf.urls import patterns, url

from ellipse import views

urlpatterns = patterns('',
    url(r'^$', views.loginpage, name='loginpage'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^manage/$', views.manage, name='manage'),
    url(r'^(?P<user_id>\d+)/$', views.useractivity, name='useractivity'),
)


