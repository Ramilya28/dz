from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = (
        ('Low', 'Низкий'),
        ('Medium', 'Средний'),
        ('High', 'Высокий'),
    )
    STATUS_CHOICES = (
        ('New', 'Новая'),
        ('In Progress', 'В прогрессе'),
        ('Done', 'Выполнено'),
        ('Cancelled', 'Отменено'),
        ('Postponed', 'Отложено'),
    )

    name = models.CharField(max_length=100)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')

    def __str__(self):
        return self.name
