from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import *
from . import forms


def index(request):
    my_dict = {
        'insert_me': 'Hello Iam from views.py',
        'number': 100
    }
    return render(request, 'AppTwo/index.html', context=my_dict)


def access_records(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    my_dict = {
        'insert_me': 'Hello Iam from views.py'
    }
    return render(request, 'AppTwo/access_records.html', context=date_dict)


def display_users(request):
    form = forms.NewUserForm()

    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            return index(request)
        else:
            print('ERROR FORM INVALID')
    # users = User.objects.order_by('first_name')
    # data = {"user_data": users}
    return render(request, 'AppTwo/users.html', {'form': form})


def help_index(request):
    return HttpResponse('This is Help')


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            pass
    return render(request, 'AppTwo/form_page.html', {'form': form})


@login_required
def special(request):
    return HttpResponse('Special Function')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)  # hashing password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'AppTwo/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account NOT ACTIVE")
        else:
            print("Attempt failed!")
            print(f"Username: {username} and password {password}")
            return HttpResponse("Invalid details")
    else:
        return render(request, 'AppTwo/login.html', {})
