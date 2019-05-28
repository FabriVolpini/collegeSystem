from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import PasswordInput
from .models import CustomUser, Category, Course, Comment
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


# class CommentCreationForm(forms.Form):
#     CATEGORY_CHOICES = Category.objects.all().__str__()
#     COURSE_CHOICES = Course.objects.all().__str__()
#
#     first_name = forms.CharField(label='Nombre del Alumno', max_length=100)
#     last_name = forms.CharField(label='Apellido del Alumno', max_length=100)
#     course = forms.ChoiceField(label='Año', choices=COURSE_CHOICES, required=True)
#     category = forms.MultipleChoiceField(label='Categorías', choices=CATEGORY_CHOICES, required=True)
#     description = forms.CharField(label='Descripción')

class CommentCreationForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = []


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
