from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index, name='index'),
    url(r'^testeJson/$', views.testeJson, name='testeJson'),
    url(r'^testeJson2/$', views.testeJson2, name='testeJson2'),
    url(r'^coords/save$', views.coords_save, name='coords_save'),
    url(r'^coords/save2$', views.testeJson, name='testeJson'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]