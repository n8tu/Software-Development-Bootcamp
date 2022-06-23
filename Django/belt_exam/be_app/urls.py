from django.urls import *
from . import views

urlpatterns=[
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('dashboard',views.dashboard),
    path('logout',views.logout),
    path('trips/new',views.new_trip),
    path('trips/create',views.create_trip),
    path('trips/edit/<trip_id>',views.edit_trip),
    path('trips/update/<trip_id>',views.update_trip),
    path('trips/<trip_id>',views.show_trip),
    path('trips/join/<trip_id>',views.join_trip),
    path('trips/cancel/<trip_id>',views.cancel_trip),
    path('trips/delete/<trip_id>',views.delete_trip),
]