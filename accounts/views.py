from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile
from django.contrib.auth.models import User
from .forms import EditarPerfilForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('perfil_usuario')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/cambiar_contrasena.html', {'form': form})

class SignUpView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('login')
        return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile.html', {'form': form})


@login_required
def perfil_usuario(request):
    return render(request, 'accounts/perfil.html')



@login_required
def editar_perfil(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = EditarPerfilForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('perfil_usuario')
    else:
        user_form = EditarPerfilForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'accounts/editar_perfil.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })