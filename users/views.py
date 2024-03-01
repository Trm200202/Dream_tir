from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import SignUpSerializer, SignInSerializer, PhoneSerializer, LogoutSerializer
from .models import User, CODE_VERIFIED
from datetime import datetime
from rest_framework import permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db.models import Q
from . import serializers

from .utils import send_verification_code
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from . import permission
from app import models


class SignUpAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = SignUpSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data.get('phone')
        password = serializer.validated_data.get('password')
        user = User.objects.filter(phone=phone).first()
        if user is None:
            user = User.objects.create_user(phone=phone, password=password)
        else:
            user.set_password(password)
            user.save()
        code = user.create_verify_code()
        send_verification_code(user.phone, code)

        return Response(
            data={
                'success': True,
                "user_id": user.id,
                'auth_status': user.auth_status,
                "access": user.tokens()['access'],
                "refresh": user.tokens()['refresh']
            },
            status=201
        )


class VerifyAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user, code = self.request.user, self.request.data.get('code')

        self.check_verify(user, code)
        return Response(
            data={
                'success': True,
                'auth_status': user.auth_status,
                "access": user.tokens()['access'],
                "refresh": user.tokens()['refresh']
            },
            status=200
        )

    @staticmethod
    def check_verify(user, code):
        verifies = user.verify_codes.filter(
            expiration_time__gte=datetime.now(),
            code=code,
            is_confirmed=False
        )
        if not verifies.exists():
            data = {
                'msg': 'Kod eskirgan yoki noto\'g\'ri'
            }
            raise ValidationError(data)
        verifies.update(is_confirmed=True)
        user.auth_status = CODE_VERIFIED
        user.save()


class SignInAPIView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SignInSerializer


class GetNewVerification(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        self.check_verification(user)
        code = user.create_verify_code()
        send_verification_code(user.phone, code)
        return Response(
            data={
                'success': True,
                'auth_status': user.auth_status,
                "access": user.tokens()['access'],
                "refresh": user.tokens()['refresh']
            },
            status=200
        )

    @staticmethod
    def check_verification(user):
        if user.verify_codes.filter(Q(expiration_time__gte=datetime.now()) & Q(is_confirmed=True)).exists():
            data = {
                'msg': 'Sizga kod allaqachon yuborilgan'
            }
            raise ValidationError(data, 400)


# Reset Password
class ResetPasswordAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        phone = self.request.data.get('phone')
        user = User.objects.filter(phone=phone).first()
        if user is None:
            data = {
                'msg': 'Ushbu telefon raqami topilmadi'
            }
            raise ValidationError(data, 400)
        code = user.create_verify_code()
        send_verification_code(user.phone, code)
        return Response(
            data={
                'success': True,
                'auth_status': user.auth_status,
                "access": user.tokens()['access'],
                "refresh": user.tokens()['refresh']
            },
            status=200
        )


class ResetPasswordVerifyAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user, code = self.request.user, self.request.data.get('code')
        self.check_verify(user, code)
        return Response(
            data={
                'success': True,
                'auth_status': user.auth_status,
                "access": user.tokens()['access'],
                "refresh": user.tokens()['refresh']
            },
            status=200
        )

    @staticmethod
    def check_verify(user, code):
        verifies = user.verify_codes.filter(
            expiration_time__gte=datetime.now(),
            code=code,
            is_confirmed=False
        )
        if not verifies.exists():
            data = {
                'msg': 'Kod eskirgan yoki noto\'g\'ri'
            }
            raise ValidationError(data)
        verifies.update(is_confirmed=True)
        user.auth_status = CODE_VERIFIED
        user.save()


class ResetPasswordConfirmAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user, password = self.request.user, self.request.data.get('password')
        user.set_password(password)
        user.save()
        return Response(
            data={
                'success': True,
                'auth_status': user.auth_status,
                "access": user.tokens()['access'],
                "refresh": user.tokens()['refresh']
            },
            status=200
        )


class PhoneRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = PhoneSerializer

    def get_object(self):
        return self.request.user


class UserProfileRetrieveAPIView(RetrieveUpdateAPIView):
    permission_classes = (permission.ProfilePermission,)
    serializer_class = serializers.UserProfileSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        teacher = self.request.user
        instance = self.get_object()
        if teacher.user_type == 'teacher':
            answers = models.StudentAnswer.objects.filter(lesson__chapter__course__support_teacher=teacher,
                                                          lesson_result__mark__isnull=True)
            answer_count = answers.exclude(Q(lesson__task__in=['', None]) & Q(lesson__task_description="")).count()
            instance.count = answer_count
        else:
            instance.count = -1
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ChangePasswordAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        user = request.user
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response({"message": "Parol muvaffaqiyatli yangilandi"}, status=200)
        return Response({"msg": "Eski parol xato kiritildi"}, status=400)


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
