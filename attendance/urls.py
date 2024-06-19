from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('punch/', views.punch, name='punch'),
    path('report/', views.report, name='report'),
]
