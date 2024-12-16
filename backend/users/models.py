# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('general', 'General User'),
        ('provider', 'Service Provider')
    )
    
    SOCIAL_PROVIDER_CHOICES = (
        ('email', 'Email'),
        ('google', 'Google'),
        ('facebook', 'Facebook'),
        ('phone', 'Phone')
    )
    
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', 
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    
    phone = models.CharField(
        validators=[phone_regex], 
        max_length=17, 
        blank=True, 
        null=True, 
        unique=True
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    social_provider = models.CharField(
        max_length=20, 
        choices=SOCIAL_PROVIDER_CHOICES, 
        default='email'
    )
    is_phone_verified = models.BooleanField(default=False)
    social_uid = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.username





class PhoneOTP(models.Model):
    phone = models.CharField(max_length=17, unique=True)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    attempts = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    
    def is_expired(self):
        # OTP expires after 10 minutes
        return (timezone.now() - self.created_at).total_seconds() > 600
    
    def __str__(self):
        return f"OTP for {self.phone}"





class ServiceProviderProfile(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('venue', 'Venue'),
        ('sound', 'Sound System'),
        ('artist', 'Artist'),
        ('decoration', 'Decoration'),
        ('security', 'Security'),
        ('catering', 'Catering')
    ]
    
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        primary_key=True,
        related_name='service_provider_profile'
    )
    company_name = models.CharField(max_length=200)
    service_types = models.JSONField(default=list)  # Allows multiple service types
    location = models.CharField(max_length=300)
    
    def __str__(self):
        return f"{self.company_name} - {self.user.username}"
    


