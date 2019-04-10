from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import CustomUserLoginForm, CustomUserCreationForm, CustomUserEditForm
from django.contrib import auth
from django.urls import reverse


def login(request):
    title = 'Pinguru - Login'

    login_form = CustomUserLoginForm(data=request.POST or None)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = CustomUserCreationForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        register_form = CustomUserCreationForm()

    content = {'title': title, 'register_form': register_form}

    return render(request, 'authapp/register.html', content)


def edit(request):
    title = 'edit'

    if request.method == 'POST':
        edit_form = CustomUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        edit_form = CustomUserEditForm(instance=request.user)

    content = {'title': title, 'edit_form': edit_form}

    return render(request, 'authapp/edit.html', content)
