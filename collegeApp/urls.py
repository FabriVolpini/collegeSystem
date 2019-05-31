from django.urls import path
from . import views

urlpatterns = [
    path('', views.comments_history, name='comments_list'),
    path('misnotas/', views.my_comments),
    path('verAsistencia/', views.see_assistance, name='ver_asistencia'),
    path('lista/', views.student_list, name='lista'),
    path('calificaciones/', views.academic_progress, name='marks'),
    path('perfil/', views.profile, name='profile'),
    path('subircalificaciones/', views.update_grade, name='upgrade_note'),
    path('crearcomentario/', views.create_comment, name='create_comment'),
    path('nuevoUsuario/', views.new_user, name='newUser'),
    path('agregarAlumno/', views.new_student, name='add_student')
]
