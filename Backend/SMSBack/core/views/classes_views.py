from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser 

from core.models import Class, School, Grade, Semester, Subject
from core.serializers import ClassSerializer
from core.permissions import IsSuperAdmin, IsSchoolAdmin, IsTeacher, IsTeacherOfSubject, IsSchoolAdminOfSchool


from rest_framework import status

@api_view(['GET'])
@permission_classes([IsSchoolAdmin])
def getClasses(request):
    try:
        school = request.user.managed_school  # This assumes the User model has a managed_school related name pointing to the School model
    except School.DoesNotExist:
        return Response({'error': 'School not found for the current admin'}, status=status.HTTP_404_NOT_FOUND)

    classes = Class.objects.filter(school=school)
    serializer = ClassSerializer(classes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsSchoolAdmin])
def getClass(request, pk):
    classs = Class.objects.get(_id=pk)
    serializer = ClassSerializer(classs, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsSchoolAdminOfSchool])
def createClass(request):
    if request.method == 'POST':
        school = request.school  # Retrieve the school from the request
        if not school:
             return Response({'error': 'School not found for this admin'}, status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        serializer = ClassSerializer(data=data)
        if serializer.is_valid():
            serializer.save(school=school)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([IsSchoolAdmin])
def get_subject_grade_statistics(request, class_id, semester_id):
    try:
        class_instance = Class.objects.get(_id=class_id)
        semester_instance = Semester.objects.get(_id=semester_id)
    except Class.DoesNotExist:
        return Response({'error': 'Class not found'}, status=status.HTTP_404_NOT_FOUND)
    except Semester.DoesNotExist:
        return Response({'error': 'Semester not found'}, status=status.HTTP_404_NOT_FOUND)

    subjects = Subject.objects.filter(school=class_instance.school)
    response_data = []

    for subject in subjects:
        grades = Grade.objects.filter(
            student__current_class=class_instance,
            semester=semester_instance,
            subject=subject
        )

        number_of_passed = grades.filter(grade__in=['1', '2', '3', '4']).count()
        number_of_average = grades.filter(grade__in=['5', '6']).count()
        number_of_failed = grades.filter(grade__in=['7', '8', '9']).count()

        response_data.append({
            "className": class_instance.name,
            "class_id": class_instance._id,
            "semester": semester_instance.name,
            "subjectName": subject.name,
            "number_of_passed": number_of_passed,
            "number_of_average": number_of_average,
            "number_of_failed": number_of_failed,
            "date_recorded": grades.first().date_recorded if grades.exists() else None
        })

    return Response(response_data, status=status.HTTP_200_OK)


# @api_view(['POST'])
# @permission_classes([IsSchoolAdmin, IsSchoolAdminOfSchool])
# def createClass(request):
#     if request.method == 'POST':
#         user = request.user
#         print(user)

#         # Get the school stored in the request by the permission class
#         school = request.school
        
#         if not school:
#             return Response({'error': 'School not found for this admin'}, status=status.HTTP_400_BAD_REQUEST)

#         data = request.data
#         serializer = ClassSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save(school=school)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT'])
# @permission_classes([IsAdminUser])
# def updateCategory(request, pk):
#     data = request.data
#     category = Category.objects.get(_id=pk)

#     category.name = data['name']

#     category.save()

#     serializer = CategorySerializer(category, many=False)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getCategoryProducts(request, pk):
#     try:
#         category = Category.objects.get(_id=pk)
#         products = category.product_set.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#     except Category.DoesNotExist:
#         return Response({'detail': 'Category does not exist'}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# @permission_classes([IsAdminUser])
# def deleteCategory(request, pk):
#     category = Category.objects.get(_id=pk)
#     category.delete()
#     return Response('Category Deleted')