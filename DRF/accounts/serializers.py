from rest_framework import serializers
from django.contrib.auth.models import User


def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('The email entered should not be admin')


def exists_email(value):
    user = User.objects.filter(email=value)
    if user:
        raise serializers.ValidationError('The email entered already exists')


class UserRegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = User
        fields = ('username','email','password','password2')
        extra_kwargs = {
            'password':{'write_only':True},
            'email':{'validators':(clean_email,exists_email)}
        }

    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)

    def validate_username(self,value):
        if value == 'admin':
            raise serializers.ValidationError('You cant use admin')
        return value

    def validate(self,data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords must match')
        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
