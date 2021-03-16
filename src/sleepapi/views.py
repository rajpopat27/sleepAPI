from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.urls import reverse

from sleepapi.serializers import SleepCycleSerializer, UserSerializer
from sleepapi.models import SleepCycleModel

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.shortcuts import render,redirect


class ErrorApiView(APIView):
    def get(self, request):
        return render(request,'sleepapi/error.html')
class SuccessApiView(APIView):
    def get(self, request):
        return render(request,'sleepapi/success.html')

class SleepApiInfoView(APIView):
    def post(self, request):
        req_params = request.data.copy()
        req_params['user_id']=request.user.id
        serilalizer = SleepCycleSerializer(data=req_params)
        if not serilalizer.is_valid():
            return redirect(reverse('sleep:error'))    
        else:
            serilalizer.save()
            return redirect(reverse('sleep:success' ))

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'sleepapi/info.html')
        else:
            return render(request,'sleepapi/login.html',{'error': "User does not exsist"}) 


class SignUpApiView(APIView):

    def post(self, request):
        req_parms = request.data
        user_ser = UserSerializer(data=req_parms)
        if not user_ser.is_valid():
            return render(request,'sleepapi/signup.html',{'error': "User data not valid"}) 
        user = User.objects.create_user(
            username=req_parms['username'], password=req_parms['password'])

        return  redirect(reverse('sleep:login' ))
    def get(self,request):
        return render(request,'sleepapi/signup.html') 


class LoginApiView(APIView):

    def post(self, request):
        req_parms = request.data
        user = authenticate(username=req_parms['username'], password=req_parms['password'])
        if not user:
            # return render(request,'sleepapi/signup.html',{'error': "User does not exsist"}) 
            return redirect(reverse('sleep:signup' ))
        login(request, user)
        # return render(request,'sleepapi/info.html')
        return redirect(reverse('sleep:info' ))

    def get(self, request):
        return render(request, 'sleepapi/login.html',{})


