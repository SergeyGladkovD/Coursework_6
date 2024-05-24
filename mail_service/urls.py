from django.urls import path
from mail_service.apps import MailServiceConfig
from mail_service.views import CustomerCreateView, CustomerUpdateView, CustomerListView, CustomerDetailView, \
	CustomerDeleteView, MessageCreateView, MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView

app_name = MailServiceConfig.name


urlpatterns = [
	path('create/', CustomerCreateView.as_view(), name='create'),
	path('', CustomerListView.as_view(), name='list'),
	path('view/<int:pk>/', CustomerDetailView.as_view(), name='view'),
	path('edit/<int:pk>', CustomerUpdateView.as_view(), name='edit'),
	path('delete/<int:pk>я', CustomerDeleteView.as_view(), name='delete'),
	path('message/create/', MessageCreateView.as_view(), name='create_message'),
	path('message/', MessageListView.as_view(), name='list_message'),
	path('message/view/<int:pk>/', MessageDetailView.as_view(), name='view_message'),
	path('message/edit/<int:pk>', MessageUpdateView.as_view(), name='edit_message'),
	path('message/delete/<int:pk>я', MessageDeleteView.as_view(), name='delete_message'),
]
