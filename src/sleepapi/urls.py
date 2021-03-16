from django.urls import path, re_path

from sleepapi.views import  SignUpApiView, LoginApiView,SleepApiInfoView,ErrorApiView,SuccessApiView
app_name = 'sleep'

urlpatterns = [
    path('info/', SleepApiInfoView.as_view(), name="info"),
    path('signup/', SignUpApiView.as_view(), name="signup"),
    path('login/', LoginApiView.as_view(), name="login"),
    path('error/', ErrorApiView.as_view(), name="error"),
    path('success/', SuccessApiView.as_view(), name="success"),
]
