from django.db import models


class Task(models.Model):
    title = models.CharField('Название задачи', max_length=200)
    text = models.TextField('Текст задачи', blank=True)

    start_at = models.DateField('Дата старта задачи')
    finish_at = models.DateField(
        'Дата окончания задачи',
        null=True,  # empty means task  ends at the same date as start
        blank=True)

    def __str__(self,):
        return self.title
