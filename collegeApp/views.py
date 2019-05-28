from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from collegeApp.models import Comment, Grades, Professor, Preceptor, Principal
from django.http import HttpResponseRedirect
from .forms import CommentCreationForm, UpdateGrade, MembersCreationForm


@login_required(login_url="cuentas/login/")
def comments_history(request):
    # Historial de notas
    comments = Comment.objects.all()
    return render(request, 'comments_history.html', {'comments': comments})


@login_required(login_url="cuentas/login/")
def academic_progress(request):
    # Progreso Academico
    grades = Grades.objects.all()
    return render(request, 'academic_progress.html', {'grades': grades})


@login_required(login_url="cuentas/login/")
def see_assistance(request):
    # Asistencia
    return render(request, 'see_assistance.html')


@login_required(login_url="cuentas/login/")
def create_comment(request):
    if request.method == 'POST':
        form = CommentCreationForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/')

    else:
        form = CommentCreationForm()

    return render(request, 'create_comment.html', {'form': form})


@login_required(login_url="cuentas/login/")
def my_comments(request):
    user = request.user
    comments = Comment.objects.filter(author=user)

    return render(request, 'my_comments.html', {'comments': comments})


@login_required(login_url="cuentas/login/")
def update_grade(request):
    if request.method == 'POST':
        form = UpdateGrade(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/')

    else:
        form = UpdateGrade()

    return render(request, 'update_grade.html', {'form': form})


@login_required(login_url="cuentas/login/")
def profile(request):
    user = request.user

    if user.is_superuser:
        return render(request, 'accounts/director_profile.html')

    elif user.is_staff:
        return render(request, 'accounts/preceptor_profile.html')

    else:
        return render(request, 'accounts/teacher_profile.html')


def new_user(request):
    if request.method == 'POST':
        form = MembersCreationForm(request.POST)

        if form.is_valid():

            if form.cleaned_data['type'] == 1:

                Professor.objects.create_user(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )

            elif form.cleaned_data['type'] == 2:

                Preceptor.objects.create_staff_user(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )

            else:

                Principal.objects.create_superuser(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )

            return HttpResponseRedirect('/')

    else:
        form = MembersCreationForm()

    return render(request, 'registration/new_account.html', {'form': form})
