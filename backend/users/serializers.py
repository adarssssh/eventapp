from rest_framework import serializers
from django.db.models import Q 
from django.contrib.auth import authenticate
from .models import User, PhoneOTP, ServiceProviderProfile
import random






class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password', 'confirm_password', 'user_type']
        extra_kwargs = {
            'email': {'required': False},
            'phone': {'required': False}
        }
    
    def validate(self, data):
        # Validate password match
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Passwords do not match")
        
        # Validate either email or phone is provided
        if not data.get('email') and not data.get('phone'):
            raise serializers.ValidationError("Either email or phone must be provided")
        
        return data
    
    def create(self, validated_data):
        # Remove confirm_password before creating user
        validated_data.pop('confirm_password')
        
        # Set default username if not provided
        if not validated_data.get('username'):
            validated_data['username'] = validated_data.get('email') or validated_data.get('phone')
        
        user = User.objects.create_user(**validated_data)
        return user








class PhoneOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(
        validators=[User.phone_regex],
        required=True
    )
    
    def generate_otp(self):
        # Generate 6-digit OTP
        return str(random.randint(100000, 999999))
    
    def create_or_update_otp(self, validated_data):
        phone = validated_data['phone']
        otp = self.generate_otp()
        
        # Create or update OTP record
        phone_otp, created = PhoneOTP.objects.update_or_create(
            phone=phone,
            defaults={
                'otp': otp,
                'attempts': 0,
                'is_verified': False
            }
        )
        
        return phone_otp








class ServiceProviderRegistrationSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer()
    
    class Meta:
        model = ServiceProviderProfile
        fields = ['user', 'company_name', 'service_types', 'location']
    
    def create(self, validated_data):
        # Extract user data
        user_data = validated_data.pop('user')
        
        # Create user first
        user_serializer = UserRegistrationSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        
        # Set user type to service provider
        user.user_type = 'provider'
        user.save()
        
        # Create service provider profile
        service_provider_profile = ServiceProviderProfile.objects.create(
            user=user,
            **validated_data
        )
        
        return service_provider_profile
    






class LoginSerializer(serializers.Serializer):
    login_identifier = serializers.CharField()  # Can be email, phone, or username
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        login_identifier = data.get('login_identifier')
        password = data.get('password')
        
        # Try to authenticate with different identifiers
        user = None
        if '@' in login_identifier:
            try:
                user_obj = User.objects.get(email=login_identifier)
                user = authenticate(username=user_obj.username, password=password)
                
            except User.DoesNotExist:
                raise serializers.ValidationError("No user with this email found.")
        else:
            try:
                # Try to find user by phone or username

                user_obj = User.objects.filter(
                    Q(phone=login_identifier) | Q(username=login_identifier)
                ).first()

                # user_obj = User.objects.filter(
                #     models.Q(phone=login_identifier) | 
                #     models.Q(username=login_identifier)
                # ).first()
                
                if user_obj:
                    user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass
        
        if not user:
            raise serializers.ValidationError("Unable to log in with provided credentials")
        
        data['user'] = user
        return data