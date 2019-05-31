from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import PasswordInput
from .models import CustomUser, Comment, Student, Course, Grades
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


class CourseCreationForm(forms.ModelForm):

    class Meta:
        model = Course
        exclude = ['deleted_at']


class UpdateGrade(forms.ModelForm):

    class Meta:
        model = Grades
        exclude = ['deleted_at', 'professor']



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
