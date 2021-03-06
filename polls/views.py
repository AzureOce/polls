# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice


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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', context={
        'question': question,
    })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST is a dictionary-like object that lets you access submitted data by key name.
        # request.POST values are always strings.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # request.POST['choice'] will raise KeyError if choice wasn’t provided in POST data. The above code checks for
    # KeyError and redisplays the question form with an error message if choice isn’t given.
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', context={
            'question': question,
            'error_message': "You didn't Select a Choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.This tip isn’t specific to Django; it’s just good Web development practice.
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))


# Amend views
class IndexView(generic.ListView):
    """
    display a list of objects the ListView generic view uses a default template called <app name>/<model
    name>_list.html; we use template_name to tell ListView to use our existing "polls/index.html" template.
    """

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the latest five published Question.
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
        # return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    """
    display a detail page for a particular type of object. The DetailView generic view expects the primary key value
    captured from the URL to be called "pk", so we’ve changed question_id to pk for the generic views.
    the DetailView generic view uses a template called <app name>/<model name>_detail.html.
    """
    template_name = 'polls/detail.html'
    context_object_name = 'question'
    model = Question

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultView(generic.DetailView):
    model = Question
    context_object_name = 'question'
    template_name = 'polls/result.html'
