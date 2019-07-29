from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView

# Create your views here.

from Threshold import models

class Index(TemplateView):
    template_name =  'index.html'

class Contests(ListView):
    model = models.Contest
    template_name = 'Threshold/contests.html'

class Contest(DetailView):
    model = models.Contest
    template_name = 'Threshold/contest.html'

class Problem(DetailView):
    template_name = 'Threshold/problem.html'

    def get_queryset(self):
        return models.Contest.get(id = self.kwargs['contest_id']).problems