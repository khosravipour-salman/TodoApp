from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from account.forms import UserForm


def sign_up(request):
   if request.method == 'POST':  
      form = UserForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('sign_in')
   
   form = UserForm()
   return render(request, 'account/sign_up.html', {'form': form})



def sign_in(request):
   return HttpResponse('Login page')













      # if request.method == 'POST' :
   #    userForm = UserForm(request.POST)

   #    if userForm.is_valid() :
   #       userForm.save()

   # userForm = UserForm()
   # return render(request, "account/sign_up.html",
   #  {'form' : userForm})