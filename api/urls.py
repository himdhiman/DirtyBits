from django.urls import path

from api import views

urlpatterns = [
	path('run/', views.runCode, name = 'run')
]