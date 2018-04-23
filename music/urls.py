from django.conf.urls import url
from . import views

app_name='music'
urlpatterns = [
    # url(r'^$', views.index,name='index'),
    url(r'^(?P<album_id>[0-9]+)/favourite/$',views.favourite,name='favourite'),
    #url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^$', views.Indexview.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.Detailview.as_view(),name='detail'),
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-Update'),
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
    url(r'^(?P<pk>[0-9]+)/addsong/$', views.songCreate.as_view(), name='song-add'),
    url(r'^register/$', views.UserFormView.as_view(),name='register'),

]