from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StatusChoice(TextChoices):
    ACTIVE = 'active', 'Активно'
    BLOCKED = 'blocked', 'Заблокировано'


class GuestBook(models.Model):
    author_name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Имя автора")
    author_email = models.EmailField(max_length=200, blank=False, null=False, verbose_name="Почта автора")
    description = models.TextField(max_length=2000, blank=False, null=False, verbose_name="Текст записи")
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False, editable=False,
                                      verbose_name="Дата и время создания")
    modified_at = models.DateTimeField(auto_now=True, blank=False, null=False, verbose_name="Дата и время изменения")
    status = models.CharField(choices=StatusChoice.choices, max_length=30, default=StatusChoice.ACTIVE,
                              verbose_name="Статус")

    def __str__(self):
        return f'{self.author_name} {self.status}'
