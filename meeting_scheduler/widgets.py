from django import forms
from datetime import date, time
from django.core import validators
from django.core.exceptions import ValidationError

class DatePickerInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, attrs=None, format=None, placeholder=None):
        if placeholder:
            attrs = attrs or {}
            attrs['placeholder'] = placeholder
        super().__init__(attrs=attrs, format=format)

class TimePickerInput(forms.TimeInput):
    input_type = 'time'

    def __init__(self, attrs=None, format=None, placeholder=None):
        if placeholder:
            attrs = attrs or {}
            attrs['placeholder'] = placeholder
        super().__init__(attrs=attrs, format=format)

class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'

    def __init__(self, attrs=None, format=None, placeholder=None):
        if placeholder:
            attrs = attrs or {}
            attrs['placeholder'] = placeholder
        super().__init__(attrs=attrs, format=format)