from django.urls import path
from . import views

urlpatterns = [
    #path('', home),
    path('', views.comments_history, name='comment_list'),
    path('asistencia/', views.see_assistance),
    path('perfil/', views.teacher),
    #path('',views.create_comment, name = 'comment_creation')

]














































































