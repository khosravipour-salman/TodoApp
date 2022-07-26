from django.shortcuts import render, redirect
from todo_app.models import TaskModel


def task_list(request, status=None):
	if status == 'done':
		obj_list = TaskModel.objects.filter(status='f')

	elif status == 'in-process':
		obj_list = TaskModel.objects.filter(status='ip')

	else:
		obj_list = TaskModel.objects.all()

	return render(request, 'todo_app/task_list.html', {'obj_list': obj_list})


def task_delete(request, task_id):
	task_obj = TaskModel.objects.get(id=task_id)
	task_obj.delete()
	return redirect(request.META.get('HTTP_REFERER'))


def task_create(request):
	if request.method == 'POST':
		task_name = request.POST.get('task_name')
		TaskModel.objects.create(title=task_name)
		return redirect('list')

	return render(request, 'todo_app/task_create.html')

# task-inprocess
# task-done
# task-edit
