from django.urls import path
from todo_app import views

urlpatterns = [
	path('task-list/', views.task_list, name='list'), 
	path('task-list/<str:status>/', views.task_list, name='list_with_param'),
	path('task-delete/<int:task_id>/', views.task_delete, name='delete'), 
	path('task-create/', views.task_create, name='create'), 
	path('task-update/<int:task_id>/', views.task_update, name='update'),
	path('task-next-state/<int:task_id>/', views.task_next, name='next'),
]
