from django import forms

from mail_service.models import Customer, Message, Mailing, MailingAttempt


class CustomerForm(forms.Form):
    class Meta:
        model = Customer


class MessageForm(forms.Form):
    class Meta:
        model = Message


class MailingForm(forms.Form):
    class Meta:
        model = Mailing


class MailingAttemptForm(forms.Form):
    class Meta:
        model = MailingAttempt
