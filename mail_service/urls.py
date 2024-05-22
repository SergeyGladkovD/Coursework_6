from django.urls import path

from mail_service.views import index, contacts

app_name = 'students_list'

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts')
]
