from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .models import User, CODE_VERIFIED
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from django.db.models import Q


class SignUpSerializer(serializers.Serializer):
    phone = PhoneNumberField(required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        phone = attrs.pop('phone')
        password = attrs.pop('password')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError(
                detail={'msg': 'Parollar mos emas'},
                code=400
            )
        user = User.objects.filter(Q(phone=phone) & Q(auth_status=CODE_VERIFIED)).first()
        if user is not None:
            raise serializers.ValidationError(
                detail={'msg': 'Ushbu foydalanuvchi allaqachon mavjud'},
                code=400
            )
        attrs['phone'] = phone
        attrs['password'] = password
        return attrs


class SignInSerializer(TokenObtainPairSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'phone',
            'password',
            'tokens'
        )

        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'tokens': {'read_only': True, 'required': False}
        }

    def validate(self, attrs):
        phone = attrs.pop('phone')
        password = attrs.pop('password')
        user = User.objects.filter(Q(phone=phone) & Q(auth_status=CODE_VERIFIED)).first()
        if user is None:
            raise serializers.ValidationError(
                detail={'msg': "Bu raqam ro'yxatdan o'tmagan"},
                code=400
            )
        if not user.check_password(password):
            raise serializers.ValidationError(
                detail={'msg': "Parol noto'g'ri kiritildi"},
                code=400
            )
        attrs['phone'] = str(phone)
        attrs['user_type'] = user.user_type
        attrs.update(user.tokens())

        return attrs


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone',)


class UserProfileSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "phone", "user_type", "count")
        read_only_fields = ('phone',)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
