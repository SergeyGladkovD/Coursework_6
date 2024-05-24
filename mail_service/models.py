from django.db import models

NULLABLE = {"blank": "True", "null": "True"}


class Customer(models.Model):
	name = models.CharField(max_length=150, verbose_name='Ф.И.О.')
	email = models.EmailField(max_length=150, verbose_name='email', unique=True)
	comment = models.TextField(verbose_name='комментарий', **NULLABLE)

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

	# mailing_list = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')

	def __str__(self):
		return f'{self.topic_letter} {self.body_letter}'

	class Meta:
		verbose_name = 'Сообщение'
		verbose_name_plural = 'Сообщения'


class MailingAttempt(models.Model):
	date_time = models.DateTimeField(verbose_name='дата и время последней отправки попытки', auto_now_add=True)
	status = models.BooleanField(verbose_name='статус попытки')  # (успешно / не успешно)
	response_server = models.CharField(max_length=150, verbose_name='ответ почтового сервера', **NULLABLE)  # (если он был)

	# mailing_list = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
	# client = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')

	def __str__(self):
		return f'{self.date_time} {self.status} {self.response_server}'

	class Meta:
		verbose_name = 'Попытка отправки по почте'
		verbose_name_plural = 'Попытки отправки по почте'
