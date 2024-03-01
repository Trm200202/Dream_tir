import random
from datetime import datetime, timedelta

from rest_framework_simplejwt.tokens import RefreshToken
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager

STUDENT, TEACHER = ('student', 'teacher')
NEW, CODE_VERIFIED = (
    'new',
    'code_verified',
)

PHONE_EXPIRE = 1


class UserConfirmation(models.Model):
    code = models.CharField(max_length=4)
    user = models.ForeignKey('users.User', models.CASCADE, 'verify_codes')
    expiration_time = models.DateTimeField(null=True)
    is_confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.expiration_time = datetime.now() + timedelta(minutes=PHONE_EXPIRE)
        super(UserConfirmation, self).save(*args, **kwargs)


class UserManager(AbstractUserManager):
    def _create_user(self, phone, password, **extra_fields):
        """
        Create and save a user with the given phone and password.
        """
        if not phone:
            raise ValueError("The given phone number must be set")

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(phone, password, **extra_fields)

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, password, **extra_fields)


class User(AbstractUser):
    REQUIRED_FIELDS = []
    email = None
    username = None

    USER_ROLES = (
        (STUDENT, STUDENT),
        (TEACHER, TEACHER),
    )

    AUTH_STATUS = (
        (NEW, NEW),
        (CODE_VERIFIED, CODE_VERIFIED),
    )

    phone = PhoneNumberField(unique=True, verbose_name="Phone")
    user_type = models.CharField(max_length=20, choices=USER_ROLES, default=STUDENT)
    auth_status = models.CharField(max_length=20, choices=AUTH_STATUS, default=NEW)
    objects = UserManager()
    USERNAME_FIELD = 'phone'

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.phone} {self.id}"

    def create_verify_code(self):
        code = "".join(str(random.randint(0, 100) % 10) for _ in range(4))
        if UserConfirmation.objects.filter(user=self).exists():
            UserConfirmation.objects.filter(user=self).update(
                code=code,
                is_confirmed=False,
                expiration_time=datetime.now() + timedelta(minutes=PHONE_EXPIRE)
            )
        else:
            UserConfirmation.objects.create(user=self, code=code)
        return code

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
