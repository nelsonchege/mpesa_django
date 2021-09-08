from django.urls import path
from django.urls.resolvers import URLPattern
from .views import lipa_na_mpesa_online
urlpatterns =[
    path('lipa', lipa_na_mpesa_online, name='lipa_na_mpesa'),
]