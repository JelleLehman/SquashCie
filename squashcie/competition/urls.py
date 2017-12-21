from django.conf.urls import url
from . import views

urlpatterns = [
    # /competition/
    url(r'^$', views.index, name='index'),

    # /competition/1/
    url(r'^(?P<match_id>[0-9]+)/$', views.detail, name='detail'),
]
