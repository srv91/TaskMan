from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'TaskMan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ellipse/', include('ellipse.urls', namespace="ellipse")),
    url(r'^comet/', include('comet.urls', namespace="comet")),
    url(r'^admin/', include(admin.site.urls)),
]
