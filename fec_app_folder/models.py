from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
import uuid as uuid_lib


class CustomUserManager(UserManager):
  use_in_migrations = True
  def _create_user(self, username, email, password, **extra_fields):
    if not email:
      raise ValueError('The given email must be set')
    email = self.normalize_email(email)
    username = self.model.normalize_username(username)
    user = self.model(username, email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_user(self, username, email, password=None, **extra_fields):
      extra_fields.setdefault('is_staff', False)
      extra_fields.setdefault('is_superuser', False)
      return self._create_user(username, email, password, **extra_fields)

  def create_superuser(self, username, email, password, **extra_fields):
      extra_fields.setdefault('is_staff', True)
      extra_fields.setdefault('is_superuser', True)
      
      if extra_fields.get("is_staff") is not True:
          raise ValueError('Superuser must have is_staff=True.')
      if extra_fields.get("is_superuser") is not True:
          raise ValueError('Superuser must have is_superuser=True.')
      return self._create_user(username, email, password, **extra_fields)


class UserDB(AbstractBaseUser, PermissionsMixin):
    """Custom User"""
    class Meta:
        verbose_name = 'UserDB'
        verbose_name_plural = 'UserDB'

    uuid = models.UUIDField(default=uuid_lib.uuid4, primary_key=True, editable=False)     # 管理ID
    username_validators = UnicodeUsernameValidator()     #不正な文字列が含まれていないかチェック
    username = models.CharField(max_length=15, unique=True, help_text="ニックネームを入力してください")     #ユーザ氏名
    email = models.EmailField(unique=True, null=False, blank=False)     #メールアドレス = これで認証する
    is_active = models.BooleanField(default=True) # アクティブ権限
    is_staff = models.BooleanField(default=False) # スタッフ権限
    is_superuser = models.BooleanField(default=False) # 管理者権限
    date_joined = models.DateTimeField(default=timezone.now) # アカウント作成日時
    password_changed = models.BooleanField(default=False, null=True) # パスワードを変更したかどうかのフラグ
    password_changed_date = models.DateTimeField(null=True) # 最終パスワード変更日時

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELD = ['email', 'username']

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.uuid

    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.username