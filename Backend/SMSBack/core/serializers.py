from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    school_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'role', 'school_id']

    def get__id(self, obj):
        return obj.id
    
    def get_school_id(self, obj):
        if obj.role == 'school_admin':
            school = School.objects.filter(admin=obj).first()
            return school._id if school else None
        return None

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.username
        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'role', 'token', 'school_id']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
    
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            # first_name=validated_data.get('first_name', ''),
            # last_name=validated_data.get('last_name', ''),
            role='school_admin'
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class ClassSerializer(serializers.ModelSerializer):
    school = serializers.CharField(source='school.name', read_only=True)
    class Meta:
        model = Class
        fields = '__all__'
    
class SchoolSerializer(serializers.ModelSerializer):
    admin_username = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = School
        fields = ['_id', 'name', 'school_type', 'address', 'phone', 'admin', 'admin_username']

    def get_admin_username(self, obj):
        return obj.admin.username if obj.admin else None

    def create(self, validated_data):
        admin_data = validated_data.pop('admin')
        school = School.objects.create(**validated_data)
        school.admin = admin_data
        school.save()
        return school