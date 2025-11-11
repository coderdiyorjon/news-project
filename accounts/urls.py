from django.urls import path
from .views import user_login
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
]