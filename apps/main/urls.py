from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index, name='Home'),
    url(r'^reg$', register, name='Register'),
    url(r'^authenticate$', auth, name='Authenticate' ),
    url(r'^logout$', logout, name='Logout')
]

