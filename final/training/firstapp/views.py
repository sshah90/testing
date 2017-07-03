from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from firstapp.forms import SignUpForm
from django.contrib import messages
from firstapp.models import UserProfile
from django.template.response import  TemplateResponse

def home(request):

    return render(request,"home.html")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'You are now our member, Please Log in...!')

            return redirect('home')

    else:
        form = SignUpForm()
    return render(request, 'reg_form.html', {'form': form})


def data_base(request):
    data=UserProfile.objects.all()
    return TemplateResponse(request,'user.html',{'data':data})