from django.urls import path
from . import views

urlpatterns = [
    # path('', home),

    path('', views.comments_history, name='comments_list'),

    path('asistencia/', views.see_assistance, name='assistance_list'),
    path('calificaciones/', views.academic_progress, name='marks'),

    path('perfil/', views.teacher),
    # path('',views.create_comment, name = 'comment_creation')

]
