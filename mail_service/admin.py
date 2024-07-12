from django.contrib import admin
from mail_service.models import Customer, Mailing, MailingAttempt, Message


@admin.register(Customer)
class Customer(admin.ModelAdmin):
    list_display = ("name", "email", "comment")
    list_filter = ("name", "email", "comment")
    search_fields = ("name", "email", "comment")


@admin.register(Mailing)
class Mailing(admin.ModelAdmin):
    list_display = ("start_date", "period", "status")
    list_filter = ("start_date", "period", "status")
    search_fields = ("start_date", "period", "status")


@admin.register(Message)
class Message(admin.ModelAdmin):
    list_display = ("topic_letter", "body_letter")
    list_filter = ("topic_letter", "body_letter")
    search_fields = ("topic_letter", "body_letter")


@admin.register(MailingAttempt)
class MailingAttempt(admin.ModelAdmin):
    list_display = ("date_time", "status", "response_server")
    list_filter = ("date_time", "status", "response_server")
    search_fields = ("date_time", "status", "response_server")
