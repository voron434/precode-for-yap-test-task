# Generated by Django 4.2.5 on 2023-09-30 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название задачи')),
                ('text', models.TextField(verbose_name='Текст задачи')),
                ('start_at', models.DateField(verbose_name='Дата старта задачи')),
                ('finish_at', models.DateField(blank=True, null=True, verbose_name='Дата окончания задачи')),
            ],
        ),
    ]
