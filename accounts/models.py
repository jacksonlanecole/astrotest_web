from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
            verbose_name='first name',
            max_length=255,
            )
    last_name = models.CharField(
            verbose_name='last name',
            max_length=255,
            )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
            'first_name',
            'last_name',
            ]

    def get_full_name(self):
        '''
        '''
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.first_name + " " + self.last_name

    #def has_perm(self, perm, obj=None):
    #    """Does the user have a specific permission?"""
    #    # Simplest possible answer: Yes, always
    #    return True

    #def has_module_perms(self, app_label):
    #    """Does the user have permissions to view the app `app_label`?"""
    #    # Simplest possible answer: Yes, always
    #    return True
