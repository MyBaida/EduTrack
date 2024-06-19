from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('super_admin', 'Super Admin'),
        ('school_admin', 'School Admin'),
        ('teacher', 'Teacher'),
    ]

    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    profile= models.ImageField(null=True, blank=True, default='/placeholder.png')


    def __str__(self):
        return self.username
    

class School(models.Model):
    SCHOOL_TYPE_CHOICES = [
        ('preschool', 'Preschool'),
        ('primary', 'Primary School'),
        ('jhs', 'Junior High School'),
        ('shs', 'Senior High School'),
        ('university', 'University'),
    ]
    _id= models.AutoField(primary_key=True, editable=False)
    name= models.CharField(max_length=250)
    school_type= models.CharField(max_length=50, choices=SCHOOL_TYPE_CHOICES)
    address = models.TextField(max_length=250)
    phone = models.CharField(max_length=15)
    admin = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='managed_school')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    _id= models.AutoField(primary_key=True, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')

    def __str__(self):
        return self.user.username


class Class(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classes', blank=True)
    _id= models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return f'{self.name} - {self.school.name}'


class Student(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField()
    enrollment_date = models.DateField()
    profile= models.ImageField(null=True, blank=True, default='/placeholder.png')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    current_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, related_name='students')
    completed = models.BooleanField(default=False, blank=True, null=True)
    completed_date = models.DateField(blank=True, null=True)
    _id= models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Semester(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    _id= models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='subjects')
    teachers = models.ManyToManyField(Teacher, related_name='subjects')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='subjects')
    _id= models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True, blank=True)
    grade = models.CharField(max_length=2, null=True, blank=True)
    score = models.PositiveIntegerField(null=True, blank=True)
    date_recorded = models.DateField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return f'{self.student} - {self.subject}: {self.grade}'

    def save(self, *args, **kwargs):
        if not self.semester:
            self.semester = self.subject.semester
        super().save(*args, **kwargs)
        

