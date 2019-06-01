from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import PasswordInput
from .models import CustomUser, Comment, Student, Course, Grades, Subject, Category
from django import forms


class MembersCreationForm(forms.Form):

    TYPE_CHOICES = (
        (1, "Profesor"),
        (2, "Preceptor"),
        (3, "Director")
    )

    first_name = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control'})), label='Nombre')
    last_name = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control'})), label='Apellido')
    email = forms.EmailField(widget=forms.EmailField)
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


class GradeCreationForm(forms.ModelForm):
    class Meta:
        model = Grades
        exclude = ['deleted_at']

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

    name = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control'})), label='Nombre del alumno')
    surname = forms.CharField(widget=(forms.TextInput(attrs={'class': 'form-control'})), label='Apellido del alumno')
    subject = forms.ChoiceField(choices=TYPE_SUBJECT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control'}), required=True, label='Materia')
    grade = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control'}), required=True, label='Nota')


class CourseCreationForm(forms.ModelForm):

    class Meta:
        model = Course
        exclude = ['deleted_at']


class SubjectCreationForm(forms.ModelForm):

    class Meta:
        model = Subject
        exclude = ['deleted_at']


class CategoryCreationForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ['deleted_at']
