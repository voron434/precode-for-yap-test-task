import datetime

from django.shortcuts import render

from tasks.models import Task


def list_tasks_for_day(request):
    # FIXME: Задачи отображаются на текущий день. Нужно сделать выбор даты

    date = datetime.datetime.today()
    active_tasks_for_date = Task.objects.filter(
        start_at__lte=date,
        finish_at__gte=date
    )  # FIXME: даты с пустым finish_at не отображаются, починим в следующих заданиях

    context = {
        'active_tasks_for_date': active_tasks_for_date,
    }
    return render(request, 'tasks_list.html', context=context)
