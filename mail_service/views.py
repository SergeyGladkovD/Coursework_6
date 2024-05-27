from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from mail_service.models import Customer, Message, Mailing


class CustomerCreateView(CreateView):
    model = Customer
    fields = ('email', 'name', 'comment')
    success_url = reverse_lazy('mail_service:list')


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ('email', 'name', 'comment')
    success_url = reverse_lazy('mail_service:list')


class CustomerListView(ListView):
    model = Customer


class CustomerDetailView(DetailView):
    model = Customer


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('mail_service:list')


class MessageCreateView(CreateView):
    model = Message
    fields = ('topic_letter', 'body_letter')
    success_url = reverse_lazy('mail_service:list_message')


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('topic_letter', 'body_letter')
    success_url = reverse_lazy('mail_service:list_message')


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mail_service:list_message')


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('date_time', 'period', 'status')
    success_url = reverse_lazy('mail_service:list_mailing')


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('date_time', 'period', 'status')
    success_url = reverse_lazy('mail_service:list_mailing')


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mail_service:list_mailing')
