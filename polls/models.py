# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(verbose_name="问题描述", max_length=200)
    pub_date = models.DateTimeField('发布日期')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return timezone.now() - timezone.timedelta(days=1) <= self.pub_date <= timezone.now()

    was_published_recently.short_description = "是否最近发布"


class ChoiceManager(models.Manager):
    def test_filter(self, test):
        # 这个方法使用了self.filter()，此处self指manager本身
        return self.filter(choice_text__contains=test).count()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #  它将取代模型的默认manager（objects）如果我们没有特别定义，它将会被自动创建。 我们把它命名为objects，这是为了与自动创建的manager保持一致。
    objects = ChoiceManager()

    def __str__(self):
        return self.choice_text
