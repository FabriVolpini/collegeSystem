from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from collegeApp.models import Comment, Grades


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

# @login_required(login_url="cuentas/login/")
# def home(request):
#   comments = Comment.objects.all()
#  return render(request, 'comments_history.html', {'comments': comments})


def createcomment(request):
    return render(request, 'create_comment.html')


def my_comments(request):
    return render(request, 'my_comments.html')


def upgrade_grade(request):
    return render(request, 'update_grade.html')