from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    """ Опрос """
    question = models.CharField('Вопрос', max_length=100)
    created_by = models.ForeignKey(User, verbose_name = 'Автор', on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Опубликован', auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Choice(models.Model):
    """ Вариант ответа """
    poll = models.ForeignKey(Poll, verbose_name = 'Вопрос', related_name='choices',on_delete=models.CASCADE)
    choice_text = models.CharField('Вариант ответа', max_length=100)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'

class Vote(models.Model):
    """ Голосование """
    voted_by = models.ForeignKey(User, verbose_name = 'Голосующий', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, verbose_name = 'Вопрос', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, verbose_name = 'Вариант ответа', related_name='votes', on_delete=models.CASCADE)

    class Meta:
        # unique_together = ('poll', 'choice')
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'
