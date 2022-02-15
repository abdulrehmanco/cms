from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.views.decorators.csrf import csrf_exempt

import jwt, datetime


# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', options={"verify_signature": False}, algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response








class MedicineViewset(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset=Medicine.objects.all()
    serializer_class=MedicineSerializers



class CompanyViewset(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset=Company.objects.all()
    serializer_class=CompanySerializers

class CustomerViewset(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializers

class EmployeeViewset(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers

class EmployeeSalViewset(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset=EmployeeSalary.objects.all()
    serializer_class=EmployeeSalarySerializers

class BillViewset(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset=Bill.objects.all()
    serializer_class=BillSerializers

class Homeviewset(viewsets.ViewSet):
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]
    
    def list(self,request):
        medcount=Medicine.objects.all()
        Medcount_serilizer = MedicineSerializers(medcount,many=True,context={"request":request})

        comcount=Company.objects.all()
        Comcount_serilizer = CompanySerializers(comcount,many=True,context={"request":request})

        empcount=Employee.objects.all()
        Empcount_serilizer= EmployeeSerializers(empcount,many=True,context={"request":request})



        dict_response={"error":False,"message":"Home page data","medcount":len(Medcount_serilizer.data),
        "comcount":len(Comcount_serilizer.data),"empcount":len(Empcount_serilizer.data)}
        return Response(dict_response)
