from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    # is_member = models.BooleanField(_('member status'), default=False)
    # is_viewer = models.BooleanField(_('viewer status'), default=False)
    # is_admin = models.BooleanField(_('admin status'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username


# class Project(models.Model):
#     name = models.CharField(max_length=30, blank=False)
#     description = models.TextField(max_length=300, blank=True)
#     creator = models.ManyToManyField(User)
#
#
# class ProjectMember(models.Model):
#     project = models.ForeignKey(Project)
#     user = models.ForeignKey(User)


# class Block(models.Model):
#     name = models.CharField(max_length=30)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     BLOCK_TYPE_CHOICES = (
#         (1, 'to_do'),
#         (2, 'in_progress'),
#         (3, 'done'),
#         (0, 'new')
#     )
#
#     block_type = models.PositiveSmallIntegerField(choices=BLOCK_TYPE_CHOICES)


# class Task(models.Model):
#     name = models.CharField(max_length=30, blank=False)
#     description = models.TextField(max_length=300, blank=True)
#     creator = models.ForeignKey(User)
#     executor = models.ForeignKey(User)
#     block = models.ForeignKey(Block)

# class TaskDocument(models.Model):
#     document = models.FileField(blank=True)
#     creator = models.ForeignKey(User)
#     task = models.ForeignKey(Task)

# class TaskComment(models.Model):
#     body = models.TextField(max_length=100, blank=True)
#     created_at = models.DateTimeField()
#     creator = models.ForeignKey(User)
#     task = models.ForeignKey(Task)
