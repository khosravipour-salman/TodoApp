from django import forms
from django.core.exceptions import ValidationError
from todo_app.models import TaskModel


class TaskForm(forms.Form):
	class Meta:
		model = TaskModel
		fields = ['title', ]

	def clean_title(self):
		title = self.cleaned_data['title']
		if '_' in title:
			raise ValidationError("Daram gir alaki midm")

		return title

# authentication 
# register sign-up DONE
# login    sign-in --> session cookie --> sessionid 82a1jr5mv6wpxwjzl4a7oas5cxw8jki2
# logout   sign-out

# session table
# 1. username va password ro migire
# 2. usrname va password ro ba db check mikone --> authenticate
# 3. login --> login
# 4. redirect be safhe badi

# 1. logout
# 2. session id hazf mishe 