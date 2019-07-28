from django.urls import path, include

from Threshold import views

urlpatterns = [
    path('', views.index)
    # path('problem/', include('views.problem'))
]