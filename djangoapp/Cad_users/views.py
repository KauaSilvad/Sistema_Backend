# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializer import UserSerializer
import json

User = get_user_model()

def LoginView(request):
    return render(request, 'cad_users/login.html')

def CadastroView(request):
    if request.method == 'POST':
        try:
            # cria um dic para os dados do user
            data = {
                'username': request.POST.get('cpf'), 
                'email': request.POST.get('email'),
                'password': request.POST.get('password'),
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'phone': request.POST.get('phone'),
                'cpf': request.POST.get('cpf'),
                'address': request.POST.get('address'),
                'state': request.POST.get('state'),
                'city': request.POST.get('city'),
                'zip_code': request.POST.get('zip_code')
            }
            
          
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                user = serializer.save()
                messages.success(request, 'Cadastro realizado com sucesso!')
                return redirect('login')
            else:
                
                for field, errors in serializer.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")
        except Exception as e:
            messages.error(request, f"Erro ao processar o cadastro: {str(e)}")
    
    return render(request, 'cad_users/cadastro.html')