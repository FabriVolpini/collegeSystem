from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from collegeApp.models import Comment, Grades, Professor, Course, CustomUser, Student, Phone
from django.http import HttpResponseRedirect
from .forms import CommentCreationForm, GradeCreationForm, MembersCreationForm, StudentCreationForm, CourseCreationForm, \
    SubjectCreationForm, CategoryCreationForm, PhoneCreationForm


@login_required(login_url="cuentas/login/")
def comments_history(request):
    user = request.user
    # Historial de notas
    comments = Comment.objects.all().order_by('-date')

    return render(request, 'comments_history.html', {'comments': comments, 'user': user})


@login_required(login_url="cuentas/login/")
def academic_progress(request):
    # Progreso Academico
    # asd = Course.
    # Course.division.
    # try:
    #     division = Course.objects.
    # Course.objects.get(division=)
    # asd = Course.objects.filter(year="FIR")

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
    comments = Comment.objects.filter(author=user)

    return render(request, 'accounts/profile.html', {'comments': comments, 'user': user})

    # if user.is_superuser:
    #     return render(request, 'accounts/director_profile.html', {'comments': comments, 'user': user})
    #
    # elif user.is_staff:
    #     return render(request, 'accounts/preceptor_profile.html', {'comments': comments})
    #
    # else:
    #     return render(request, 'accounts/teacher_profile.html', {'comments': comments})


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
def student_list(request):
    students = Student.objects.all()
    return render(request, 'assistance.html', {'students': students})


@login_required(login_url="cuentas/login/")
def assistance(request):
    if request.method == 'POST':  # si el usuario está enviando el formulario con datos
        form = AssistanceForm(request.POST)  # Bound form
        if form.is_valid():
            presence = form.save()  # Guardar los datos en la base de datos
        return HttpResponseRedirect(reverse('lista'))
    else:
        form = AssistanceForm()  # Unbound form
    return render(request, 'assistance.html', {'form': form})


@login_required(login_url="cuentas/login/")
def student_info(request, pk):
    student = Student.objects.get(id=pk)
        # .filter(id=pk)\
        # .select_related("course")
    # student.phone.number
    # student.phone.
    # phone = Phone.objects.filter(student=student)
    # # p
    # phone = Phone.objects.get(student=student)
    comments = Comment.objects.filter(student=student.id)
    return render(request, 'student_info.html', {'student': student, 'comments': comments})

    return render(request, 'student_info.html', {'student': student, 'comments': comments})


@login_required(login_url="cuentas/login/")
def new_phone(request):
    if request.method == 'POST':
        form = PhoneCreationForm(request.POST)

        if form.is_valid():
            phone = form.save(commit=False)
            phone.save()

            return HttpResponseRedirect('/')

    else:
        form = PhoneCreationForm()

    return render(request, 'add_phones.html', {'form': form})

