from django.db import models

class Dann(models.Model):
	name = models.CharField(max_length=50, verbose_name="Имя")
	massage = models.TextField(max_length=255, verbose_name="Сообщение")
	date = models.DateTimeField(verbose_name="Дата сообщения")

	def __str__(self):
		return self.name