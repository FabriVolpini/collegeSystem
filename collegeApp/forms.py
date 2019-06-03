from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import PasswordInput, Textarea
from .models import CustomUser, Comment, Student, Course, Grades, Subject, Category
from django import forms


class MembersCreationForm(forms.Form):
    TYPE_CHOICES = (
        (1, "Profesor"),
        (2, "Preceptor"),
        (3, "Director")
    )

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control col-6'}), label='Nombre')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Apellido')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Contraseña')
    type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), label='Tipo')


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
        labels = {
            'student': 'Alumno',
            'categories': 'Categoría',
            'description': 'Descripción'
        }
        widgets = {
            'student': forms.TextInput(attrs={'class': 'col-6'}),
            'categories': forms.Select(attrs={'class': 'custom-select col-4'}),
            'description': forms.Textarea(attrs={'class': 'col'})
        }


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['deleted_at']
        labels = {
            'first_name': 'Nombres del alumno',
            'last_name': 'Apellidos del alumno',
            'birthday': 'Fecha de nacimiento',
            'course': 'Curso'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control col'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control col'}),
            'birthday': forms.DateTimeInput(attrs={'class': 'custom-select col-sm-5'}),
            'course': forms.Select(attrs={'class': 'custom-select my-1 mr-sm-2 col'}, )
        }


#  year = forms.ChoiceField(choices=TYPE_CHOICES_YEAR, widget=forms.Select(attrs={
#    'class': 'form-control'}), required=True, label='Año')
# division = forms.ChoiceField(choices=TYPE_CHOICES_DIVISION, widget=forms.Select(attrs={
#    'class': 'form-control'}), required=True, label='División')
# shift = forms.ChoiceField(choices=TYPE_CHOICES_YEAR, widget=forms.Select(attrs={
#    'class': 'form-control'}), required=True, label='Turno')


class GradeCreationForm(forms.ModelForm):
    class Meta:
        model = Grades
        exclude = ['deleted_at', 'professor']
        labels = {
            'student': 'Alumno',
            'subject': 'Materia',
            'grade': 'Nota'
        }

        widgets = {
            'student': forms.Select(attrs={'class': 'form-control col'}),
            'subject': forms.Select(attrs={'class': 'custom-select col-md-6'}),
            'grade': forms.TextInput(attrs={'class': 'form-control col-2'})
        }


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ['deleted_at']
        labels = {
            'year': 'Año',
            'division': 'División',
            'shift': 'Turno'
        }

        widgets = {
            'year': forms.TextInput(attrs={'class': 'col'}),
            'division': forms.TextInput(attrs={'class': 'col'}),
            'shift': forms.TextInput(attrs={'class': 'col'})
        }


class SubjectCreationForm(forms.ModelForm):
    class Meta:
        model = Subject
        exclude = ['deleted_at']
        labels = {
            'name': 'Nombre',
            'description': 'Descripción'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'col'}),
            'subject': forms.Textarea(attrs={'class': 'col'})
        }


class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['deleted_at']
        labels = {
            'name': 'Nombre',
            'description': 'Descripción'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col'}),
            'subject': forms.Textarea(attrs={'class': 'card-body'})
        }

# class UserLoginForm(form.Form):
#    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email')
#    password = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Contraseña')
