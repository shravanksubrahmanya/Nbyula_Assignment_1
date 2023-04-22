from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class SignUpForm(UserCreationForm):
    class Meta:
        fields = ('profile_pic','username','fname','lname','email','password1','password2')
        model = CustomUser # using custom user model for Signup form

        widgets = {
            'profile_pic' : forms.ClearableFileInput(attrs = {'class':'fas fa-user-alt'})
        }

class AccountUpdateForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ("fname","lname","email",'profile_pic')

        widgets = {
            'profile_pic' : forms.ClearableFileInput(attrs = {'class':'fas fa-user-alt'})
        }

class PasswordUpdateForm(PasswordChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ("old_password","new_password1","new_password2")
    
    def __init__(self, *args, **kwargs):
        super(PasswordUpdateForm, self).__init__(*args, **kwargs)
        # Add any additional fields you want here.

    def clean(self):
        # Override the clean method to add any custom validation
        cleaned_data = super(PasswordUpdateForm, self).clean()
        # Add any custom validation you want here.
        return cleaned_data
