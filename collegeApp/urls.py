from django.urls import path
from . import views

urlpatterns = [
    path('misnotas/', views.my_comments),
    path('', views.comments_history, name='comments_list'),
    path('asistencia/', views.see_assistance, name='assistance_list'),
    path('calificaciones/', views.academic_progress, name='marks'),
    path('perfil/', views.teacher),
    path('subircalificaciones', views.upgrade_grade),
    # path('',views.create_comment, name = 'comment_creation')
    path('crearcomentario', views.createcomment),
]
