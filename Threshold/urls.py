from django.urls import path, include
from django.contrib.auth.decorators import login_required

from Threshold import views

urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    #  path('problem/', include('views.problem'))
    path('contests', views.Contests.as_view(), name = 'contests'),
    path('contests/<int:pk>', login_required(views.Contest.as_view()), name = 'contest'),
    path('contests/<int:contest_id>/problem/<int:pk>', login_required(views.Problem.as_view()), name = 'Problem'),
    path('run/', views.RunCode, name = 'run')
    # path('contests/run/', views.redirect_view)
]