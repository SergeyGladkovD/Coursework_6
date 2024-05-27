from django.urls import path
from mail_service.apps import MailServiceConfig
from mail_service.views import CustomerCreateView, CustomerUpdateView, CustomerListView, CustomerDetailView, \
	CustomerDeleteView, MessageCreateView, MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView, \
	MailingCreateView, MailingListView, MailingDetailView, MailingUpdateView, MailingDeleteView

app_name = MailServiceConfig.name


urlpatterns = [
	path('create/', CustomerCreateView.as_view(), name='create'),
	path('', CustomerListView.as_view(), name='list'),
	path('view/<int:pk>/', CustomerDetailView.as_view(), name='view'),
	path('edit/<int:pk>/', CustomerUpdateView.as_view(), name='edit'),
	path('delete/<int:pk>/', CustomerDeleteView.as_view(), name='delete'),

	path('message/create/', MessageCreateView.as_view(), name='create_message'),
	path('message/', MessageListView.as_view(), name='list_message'),
	path('message/view/<int:pk>/', MessageDetailView.as_view(), name='view_message'),
	path('message/edit/<int:pk>/', MessageUpdateView.as_view(), name='edit_message'),
	path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),

	path('mailing/create/', MailingCreateView.as_view(), name='create_mailing'),
	path('mailing/', MailingListView.as_view(), name='list_mailing'),
	path('mailing/view/<int:pk>/', MailingDetailView.as_view(), name='view_mailing'),
	path('mailing/edit/<int:pk>/', MailingUpdateView.as_view(), name='edit_mailing'),
	path('mailing/delete/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),
]
