from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from sleepapi.models import SleepCycleModel


class SleepCycleSerializer(ModelSerializer):
    class Meta:
        model = SleepCycleModel
        fields = '__all__'
        read_only_fields = ('id',)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password',)


# class UserSignupSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'email', 'phone_no')


# class BugReportSerializer(ModelSerializer):
#     '''Serializer for BugReporting Feature'''
#     class Meta:
#         model = BugReport
        # fields = '__all__'
#         read_only_fields = ('id',)


# class BugReportUpdateSerializer(ModelSerializer):
#     '''Serializer for BugReporting Feature'''
#     class Meta:
#         model = BugReport
        # fields = ('status', 'assigned_to')
#         read_only_fields = ('id',)
