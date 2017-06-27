from django.shortcuts import render, redirect
from firstapp.smit import RegistrationForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    return render(request,"home.html")

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect((''))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'reg_form.html', args)