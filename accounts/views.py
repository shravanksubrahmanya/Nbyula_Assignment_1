from django.shortcuts import render

# user called modules 
from accounts.forms import SignUpForm, AccountUpdateForm, PasswordUpdateForm
from . managers import CustomUserManager
from django.shortcuts import render, get_list_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView)
from django.utils import timezone
from django.urls import reverse_lazy
from accounts.models import CustomUser
from django.contrib.auth.views import PasswordChangeView

# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class AccountDetailView(DetailView, LoginRequiredMixin):
    model = CustomUser
    template_name = "accounts/account_detail.html"
    login_url = "login/"
    redirect_field_name = 'index.html'

class AccountUpdateView(UpdateView, LoginRequiredMixin):
    model = CustomUser
    template_name = "accounts/account_update.html"
    login_url = "login/"
    form_class = AccountUpdateForm

class PasswordUpdateView(PasswordChangeView, LoginRequiredMixin):
    model = CustomUser
    template_name = "accounts/password_update.html"
    login_url = "login/"
    form_class = PasswordUpdateForm

    def get_success_url(self):
        return reverse_lazy('accounts:account_details', kwargs={'pk': self.request.user.pk})



