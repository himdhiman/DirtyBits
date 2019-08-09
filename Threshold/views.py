from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseForbidden
import requests
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

from Threshold import models

class Index(TemplateView):
    template_name =  'index.html'

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
        return models.Contest.objects.get(id = self.kwargs['contest_id']).Problems

def redirect_view(request):
    response = redirect('run/')
    return response
