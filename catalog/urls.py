from django.conf.urls import url
from django.urls import path, re_path
from .import views


app_name='catalog'


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),

]
