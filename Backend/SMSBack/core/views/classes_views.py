from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser 

from core.models import Class, School
from core.serializers import ClassSerializer
from core.permissions import IsSuperAdmin, IsSchoolAdmin, IsTeacher, IsTeacherOfSubject, IsSchoolAdminOfSchool


from rest_framework import status


@api_view(['GET'])
@permission_classes([IsSchoolAdmin])
def getClasses(request):
    classes = Class.objects.all()
    serializer = ClassSerializer(classes, many=True)
    return Response(serializer.data)

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