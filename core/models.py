"""
Database models
"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    """Manager for users"""
    
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    
    def __str__(self) -> str:
        return f"{self.name}さん"
    
    
class SNS(models.Model):
    """SNS accounts"""
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sns',
    )
    
    twitter = models.URLField(max_length=255, blank=True)
    facebook = models.URLField(max_length=255, blank=True)
    instagram = models.URLField(max_length=255, blank=True)
    threads = models.URLField(max_length=255, blank=True)
    linkedin = models.URLField(max_length=255, blank=True)
    line = models.URLField(max_length=255, blank=True)
    discord = models.URLField(max_length=255, blank=True)
    
    def __str__(self) -> str:
        return f"SNS of {self.user.name}"
    
    
class Other(models.Model):
    """Other SNS accounts"""
    sns = models.ForeignKey(
        SNS,
        on_delete=models.CASCADE,
        related_name='others',
    )
    
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    
    def __self__(self) -> str:
        return f"{self.sns.user.name}'s {self.name}"