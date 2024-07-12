from datetime import datetime, timedelta
import logging
from django.core.cache import cache
import pytz
from django.core.mail import send_mail

from mail_service.models import Mailing, Message, Customer, MailingAttempt
from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

logger = logging.getLogger(__name__)

def my_job():
    # Получаем текущее дату и время с учетом таймзоны.
    # Получаем рассылки с помощью запроса Django ORM.
    # Нужно отфильтровать по статусу и времени.
    # Проверяем периодичность рассылки и соответствие текущей даты и даты старта рассылки.
    # Если рассылка нам подходит, то получаем сообщение рассылки и клиентов рассылки.
    # Отправляем рассылку всем клиентам.
    # Записываем лог нашей рассылки.

    day = timedelta(days=1, hours=0, minutes=0)
    weak = timedelta(days=7, hours=0, minutes=0)
    month = timedelta(days=30, hours=0, minutes=0)

    mailings = (
        Mailing.objects.all()
        .filter(status="Создана")
        .filter(is_activated=True)
        .filter(next_date__lte=datetime.now(pytz.timezone("Europe/Moscow")))
        .filter(end_date__gte=datetime.now(pytz.timezone("Europe/Moscow")))
    )

    for mailing in mailings:
        mailing.status = "Запущена"
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
            status = "Отправлено"
        else:
            status = "Ошибка отправки"

        log = MailingAttempt(mailing=mailing, status=status)
        log.save()

        if mailing.interval == "ежедневно":
            mailing.next_date = log.last_mailing_time + day
        elif mailing.interval == "раз в неделю":
            mailing.next_date = log.last_mailing_time + weak
        elif mailing.interval == "раз в месяц":
            mailing.next_date = log.last_mailing_time + month

        if mailing.next_date < mailing.end_date:
            mailing.status = "Создана"
        else:
            mailing.status = "Завершена"
        mailing.save()


def get_cache_for_mailings():
    if settings.CACHE_ENABLED:
        key = "mailings_count"
        mailings_count = cache.get(key)
        if mailings_count is None:
            mailings_count = Mailing.objects.all().count()
            cache.set(key, mailings_count)
    else:
        mailings_count = Mailing.objects.all().count()
    return mailings_count


# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after your job has run. You should use it
# to wrap any jobs that you schedule that access the Django database in any way.
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database.
    It helps to prevent the database from filling up with old historical records that are no
    longer useful.

    :param max_age: The maximum length of time to retain historical job execution records.
                    Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/10"),  # Every 10 seconds
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: 'delete_old_job_executions'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
