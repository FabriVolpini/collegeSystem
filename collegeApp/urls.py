from django.urls import path
from . import views

urlpatterns = [
    path('', views.comments_history, name='comments_list'),
    path('mis-notas/', views.my_comments),
    path('asistencia/', views.see_assistance, name='assistance_list'),
    path('calificaciones/', views.academic_progress, name='marks'),
    path('perfil/', views.profile, name='profile'),
    path('subir-calificaciones/', views.update_grade, name='upgrade_note'),
    # path('',views.create_comment, name = 'comment_creation')
    path('crear-comentario/', views.create_comment, name='create_comment'),
    path('nuevo-usuario/', views.new_user, name='newUser'),
]
