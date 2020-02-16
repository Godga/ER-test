from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('register/', views.registration, name='registration'),
	path('login/', views.login, name='login'),
	path("logout/", views.logout_request, name="logout"),
]