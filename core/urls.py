from django.urls import re_path
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    # re_path('signup', views.signup),
    # re_path('login', views.login),
    # re_path('test_token', views.test_token),
    path('api/signup/', views.signup, name='signup'),
    path('api/login/', views.login, name='login'),
    path('api/test-token/', views.test_token, name='test_token'),
    path('api/index/', views.index, name='index'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]