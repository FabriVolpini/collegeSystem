from django.urls import path
from . import views

urlpatterns = [
    path('', views.comments_history, name='comments_list'),
    path('misnotas/', views.my_comments),
    path('verAsistencia/', views.see_assistance, name='assistance_list'),
    path('lista', views.student_list),
    path('calificaciones/', views.academic_progress, name='marks'),
    path('perfil/', views.profile, name='profile'),
    path('subircalificaciones/', views.update_grade, name='upgrade_note'),
    # path('',views.create_comment, name = 'comment_creation')
    path('crearcomentario/', views.create_comment, name='create_comment'),
    path('nuevoUsuario/', views.new_user, name='newUser'),
]
