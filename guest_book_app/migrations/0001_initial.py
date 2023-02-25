# Generated by Django 4.1.7 on 2023-02-25 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100, verbose_name='Имя автора')),
                ('author_email', models.EmailField(max_length=200, verbose_name='Почта автора')),
                ('description', models.TextField(max_length=2000, verbose_name='Текст записи')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=30, verbose_name='Статус')),
            ],
        ),
    ]
