from django.shortcuts import render
from rest_framework.response import     Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer

User = get_user_model

class RegisterView(APIView):
    def post(sefl, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response('Вы успешно зарегистрировались!' ,201)

class ActivationView(APIView):
    def get(self, request, email, activation_code):
        User= User.objects.filter(email=email, activation_code=activation_code).first()
        if not User: 
            return Response('пользователь не найден ',404)
        User.activation_code=''
        User.is_active=True
        User.save()
        return Response('пользователь  найден ',200)
