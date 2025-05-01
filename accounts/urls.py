from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView, profile_view
from .views import cambiar_contrasena

urlpatterns = [
    path('', views.perfil_usuario, name='perfil_usuario'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', views.editar_perfil, name='editar_perfil'),
    path('profile/change-password/', views.cambiar_contrasena, name='cambiar_contrasena'),
]
