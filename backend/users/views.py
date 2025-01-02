
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from .models import User, PhoneOTP
from .serializers import (
    UserRegistrationSerializer, 
    PhoneOTPSerializer, 
    ServiceProviderRegistrationSerializer,
    LoginSerializer
)

# Third-party integration (example with hypothetical packages)
# from social_django.utils import psa
# import firebase_admin  # For OTP verification

class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]



    def get_serializer_class(self):
        if self.action == 'register_general_user':
            return UserRegistrationSerializer
        elif self.action == 'send_phone_otp':
            return PhoneOTPSerializer
        elif self.action == 'verify_phone_otp':
            return PhoneOTPSerializer  # Same serializer can be reused
        elif self.action == 'register_service_provider':
            return ServiceProviderRegistrationSerializer
        elif self.action == 'login':
            return LoginSerializer
        # Add serializers for other actions if necessary
        return super().get_serializer_class()
    


    
    @action(detail=False, methods=['POST'])

    def register_general_user(self, request):
        
        serializer = UserRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            # Generate and send OTP
            otp = "123456"
            phone_otp, _ = PhoneOTP.objects.update_or_create(
                phone=user.phone, defaults={'otp': otp}
            )
            
            # For production, send SMS using an SMS gateway (e.g., Twilio)
            # Placeholder: return OTP in response for testing
            return Response({
                'message': 'User registered successfully. OTP has been sent to your phone.',
                'user_id': user.id,
                'otp': phone_otp.otp  # Remove this line in production
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def register_general_user(self, request):
    #     serializer = UserRegistrationSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user = serializer.save()
    #         return Response({
    #             'message': 'User registered successfully',
    #             'user_id': user.id
    #         }, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['POST'])
    def send_phone_otp(self, request):
        serializer = PhoneOTPSerializer(data=request.data)
        if serializer.is_valid():
            phone_otp = serializer.create_or_update_otp(serializer.validated_data)
            
            # In production, integrate with SMS gateway like Twilio
            # For now, we'll return OTP (remove in production)
            return Response({
                'message': 'OTP sent successfully',
                'otp': phone_otp.otp  # Remove in production
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['POST'])
    def verify_phone_otp(self, request):
        phone = request.data.get('phone')
        otp = request.data.get('otp')
        
        try:
            phone_otp = PhoneOTP.objects.get(phone=phone, otp=otp)
            
            if phone_otp.is_expired():
                return Response({
                    'message': 'OTP has expired'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Mark phone as verified and create user if not exists
            user, created = User.objects.get_or_create(
                phone=phone,
                defaults={
                    'username': phone,
                    'is_phone_verified': True,
                    'user_type': 'general'
                }
            )
            
            # Clear OTP after successful verification
            phone_otp.delete()
            
            return Response({
                'message': 'Phone verified successfully',
                'user_id': user.id,
                'created': created
            }, status=status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return Response({
                'message': 'Invalid OTP'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['POST'])
    def register_service_provider(self, request):
        serializer = ServiceProviderRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            service_provider = serializer.save()
            return Response({
                'message': 'Service Provider registered successfully',
                'user_id': service_provider.user.id
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['POST'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({
                'message': 'Login successful',
                'user_id': user.id,
                'user_type': user.user_type
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Social Login Integration (Placeholder)
    @action(detail=False, methods=['POST'])
    # @psa('social:complete')
    def social_auth(self, request, backend):
        # This is a placeholder for social authentication
        # You'll need to integrate with social-auth-app-django
        try:
            user = request.backend.do_auth(request.data.get('access_token'))
            return Response({
                'message': 'Social login successful',
                'user_id': user.id
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'message': 'Social login failed',
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)