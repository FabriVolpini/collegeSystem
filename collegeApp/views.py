from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from collegeApp.models import Comment, Grades
from django.http import HttpResponseRedirect
from .forms import CommentCreation, UpdateGrade


@login_required(login_url="cuentas/login/")
def comments_history(request):
    # Historial de notas
    comments = Comment.objects.all()
    return render(request, 'comments_history.html', {'comments': comments})


def academic_progress(request):
    # Progreso Academico
    grades = Grades.objects.all()
    return render(request, 'academic_progress.html', {'grades': grades})


def see_assistance(request):
    # Asistencia
    return render(request, 'see_assistance.html')


def assistance(request):
    return render(request, 'assistance.html')


def director(request):
    return render(request, 'director_userprofile.html')


def preceptor(request):
    return render(request, 'preceptor_userprofile.html')


def teacher(request):
    return render(request, 'teacher_userprofile.html')


def base(request):
    return render(request, 'base.html')
# @login_required(login_url="cuentas/login/")
# def home(request):
#   comments = Comment.objects.all()
#  return render(request, 'comments_history.html', {'comments': comments})
def create_comment(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentCreation(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
# if a GET (or any other method) we'll create a blank form
    else:
        form = CommentCreation()

    return render(request, 'create_comment.html', {'form': form})


def my_comments(request):
    return render(request, 'my_comments.html')


def update_grade(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UpdateGrade(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
# if a GET (or any other method) we'll create a blank form
    else:
        form = UpdateGrade()

    return render(request, 'update_grade.html', {'form': form})
