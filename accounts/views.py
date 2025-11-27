from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django import forms

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form)
            data = form.cleaned_data
            print(data)
            user = authenticate(request, username=data['username'],
                                password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Login Muvaffaqiyatli Amalga Oshirildi')
                else:
                    return HttpResponse('Foydalanuvchi aktiv emas')
            else:
                return HttpResponse('Login yoki Parol xato bo\'lishi mumkin')
        else:
            raise forms.ValidationError(form.errors)
    else:
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'registration/login.html', context)

def dashboard_view(request):
    user = request.user
    print(request)
    print(user)

    context = {
        'user': user,
    }
    return render(request, 'pages/user_profile.html', context)


def logout_view(request):
    return render(request, 'registration/logout.html')


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            context = {
                'new_user': new_user,
            }
            return render(request, 'accounts/register_done.html', context=context)
        else:
            raise forms.ValidationError(user_form.errors)
    else:
        user_form = UserRegistrationForm()
        context = {
            'user_form': user_form,
        }
        return render(request, 'accounts/register.html', context=context)