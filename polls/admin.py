# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question, Choice


# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    # This isn’t impressive with only two fields, but for admin forms with dozens of fields, choosing an intuitive
    # order is an important usability detail.
    # fields = ['pub_date', 'question_text']

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
