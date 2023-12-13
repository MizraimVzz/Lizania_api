from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)

#MODELO ADMINISTACION USUARIOS
class UserManager(BaseUserManager):

#CREAR USUARIO
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Falta correo')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

#CREAR SUPER USUARIO
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using =self._db)

        return user

# MODELO USUARIO
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique = True)
    nombres = models.CharField(max_length=50)
    ap_paterno = models.CharField(max_length=50)
    ap_materno = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10, unique = True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    REQUIRED_FIELDS = ['nombres', 'ap_paterno', 'ap_materno', 'telefono']
    USERNAME_FIELD = 'email'