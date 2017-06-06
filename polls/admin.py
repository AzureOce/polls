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

    # By default, Django displays the str() of each object. But sometimes it’d be more helpful if we could display
    # individual fields. To do that, use the list_display admin option, which is a tuple of field names to display,
    # as columns, on the change list page for the object:
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
