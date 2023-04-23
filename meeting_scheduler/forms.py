from django import forms
from meeting_scheduler.models import OffHour, Appointment
from django.contrib.admin.widgets import AdminTimeWidget 
from django.utils import timezone
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from django.core.exceptions import ValidationError

class OffHourForm(forms.ModelForm):
    class Meta:
        model = OffHour
        fields = ("date","start_time","end_time")

        widgets = {
            'date': DatePickerInput(attrs={'placeholder':'Enter date'}),
            'start_time': TimePickerInput(),
            'end_time': TimePickerInput(),
        }

class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = ("title","agenda","guest","date","start_time","end_time")
    
        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'agenda': forms.Textarea(attrs={'class':'editable medium-editor-textarea appointment-content'}),
            'date': DatePickerInput(attrs={'placeholder':'Enter date'}),
            'start_time': TimePickerInput(),
            'end_time': TimePickerInput(),
        }


