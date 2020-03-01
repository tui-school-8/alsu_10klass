from django.db import models


class Poll(models.Model):
    name = models.CharField('Название', max_length=200)
    question = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Card(models.Model):
    title = models.CharField('Название', max_length=200, blank=True)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Картинка', null=True)
    poll = models.ForeignKey(Poll, models.CASCADE)

    class Meta:
        verbose_name = 'Карточка для сравнения'
        verbose_name_plural = 'Карточки для сравнения'


comparison_choices = (
    ('left', 'Левый'),
    ('right', 'Правый'),
)


class Comparison(models.Model):
    left_card = models.ForeignKey(Card, models.CASCADE, 'left_comparisons')
    right_card = models.ForeignKey(Card, models.CASCADE, 'right_comparisons')
    choice = models.CharField('Выбор', choices=comparison_choices, max_length=20)
