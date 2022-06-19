from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('create_course',views.create_course),
    path('destroy/<_id>',views.destroy_course)
]
