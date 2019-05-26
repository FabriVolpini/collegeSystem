from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.db import models


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class CommentCreation(forms.Form):
    name = forms.CharField(label='Nombre del Alumno', max_length=100)
    surname = forms.CharField(label='Apellido del Alumno', max_length=100, required=100)
    year = forms.ChoiceField(label='Año', widget=forms.Select(), required=True)
    division = forms.ChoiceField(label='División', widget=forms.Select(), required=True)
    category = forms.ChoiceField(label='Categoría', widget=forms.Select(), required=True)
    description = forms.CharField(label='Descripción')


class UpdateGrade(forms.Form):
    name = forms.CharField(label='Nombre del Alumno', max_length=100)
    surname = forms.CharField(label='Apellido del Alumno', max_length=100, required=100)
    subject = forms.ChoiceField(label='Materia', widget=forms.Select(), required=True)
    grade = forms.ChoiceField(label='Nota', widget=forms.Select(), required=True)



# class InitForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField()
#
#     def clean_name(self):
#         return "name_passed_value"
#
#     #Field validation
#
#     def clean_email(self):
#         email_passed = self.cleaned_data.get("email")
#         email_req = "yourdomain.com"
#         if not email_req in email_passed:
#             raise forms.ValidationError("Email inválido, intente de nuevo")
#         return email_passed
#
#     def clean_password(self):
#         password_passed = self.cleaned_data.get("password")
#         password_req = "..."
#         if not password_req in password_passed:
#             raise forms.ValidationError("Contraseña inválida, intente de nuevo")
#         return password_passed
#
#     #General validation
#
#     def clean(self):
#         cleaned_data = super(UserForm, self).clean()
#         email_passed = cleaned_data.get("email")
#         email_req = "yourdomain.com"
#         password_passed = cleaned_data.get("password")
#         password_req = "..." #Ver con Agus
#         if not email_req in email_passed:
#             raise forms.ValidationError("Email o contraseña incorrectas")
#         return email_passed
