from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseForbidden


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

RUN_URL = "https://api.hackerearth.com/v3/code/run/"
def runCode(request):
	if request.is_ajax():
		source = request.POST['source']
		lang = request.POST['lang']
		data = {
			'client_secret': 'efee14e3d19da585f2660381d79d81891f3417a9' ,
			'async': 0,
			'source': source,
			'lang': lang,
			'time_limit': 5,
			'memory_limit': 262144,
		}
		if 'input' in request.POST:
			data['input'] = request.POST['input']
		r = requests.post(RUN_URL, data=data)
		return JsonResponse(r.json(), safe=False)

	else:
		return HttpResponseForbidden()