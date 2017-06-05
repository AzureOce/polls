# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context=context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does Not exist.')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', context={'question': question})


def results(request, question_id):
    return HttpResponse("You are look result for %s" % question_id)


def vote(request, question_id):
    return HttpResponse("You are look vote for %s" % question_id)
