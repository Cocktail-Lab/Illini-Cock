from django.shortcuts import render
from django.template import loader
from django.shortcuts import Http404

# Create your views here.
from django.http import HttpResponse

from .models import Question

import openai

openai.api_key = "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"



def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    q = Question.objects.get(pk=question_id)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user","content":q.question_text}])
    r = completion.choices[0].message.content
    return render(request, "polls/detail.html", {"question": r})


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)