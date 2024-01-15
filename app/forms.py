import datetime
from django import forms
from app.models import Experiencia, Seguidor, Seguidos
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    
    username = forms.CharField(label = 'Username', widget = forms.TextInput(attrs = {'class': 'form-control'}))
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs = {'class': 'form-control'}))
    password2 = forms.CharField(label = 'Password confirmation', widget = forms.PasswordInput(attrs = {'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        # ! eliminar help_texts
        help_texts = {k:"" for k in fields}
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 != password2:
            self.add_error('password', "Passwords don't match")
            raise ValidationError('DANGER', code = 'invalid')


class ExperienceForm(forms.ModelForm):
    
    class Meta:
        model = Experiencia
        exclude = ['created_at', 'created_by', 'updated_by', 'last_modified_at', 'last_modified_by', 'borrado']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        fecha_fin = self.cleaned_data.get('fecha_fin')
        
        if fecha_inicio > fecha_fin:
            self.add_error('fecha_inicio', 'Start date must be before end date')
            raise ValidationError('DANGER', code = 'invalid')
        
        if fecha_fin > datetime.date.today():
            self.add_error('fecha_fin', 'End date must be before today')
            raise ValidationError('DANGER', code = 'invalid')
        
class SeguidorForm(forms.ModelForm):
    
    class Meta:
        model = Seguidor
        exclude = ['created_at', 'created_by', 'updated_by', 'last_modified_at', 'last_modified_by', 'borrado']
        
    def clean(self):
        cleaned_data = super().clean()


class SeguidosForm(forms.ModelForm):
    
    class Meta:
        model = Seguidos
        exclude = ['created_at', 'created_by', 'updated_by', 'last_modified_at', 'last_modified_by', 'borrado']