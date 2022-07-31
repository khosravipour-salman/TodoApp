from django.shortcuts import render, redirect, get_object_or_404
from todo_app.models import TaskModel
from todo_app.forms import TaskForm


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
		form = TaskForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('list')

	form = TaskForm()
	return render(request, 'todo_app/task_create.html', {'form': form})


def task_update(request, task_id):
	task_obj = get_object_or_404(TaskModel, id=task_id)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task_obj)
		if form.is_valid():
			form.save()
			return redirect('list')

	form = TaskForm(instance=task_obj)
	return render(request, 'todo_app/task_create.html', {'form': form, 'obj': task_obj})


def task_next(request, task_id):
	task_obj = get_object_or_404(TaskModel, id=task_id)
	task_obj.next()
	return redirect(request.META.get('HTTP_REFERER'))

