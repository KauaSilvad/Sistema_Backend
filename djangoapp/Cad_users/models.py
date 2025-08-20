from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)
    
    # Novos campos
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="O número de telefone deve estar no formato: '+999999999'. Até 15 dígitos."
    )
    phone = models.CharField(_('telefone'), validators=[phone_regex], max_length=17, blank=False)
    cpf = models.CharField(_('CPF'), max_length=14, unique=True, blank=False)
    
    # Campos de endereço
    address = models.CharField(_('endereço'), max_length=255, blank=False)
    state = models.CharField(_('estado'), max_length=2, blank=False)
    city = models.CharField(_('cidade'), max_length=100, blank=False)
    zip_code = models.CharField(_('CEP'), max_length=9, blank=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone', 'cpf', 'address', 'state', 'city', 'zip_code']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
