from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self,email,password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        email = email.lower()
        
        user = self.model(
            email = email,
            **kwargs
        )
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self,email,password=None, **kwargs):
        user = self.create_user(
            email,
            password = password,
            **kwargs
        )
        
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user
    
class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=255)
    verified_email = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    affiliate_id = models.CharField(max_length=30, blank=True, null=True)
    store_id = models.CharField(max_length=30, blank=True, null=True)
    store_name = models.CharField(max_length=30, blank=True, null=True)
    
    address= models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    zip = models.CharField(max_length=30, blank=True, null=True)
    region = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    time_zone = models.CharField(max_length=30, blank=True, null=True)
    
    current_browser = models.CharField(max_length=30, blank=True, null=True)
    current_device = models.CharField(max_length=30, blank=True, null=True)
    
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    
    def __str__(self):
        return self.email

