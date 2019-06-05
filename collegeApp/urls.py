from django.urls import path
from . import views

urlpatterns = [
    path('', views.comments_history, name='comments_list'),
    path('misnotas/', views.my_comments),
    path('verAsistencia/', views.see_assistance, name='ver_asistencia'),
    path('lista/', views.student_list, name='lista'),
    path('calificaciones/', views.academic_progress, name='marks'),
    path('perfil/', views.profile, name='profile'),
    path('subir-calificaciones/', views.update_grade, name='upgrade_grade'),
    path('crear-comentario/', views.create_comment, name='create_comment'),
    path('nuevo-usuario/', views.new_user, name='newUser'),
    path('agregar-alumno/', views.new_student, name='add_student'),
    path('agregar-curso/', views.new_course, name='newCourse'),
    path('agregar-materia/', views.new_subject, name='newSubject'),
    path('agregar-categoria/', views.new_category, name='newCategory'),
    path('informacion-alumno/<int:pk>', views.student_info, name='studentInfo')

]
