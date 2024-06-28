from datetime import datetime, timedelta
import pytz
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings
from mail_service.models import Mailing, MailingAttempt


def my_job():
    day = timedelta(days=1, hours=0, minutes=0)
    weak = timedelta(days=7, hours=0, minutes=0)
    month = timedelta(days=30, hours=0, minutes=0)

    mailings = Mailing.objects.all().filter(status='Создана')\
        .filter(is_activated=True)\
        .filter(next_date__lte=datetime.now(pytz.timezone('Europe/Moscow')))\
        .filter(end_date__gte=datetime.now(pytz.timezone('Europe/Moscow')))

    for mailing in mailings:
        mailing.status = 'Запущена'
        mailing.save()
        emails_list = [client.email for client in mailing.mail_to.all()]

        result = send_mail(
            subject=mailing.message.title,
            message=mailing.message.content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=emails_list,
            fail_silently=False,
        )

        if result == 1:
            status = 'Отправлено'
        else:
            status = 'Ошибка отправки'

        log = MailingAttempt(mailing=mailing, status=status)
        log.save()

        if mailing.interval == 'ежедневно':
            mailing.next_date = log.last_mailing_time + day
        elif mailing.interval == 'раз в неделю':
            mailing.next_date = log.last_mailing_time + weak
        elif mailing.interval == 'раз в месяц':
            mailing.next_date = log.last_mailing_time + month


        if mailing.next_date < mailing.end_date:
            mailing.status = 'Создана'
        else:
            mailing.status = 'Завершена'
        mailing.save()
