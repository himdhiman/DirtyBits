from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseForbidden
import requests
from django.views.decorators.csrf import csrf_exempt
import json
from coderunner.coderunner import code


# Create your views here.

from Threshold import models


class Index(TemplateView):
    template_name = 'index.html'

# @login_required(login_url = '/auth/login')


class Contests(LoginRequiredMixin, ListView):
    login_url = 'auth/login/'
    redirect_field_name = 'redirected_to'
    model = models.Contest
    template_name = 'Threshold/contests.html'

# @login_required(login_url = '/auth/login')


class Contest(DetailView):
    model = models.Contest
    template_name = 'Threshold/contest.html'

# @login_required(login_url = '/auth/login')


class Problem(DetailView):
    template_name = 'Threshold/problem.html'

    def get_queryset(self):
        return models.Contest.objects.get(id=self.kwargs['contest_id']).Problems

@csrf_exempt
def redirect_view(request):
    # print("HELLO")
    response = redirect('run')
    return response


def RunCode(request):
    SourceCode = request.POST.get('source')
    Language = request.POST.get('lang')
    if(request.POST.get('input') != ''):
        input_data = request.POST.get('input')
        r = code(SourceCode, Language, inp = input_data, path = False)
        r.run()
    else:
        r = code(SourceCode, Language, path = False)
        r.run()
    cstat = r.getStatus()
    rstat = "Running"
    time = r.getTime()
    memory = r.getMemory()
    out = r.getOutput()
    if(cstat == "Accepted"):
        data = {
        'cstat' : cstat,
        'rstat' : rstat,
        'time' : time,
        'memory' : memory,
        'output' : out
        }
        return JsonResponse(data)

    else:
        err = r.getError()
        data = {
        'cstat' : cstat,
        'rstat' : rstat,
        'time' : time,
        'memory' : memory,
        'output' : out,
        'error' : err
        }
        print(data)
        return JsonResponse(data)
