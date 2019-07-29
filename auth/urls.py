from django.urls import path

from auth import views

urlpatterns = [
    path('signup/', views.SignUp),
    path('login/', views.UserLogin),
    path('logout/', views.Logout)
]