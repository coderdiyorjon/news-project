from django.urls import path
from .views import dashboard_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('profile/', dashboard_view, name='user_profile'),
]