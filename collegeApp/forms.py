from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import PasswordInput
from .models import CustomUser, Comment, Student
from django import forms


class MembersCreationForm(forms.Form):

    TYPE_CHOICES = (
        (1, "Profesor"),
        (2, "Preceptor"),
        (3, "Director")
    )

    first_name = forms.CharField(label='Nombre', max_length=100)
    last_name = forms.CharField(label='Apellido', max_length=100)
    email = forms.EmailField()
    password = forms.CharField(label='Contraseña', widget=PasswordInput)
    type = forms.ChoiceField(choices=TYPE_CHOICES)


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class CommentCreationForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['deleted_at', 'date', 'author']


class StudentCreationForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ['deleted_at']
        labels = {
            'birthday': 'Fecha de nacimiento'
        }


class UpdateGrade(forms.Form):

    TYPE_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
    )

    TYPE_SUBJECT_CHOICES = (
        (1, "Profesor"),
        (2, "Preceptor"),
        (3, "Director")
    )

    name = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control'})), label='Nombre del alumno:')
    surname = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control'})), label='Apellido del alumno')
    subject = forms.ChoiceField(choices=TYPE_SUBJECT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control'}), required=True, label='Materia')
    grade = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control'}), required=True, label='Nota')

