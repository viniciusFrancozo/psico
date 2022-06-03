from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, cargo, password=None):
        if not email:
            raise ValueError('O usuário deve conter um e-mail válido')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            cargo=cargo
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name,cargo, last_name, password=None):
        if not email:
            raise ValueError('O usuário deve conter um e-mail válido')

        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            cargo=cargo,
            last_name=last_name,
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True

        user.save(using=self._db)
        return user


class Account(AbstractUser, PermissionsMixin):
    """ New user model for attending elderly demands """

    # Account registration data
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30)
    first_name = models.CharField(_('Nome'), max_length=150)
    last_name = models.CharField(_('Sobrenome'), max_length=150)

    # Data required for serving or request a service
    cargo = models.CharField(max_length=15, choices=(
            ('', 'Cargo'),
            ('PE', 'Cliente'),
            ('PI', 'Psicologo')
        ), default=''
    )

    # Required Django AbstractUser model fields
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'cargo']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Pessoa(models.Model):
    # one-to-one link with the Account model (used to create a "profile" for the Account model)
    pessoa = models.OneToOneField(Account, on_delete=models.CASCADE)

    # Voluntario data for serving
    agenda = models.CharField(max_length=10,
        choices=(
            ('', 'Seu Horário Preferido'),
            ('MANHA', 'Manhã'),
            ('TARDE', 'Tarde'),
            ('NOITE', 'Noite'),
            ('ANY', 'Qualquer Horário')
        ), default=''
    )
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.pessoa.email


class Psicologo(models.Model):
    # one-to-one link with the Account model (used to create a "profile" for the Account model)
    psicologo = models.OneToOneField(Account, on_delete=models.CASCADE)

    # Voluntario data for serving
    em_atendimento = models.BooleanField(default=False)

    def __str__(self):
        return self.psicologo.email