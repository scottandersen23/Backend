from django.urls import path
from . import views

app_name = 'subscriptions'

urlpatterns = [
    path('plans/', views.list_plans, name='list_plans'),
    path('subscribe/<int:plan_id>/', views.subscribe, name='subscribe'),
    path('status/', views.subscription_status, name='subscription_status'),
]
