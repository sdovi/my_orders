from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('newsletter/email', newsletterformview, name='newsletterform'),
    path('message', receivedmessagesview, name='receivedmessages'),
    path('contact', contact_view, name='contact'),
    path('faqs', faqs, name='faqs'),
    path('search-results', search_results, name='search-results'),
]