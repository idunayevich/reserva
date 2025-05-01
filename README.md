# Aplicación Web de Reservas

## Descripción

Este es un sistema desarrollado en python y django web de reservas de restaurantes. Permite el registro y gestión de usuarios.
---

## Tecnologías utilizadas

- Python 3.10+
- Django 4.x
- HTML5/CSS3
- Git

---

## Estructura del proyecto

Aplicación de reservas de restaurantes con autenticación y edición de perfiles en Django.

## Instalación
```bash
git clone <repo>
cd reservas
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Funcionalidades
- Registro/Login/Logout
- Perfil de usuario con avatar
- Alta de restaurante y reservas (CBV con LoginRequired)
- Navegación protegida por estado de autenticación

## Flujo de navegación
- Home (/)
- About (/about/)
- Login (/login/)
- Signup (/signup/)
- Profile (/accounts/profile/)
- Logout (/logout/)