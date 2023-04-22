from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name='accounts'

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("details/<int:pk>/", views.AccountDetailView.as_view(), name="account_details"),
    path("update/<int:pk>", views.AccountUpdateView.as_view(), name="account_update"),
    path("password/update/<int:pk>", views.PasswordUpdateView.as_view(), name="password_update"),
    path("login/", auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
