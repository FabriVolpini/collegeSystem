from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from collegeApp.models import Comment, Grades, Professor, Course, CustomUser
from django.http import HttpResponseRedirect
from .forms import CommentCreationForm, GradeCreationForm, MembersCreationForm, StudentCreationForm, CourseCreationForm, \
    SubjectCreationForm, CategoryCreationForm


@login_required(login_url="cuentas/login/")
def comments_history(request):
    # Historial de notas
    comments = Comment.objects.all()
    return render(request, 'comments_history.html', {'comments': comments})


@login_required(login_url="cuentas/login/")
def academic_progress(request):
    # Progreso Academico
    #asd = Course.
    #Course.division.
    # try:
    #     division = Course.objects.
    # Course.objects.get(division=)
    #asd = Course.objects.filter(year="FIR")

    course = Course.objects.all()
    grades = Grades.objects.all()
    return render(request, 'academic_progress.html', {'grades': grades, 'course': course})


@login_required(login_url="cuentas/login/")
def see_assistance(request):
    # Asistencia
    return render(request, 'see_assistance.html')


@login_required(login_url="cuentas/login/")
def create_comment(request):
    if request.method == 'POST':
        form = CommentCreationForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()

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
        form = GradeCreationForm(request.POST)

        if form.is_valid():
            grade = form.save(commit=False)
            grade.professor = request.user
            grade.save()

            return HttpResponseRedirect('/')

    else:
        form = GradeCreationForm()

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


@login_required(login_url="cuentas/login/")
def new_student(request):
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            student.save()

            return HttpResponseRedirect('/')

    else:
        form = StudentCreationForm()

    return render(request, 'add_student.html', {'form': form})


@login_required(login_url="cuentas/login/")
def new_course(request):
    if request.method == 'POST':
        form = CourseCreationForm(request.POST)

        if form.is_valid():
            course = form.save(commit=False)
            course.save()

            return HttpResponseRedirect('/')

    else:
        form = CourseCreationForm()

    return render(request, 'add_course.html', {'form': form})


@login_required(login_url="cuentas/login/")
def new_subject(request):
    if request.method == 'POST':
        form = SubjectCreationForm(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            student.save()

            return HttpResponseRedirect('/')

    else:
        form = SubjectCreationForm()

    return render(request, 'add_subject.html', {'form': form})


@login_required(login_url="cuentas/login/")
def new_category(request):
    if request.method == 'POST':
        form = CategoryCreationForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.save()

            return HttpResponseRedirect('/')

    else:
        form = CategoryCreationForm()

    return render(request, 'add_category.html', {'form': form})


def new_user(request):
    if request.method == 'POST':
        form = MembersCreationForm(request.POST)

        if form.is_valid():

            if form.cleaned_data['type'] == 1:

                CustomUser.objects.create_user(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )

            elif form.cleaned_data['type'] == 2:

                CustomUser.objects.create_staff_user(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )

            else:

                CustomUser.objects.create_superuser(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )

            return HttpResponseRedirect('/')

    else:
        form = MembersCreationForm()

    return render(request, 'registration/new_account.html', {'form': form})


@login_required(login_url="cuentas/login/")
def training(request):
    # Capacitacion
    return render(request, 'teacher_training.html')
