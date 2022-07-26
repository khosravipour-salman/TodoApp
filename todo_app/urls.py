from django.urls import path
from todo_app import views

urlpatterns = [
	path('task-list/', views.task_list, name='list'), 
	path('task-list/<str:status>/', views.task_list, name='list_with_param'),
	path('task-delete/<int:task_id>/', views.task_delete, name='delete'), 
	path('task-create/', views.task_create, name='create'), 
]