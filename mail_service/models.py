from django.db import models
from django.shortcuts import render
from django.utils import timezone

import users.models

NULLABLE = {"blank": "True", "null": "True"}

STATUS_CHOICES = [
    ('start', 'start'),
    ('finish', 'finish'),
    ('created', 'created'),
]
INTERVAL_CHOICES = [
    ('once_a_day', 'once_a_day'),
    ('once_a_week', 'once_a_week'),
    ('once_a_month', 'once_a_month'),
]


class Customer(models.Model):
	name = models.CharField(max_length=150, verbose_name='Ф.И.О.')
	email = models.EmailField(max_length=150, verbose_name='email', unique=True)
	comment = models.TextField(verbose_name='комментарий', **NULLABLE)
	user = models.ForeignKey(users.models.User, on_delete=models.CASCADE, null=True, verbose_name='чей клиент')

	def __str__(self):
		return f'Клиент сервиса {self.name} почта {self.email} комментарий {self.comment}'

	class Meta:
		verbose_name = 'Клиент'
		verbose_name_plural = 'Клиенты'


class Message(models.Model):
	topic_letter = models.CharField(max_length=250, verbose_name='тема письма')
	body_letter = models.TextField(verbose_name='тело письма')
	user = models.ForeignKey(users.models.User, on_delete=models.CASCADE, null=True, verbose_name='Владелец сообщения')



	def __str__(self):
		return f'{self.topic_letter} {self.body_letter}'

	class Meta:
		verbose_name = 'Сообщение'
		verbose_name_plural = 'Сообщения'


class Mailing(models.Model):
	name = models.CharField(max_length=50, verbose_name='название рассылки')
	customer = models.ManyToManyField(Customer, verbose_name='кому')
	message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение', **NULLABLE)
	start_date = models.DateTimeField(default=timezone.now, verbose_name='время старта рассылки')
	next_date = models.DateTimeField(default=timezone.now, verbose_name='время следующей рассылки')
	end_date = models.DateTimeField(default=None, verbose_name='время окончания рассылки')
	period = models.IntegerField(verbose_name='периодичность')
	status = models.BooleanField(verbose_name='статус рассылки')  # (например, завершена, создана, запущена)
	is_activated = models.BooleanField(default=True, verbose_name='действующая')
	user = models.ForeignKey(users.models.User, on_delete=models.CASCADE, null=True, verbose_name='Владелец рассылки')

	def __str__(self):
		return f'{self.name} {self.period} {self.status}'

	class Meta:
		verbose_name = 'Рассылка'
		verbose_name_plural = 'Рассылки'


class MailingAttempt(models.Model):
	mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)
	date_time = models.DateTimeField(verbose_name='дата и время последней отправки попытки', auto_now_add=True)
	status = models.BooleanField(verbose_name='статус попытки')
	response_server = models.CharField(max_length=150, verbose_name='ответ почтового сервера', **NULLABLE)

	def __str__(self):
		return f'{self.date_time} {self.status} {self.response_server}'

	class Meta:
		verbose_name = 'Попытка отправки по почте'
		verbose_name_plural = 'Попытки отправки по почте'


def base_home(request):
	return render(request, '/')