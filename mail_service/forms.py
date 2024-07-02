from django import forms

from mail_service.models import Customer, Message, Mailing, MailingAttempt


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


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
