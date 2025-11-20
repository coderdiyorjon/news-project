from django.urls import path
from .views import dashboard_view, logout_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logged_out.html'), name='logout'),
    path('logout_page/', logout_view, name='logout_page'),
    path('profile/', dashboard_view, name='user_profile'),
]