from django.db import models

NULLABLE = {"blank": "True", "null": "True"}


class Customer(models.Model):
    email = models.EmailField(verbose_name='email')
    name = models.CharField(max_length=100, verbose_name='Ф.И.О.')
    comment = models.TextField(verbose_name='комментарий')

    def __str__(self):
        return f'Клиент сервиса {self.name} почта {self.email} комментарий {self.comment}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Mailing(models.Model):
    date_time = models.DateTimeField(verbose_name='дата и время первой отправки рассылки')
    period = models.IntegerField(verbose_name='периодичность')  # (раз в день, раз в неделю, раз в месяц)
    status = models.BooleanField(verbose_name='статус рассылки')  # (например, завершена, создана, запущена)

    def __str__(self):
        return f'{self.date_time} {self.period} {self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    topic_letter = models.CharField(max_length=250, verbose_name='тема письма')
    body_letter = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return f'{self.topic_letter} {self.body_letter}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class MailingAttempt(models.Model):
    date_time = models.DateTimeField(verbose_name='дата и время последней отправки попытки')
    status = models.BooleanField(verbose_name='статус попытки')  # (успешно / не успешно)
    response_server = models.BooleanField(verbose_name='ответ почтового сервера')  # (если он был)

    def __str__(self):
        return f'{self.date_time} {self.status} {self.response_server}'

    class Meta:
        verbose_name = 'Попытка отправки по почте'
        verbose_name_plural = 'Попытки отправки по почте'
