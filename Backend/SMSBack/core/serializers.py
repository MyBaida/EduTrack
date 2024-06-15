from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken


# class UserSerializer(serializers.ModelSerializer):
#     name = serializers.SerializerMethodField(read_only=True)
#     _id = serializers.SerializerMethodField(read_only=True)
#     school_id = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = User
#         fields = ['id', '_id', 'username', 'email', 'name', 'role', 'school_id', 'profile']

#     def get__id(self, obj):
#         return obj.id
    
#     def get_school_id(self, obj):
#         if obj.role == 'school_admin':
#             school = School.objects.filter(admin=obj).first()
#             return school._id if school else None
#         return None

#     def get_name(self, obj):
#         name = obj.first_name
#         if name == '':
#             name = obj.username
#         return name

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    school_id = serializers.SerializerMethodField(read_only=True)
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'role', 'school_id', 'profile']

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

    def get_profile(self, obj):
        request = self.context.get('request')
        if obj.profile:
            relative_url = obj.profile.url
            return request.build_absolute_uri(relative_url)
        return None


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'role', 'token', 'school_id', 'profile']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
    
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

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
    className = serializers.SerializerMethodField()
    class_id = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()
    class Meta:
        model = Class
        fields = ['className', 'class_id', 'school', 'student_count']

    def get_className(self, obj):
        return obj.name
    
    def get_class_id(self, obj):
        return obj._id
    
    def get_student_count(self, obj):
        return obj.students.count()
    
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
    
class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source='student.first_name', read_only=True)
    class Meta:
        model = Student
        fields = '__all__' 
    
# class GradeSerializer(serializers.ModelSerializer):
#     student = serializers.CharField(source='student.first_name', read_only=True)
#     student_id = serializers.CharField(source='student._id', read_only=True)
#     subject = serializers.CharField(source='subject.name', read_only=True)
#     semester = serializers.CharField(source='semester.name', read_only=True)
#     class Meta:
#         model = Grade
#         fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    className = serializers.CharField(source='class.name', read_only=True)
    student = serializers.SerializerMethodField()
    student_id = serializers.CharField(source='student._id', read_only=True)
    subject = serializers.CharField(source='subject.name', read_only=True)
    semester = serializers.CharField(source='semester.name', read_only=True)

    class Meta:
        model = Grade
        fields = ['className', 'student', 'student_id', 'subject', 'semester','score', 'grade', 'date_recorded']

    def get_student(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'code']  

class TeacherSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.username', read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)
    class Meta:
        model = Teacher
        fields = ['_id', 'name', 'subjects']