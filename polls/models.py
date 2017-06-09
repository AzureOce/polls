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


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
