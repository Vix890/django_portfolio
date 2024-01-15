from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from app.views import *

urlpatterns = [
    path('home/', home_view, name='home'),
    path("info/", info_view, name="info"),
    path("estudios/", estudios_view, name="estudios"),
    
    path("experiencias/", experiences_view, name="experiencias"),
    path('experiencias/detail/<int:pk>', experience_details_view, name='experience_details'),
    path('experiencias/edit/<int:pk>', ExperienceEditView.as_view(), name='experience_edit'),
    path('experiencias/create/', ExperienceCreateView.as_view(), name='experience_create'),
    path('experiencias/delete/<int:pk>', experience_delete_view, name='experience_delete'),
    path('experiences/restore', experience_restore_view, name='experiences_restore'),
    
    path('seguidores/', seguidores_view, name='seguidores'),
    path('seguidores/detail/<int:pk>', seguidor_details_view, name='seguidor_details'),
    path('seguidores/edit/<int:pk>', SeguidorEditView.as_view(), name='seguidor_edit'),
    path('seguidores/create/', SeguidorCreateView.as_view(), name='seguidor_create'),
    path('seguidores/delete/<int:pk>', seguidor_delete_view, name='seguidor_delete'),
    path('seguidores/restore', seguidor_restore_view, name='seguidores_restore'),
    
    
    path('seguidos/', seguidos_view, name='seguidos'),
    path('seguidos/detail/<int:pk>', seguido_details_view, name='seguido_details'),
    path('seguidos/edit/<int:pk>', SeguidoEditView.as_view(), name='seguido_edit'),
    path('seguidos/create/', SeguidoCreateView.as_view(), name='seguido_create'),
    path('seguidos/delete/<int:pk>', seguidor_delete_view, name='seguido_delete'),
    path('seguidos/restore', seguidos_restore_view, name='seguidos_restore'),
    
    path('notificacines/', notificaciones_view, name='notificaciones'),
    path('notificaciones/delete/<int:pk>', notificacion_delete_view, name='notificacion_delete'),
    path('notificaciones/restore', notificaciones_restore_view, name='notificaciones_restore'),
    
    path("register/", register_view.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name='login.html'), name="login"),
    path("logout/", LogoutView.as_view(template_name='logout.html'), name="logout"),
]   