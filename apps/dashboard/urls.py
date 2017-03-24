from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index, name='Home'),
    url(r'^add$', quote, name='Quotes'),
    url(r'^fav/(?P<fav_id>\d+)$', favorites, name='Fav')
    # url(r'^remove/(?P<fav_id>\d+)$', remove,name='Remove')
]

