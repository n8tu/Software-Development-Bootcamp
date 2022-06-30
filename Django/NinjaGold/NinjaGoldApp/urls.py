from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('process_money',views.process),
    path('increase',views.increase),
    path('decrease',views.decrease),
    path('destroy',views.destroy)
]