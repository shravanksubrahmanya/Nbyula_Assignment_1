from django.shortcuts import render

# user called modules 
from meeting_scheduler.forms import OffHourForm, AppointmentForm
from meeting_scheduler.models import OffHour, Appointment
from django.shortcuts import render, get_list_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView)
from django.utils import timezone
from django.urls import reverse_lazy
from accounts.models import CustomUser
from django.core.exceptions import ValidationError

class OffHourCreateView(CreateView, LoginRequiredMixin):
    model = OffHour
    template_name = "meeting_scheduler/offhour_create.html"
    form_class = OffHourForm
    login_url = 'login/'
    success_url = reverse_lazy('home')

    def form_valid(self, form, **kwargs):
        form.instance.terraformer = self.request.user
        if form.instance.date < timezone.now().date():
            form.add_error('date', 'Please select a date in the future')
            return self.form_invalid(form)
        
        if form.instance.date == timezone.now.date():
            if  form.instance.start_time < timezone.now().time():
                form.add_error('start_time', 'Start time should be greater than current time')
                return self.form_invalid(form)
        
        if form.instance.start_time and form.instance.end_time and form.instance.start_time >= form.instance.end_time:
            form.add_error('end_time', 'Start time should be earlier than end time')
            return self.form_invalid(form)
        
        return super().form_valid(form)


class AppointmentCreateView(CreateView, LoginRequiredMixin):
    model = Appointment
    template_name = "meeting_scheduler/appointment_create.html"
    form_class = AppointmentForm
    login_url = 'login/'
    success_url = reverse_lazy('home')

    def form_valid(self, form, **kwargs):
        form.instance.terraformer = self.request.user

        if form.instance.date < timezone.now().date():
            form.add_error('date', 'Please select a date in the future')
            return self.form_invalid(form)
        
        if form.instance.date == timezone.now().date():
            if  form.instance.start_time < timezone.now().time():
                form.add_error('start_time', 'Start time should be greater than current time')
                return self.form_invalid(form)
        
        if form.instance.start_time and form.instance.end_time and form.instance.start_time >= form.instance.end_time:
            form.add_error('end_time', 'Start time should be earlier than end time')
            return self.form_invalid(form)
        
        return super().form_valid(form)

