from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''), #takes over home
    path('add/', views.task_add, name='task_add'),
    path('<int:id>/', views.task_detail, name='task_detail'),
    path('<int:id>/edit/', views.task_edit, name='task_edit'),
    path('<int:id>/delete/', views.task_delete, name='delete_task'),
]
