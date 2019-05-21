from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from collegeApp.models import Comment

# Create your views here.

def comments_history(request):
    return render(request, 'comments_history.html', {})


def see_assistance(request):
    return render(request, 'see_assistance.html')


def academic_progress(request):
    return render(request, 'academic_progress.html')


def assistance(request):
    return render(request, 'assistance.html')


def menu(request):
    return render(request, 'menu.html')


def director(request):
    return render(request, 'director_userprofile.html')


def preceptor(request):
    return render(request, 'preceptor_userprofile.html')


def teacher(request):
    return render(request, 'teacher_userprofile.html')

@login_required(login_url="accounts/login/")
def home(request):
    comments = Comment.objects.all()
    return render(request, 'comments_history.html', {'comments': comments})
