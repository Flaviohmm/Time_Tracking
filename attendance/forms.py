from django import forms
from .models import Punch

class PunchForm(forms.ModelForm):
    class Meta:
        model = Punch
        fields = ['punch_in_time', 'punch_out_time']
        widgets = {
            'punch_in_time': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
            }),
            'punch_out_time': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
            })
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
   