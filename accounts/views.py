from django.shortcuts import render

# user called modules 
from accounts.forms import SignUpForm
from . managers import CustomUserManager
from django.shortcuts import render, get_list_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView)
from django.utils import timezone
from django.urls import reverse_lazy
from accounts.models import CustomUser

# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

