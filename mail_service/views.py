from random import random

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView,
    TemplateView,
)

from blog.models import Material
from mail_service.models import Customer, Message, Mailing
from mail_service.services import get_cache_for_mailings, get_cache_for_active_mailings


def home_page(request):
    return render(request, "mail_service/home_page.html")


# class HomePageView(ListView):
#     model = Mailing
#     template_name = 'mail_service/home_page.html'
#
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         context_data['mailings_count'] = get_cache_for_mailings()
#         context_data['active_mailings_count'] = get_cache_for_active_mailings()
#         blog_list = list(Material.objects.all())
#         random.shuffle(blog_list)
#         context_data['blog_list'] = blog_list[:3]
#         context_data['clients_count'] = len(Customer.objects.all())
#         return context_data


class CustomerCreateView(CreateView):
    model = Customer
    fields = "__all__"
    success_url = reverse_lazy("mail_service:list_customer")


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = "__all__"
    success_url = reverse_lazy("mail_service:list_customer")


class CustomerListView(ListView):
    model = Customer


class CustomerDetailView(DetailView):
    model = Customer


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy("mail_service:list_customer")


class MessageCreateView(CreateView):
    model = Message
    fields = "__all__"
    success_url = reverse_lazy("mail_service:list_message")


class MessageUpdateView(UpdateView):
    model = Message
    fields = "__all__"
    success_url = reverse_lazy("mail_service:list_message")


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("mail_service:list_message")


class MailingCreateView(CreateView):
    model = Mailing
    fields = "__all__"
    success_url = reverse_lazy("mail_service:list_mailing")


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = "__all__"
    success_url = reverse_lazy("mail_service:list_mailing")


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy("mail_service:list_mailing")
