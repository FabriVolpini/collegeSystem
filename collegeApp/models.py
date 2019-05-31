from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from .managers import SoftDeletionManager, CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, null=False, blank=False, default='Jane')
    last_name = models.CharField(max_length=50, null=False, blank=False, default='Doe')
    email = models.EmailField('email address', unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()


class Course(SoftDeletionModel):
    YEAR_IN_SCHOOL_CHOICES = (
        ('Primer año', 'Primer Año'),
        ('Segundo año', 'Segundo Año'),
        ('Tercer año', 'Tercer Año'),
        ('Cuarto año', 'Cuarto Año'),
        ('Quinto año', 'Quinto Año'),
        ('Sexto año', 'Sexto Año'),
        ('Septimo año', 'Septimo Año'),
    )

    DIVISION_IN_SCHOOL_CHOICES = (
        ('A', 'Division A'),
        ('B', 'Division B'),
        ('C', 'Division C'),
        ('D', 'Division D'),
        ('E', 'Division E'),
    )

    SHIFT_IN_SCHOOL_CHOICES = (
        ('turno mañana', 'Turno mañana'),
        ('turno tarde', 'Turno tarde'),
        ('turno noche', 'Turno noche'),
    )

    id_course = models.AutoField(primary_key=True)

    year = models.CharField(
        max_length=50,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default='Primer Año',
    )

    division = models.CharField(
        max_length=50,
        choices=DIVISION_IN_SCHOOL_CHOICES,
        default='A',
    )

    shift = models.CharField(
        max_length=50,
        choices=SHIFT_IN_SCHOOL_CHOICES,
        default='turno mañana',
    )

    class Meta:
        unique_together = ("year", "division", "shift")

    def __str__(self):
        return "%s %s %s" % (self.year, self.division, self.shift)


class Subject(SoftDeletionModel):
    id_subject = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Professor(SoftDeletionModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="professor", primary_key=True)
    subjects = models.ManyToManyField(
        Subject,
        related_name="subjects",
        blank=True)

    def __str__(self):
        return "Profesor: " + self.user.first_name + " " + self.user.last_name


class Student(SoftDeletionModel):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(
        max_length=50,
        blank=False,
        null=False)
    last_name = models.CharField(
        max_length=50,
        blank=False,
        null=False)
    birthday = models.DateField()
    course = models.ForeignKey(
        Course,
        related_name="student",
        on_delete=models.CASCADE,
        default='')

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Category(SoftDeletionModel):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Comment(SoftDeletionModel):
    id = models.AutoField(primary_key = True)
    student = models.ForeignKey(
        Student,
        related_name="comments",
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="comments")
    categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name="categories")
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.student)


class Phone(SoftDeletionModel):
    id = models.AutoField(primary_key = True)
    number = models.CharField(max_length=50, blank = False, null = False)
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name = "phone")

    def __str__(self):
        return self.number


class CourseHistory(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    id_course = models.ForeignKey(Course, null = True, on_delete = models.SET_NULL)
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name = "courseHistory")

    def __str__(self):
        return str(self.id)


class AcademicHistory(SoftDeletionModel):
    id = models.AutoField(primary_key = True)
    id_course = models.ForeignKey(Course, null = True, on_delete = models.SET_NULL)
    subject = models.ForeignKey(Subject, null = True, on_delete = models.SET_NULL)
    cycle = models.IntegerField()

    def __str__(self):
        return str(self.id)


class Grades(SoftDeletionModel):
    GRADE_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
    )

    id = models.AutoField(primary_key=True)
    professor = models.ForeignKey(
        Professor,
        null=True,
        on_delete=models.SET_NULL)
    student = models.ForeignKey(
        Student,
        null=True,
        on_delete=models.SET_NULL)
    subject = models.ForeignKey(
        Subject,
        null=True,
        on_delete=models.SET_NULL)
    grade = models.CharField(
        max_length=2,
        choices=GRADE_CHOICES,
        default="0",
    )

    def __str__(self):
        return self.grade


class Presence(SoftDeletionModel):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    student = models.OneToOneField(
        Student,
        null=True,
        on_delete=models.SET_NULL)
    preceptor = models.OneToOneField(
        CustomUser,
        null=True,
        on_delete=models.SET_NULL)
    presence = models.NullBooleanField()

    def __str__(self):
        return "%s %s %s" % (self.date, self.student, self.presence)