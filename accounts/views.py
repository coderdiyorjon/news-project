from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

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
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'account/login.html', context)