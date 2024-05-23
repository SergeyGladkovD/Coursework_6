from django.urls import path
from mail_service.apps import MailServiceConfig
from mail_service.views import CustomerCreateView, CustomerUpdateView, CustomerListView, CustomerDetailView, \
	CustomerDeleteView, MessagesView

app_name = MailServiceConfig.name


urlpatterns = [
	path('create/', CustomerCreateView.as_view(), name='create'),
	path('', CustomerListView.as_view(), name='list'),
	path('view/<int:pk>/', CustomerDetailView.as_view(), name='view'),
	path('edit/<int:pk>', CustomerUpdateView.as_view(), name='edit'),
	path('delete/<int:pk>я', CustomerDeleteView.as_view(), name='delete'),
	path('message/', MessagesView.as_view(), name='message'),
]
