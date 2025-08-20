from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('login/', views.LoginView, name='login'),
    path('cadastro/', views.CadastroView, name='cadastro'),
    
]
