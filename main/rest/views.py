from django.shortcuts import render
from model.models import Employee
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import EmployeeSerializer, UserSerializer
from django.forms.models import model_to_dict

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated] # Could be [permissions.IsAuthenticated]

class RegisterUsersView(generics.ListCreateAPIView):
    """
    POST user/signup/
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username or not password or not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    
        try:
            new_user = User.objects.create_user(
                username=username, password=password, email=email
            )
            return Response(data=model_to_dict(new_user),status=status.HTTP_201_CREATED)
        except Exception as e:            
            print(e)
            return Response(status=status.HTTP_409_CONFLICT)