from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
import requests
import json
from django.views.decorators.csrf import csrf_exempt

RUN_URL = 'http://api.hackerearth.com/code/run/'

@csrf_exempt
def runCode(request):
	if request.is_ajax():
		source = request.POST.get('source')
		lang = request.POST.get('lang')
		data = {
			'client_id': 'a4daf04286e2aa804304a412dd41e1c7c0b2a27868e07.api.hackerearth.com',
			'client_secret': 'b359cdd5e6fa0e36900d299525108b9d104e72d9',
			'async': 0,
			'source': source,
			'lang': lang,
			'time_limit': 5,
			'memory_limit': 262144,
		}
		print(data)
		if 'input' in request.POST:
			data['input'] = request.POST['input']
		r = requests.post('http://api.hackerearth.com/code/run/', data=json.dumps(data))
		print(r.json())
		return JsonResponse(r.json(), safe=False)

	else:
		return HttpResponseForbidden()