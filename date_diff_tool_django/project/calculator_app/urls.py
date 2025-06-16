from django.urls import path
from . import views

urlpatterns = [
    path('working-capacity/', views.working_capacity, name='working_capacity'),
    path('calculate-days/', views.calculate_days, name='calculate_days'),
    path('calculate-date/', views.calculate_date, name='calculate_date'),
]
