
from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', views.employee_form, name='emp-insert'),
    path('list/', views.employee_list, name='emp-list'),
    path('update/<int:id>/', views.employee_form, name='emp-update'),
    path('delete/<int:id>/', views.employee_delete, name='emp-delete'),
]
