from django.conf.urls import url
from django.urls import path, re_path,include
from .import views
from django.conf import settings



app_name='catalog'


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$' , views.AuthorListView.as_view(), name='authors'),
    # url(r'^accounts/login$', include('django.contrib.auth.views.login'))

]

urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
