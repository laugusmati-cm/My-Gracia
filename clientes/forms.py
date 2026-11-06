from django import forms
from django.contrib.auth.hashers import make_password
from .models import Cliente, usuario
from django.db import transaction
from django.utils import timezone

class Clienteform(forms.ModelForm):
    correo = forms.EmailField(
        label='correo electronico'
    )
    contrasena= forms.CharField(
        label='contraseña',
        widget=forms.PasswordInput()
    )   
   
    Estado_Cliente = forms.TypedChoiceField(
        label="Estado del cliente",        
        choices=[
            ('True', 'Activo'),
            ('False', 'Inactivo')  
        ],
        coerce=lambda valor: valor =='True',
        widget=forms.Select(attrs={
            'class': 'form-control'
        })

    )
    class Meta:
        model = Cliente
        fields = [
           'Nombre_Cliente',
           'Telefono_Cliente',
           'Fecha_Nacimiento',
           'Estado_Cliente',
        ]
        label = {
           'Nombre_Cliente': 'Nombre completo',
           'Telefono_Cliente': 'Telefono',
           'Fecha_Nacimiento': 'Fecha de nacimiento',
           'Estado_Cliente': 'Cliente activo',
        }

        widgets = {
            'Nombre_Cliente': forms.TextInput(attrs ={ 'class':'form-control', 'placeholder':
               'Ingrese el nombre completo' }
            ),
            'Telefono_Cliente': forms.TextInput(
            attrs ={ 'class':'form-control', 'placaholder':
                'Ingrese el numero del telefono del cliente' }
            ),

            'Fecha_Nacimiento': forms.DateInput(
            attrs = { 'type': 'date','class':'from-control' },
            format = '%Y-%m-%d' 
            ),
            'Estado_Cliente': forms.TypedChoiceField(
            label=" Estado del cliente ",
            choices=[ 
                (True, "Activo"),
                (False, "Inactivo")
            ],
            coerce=lambda valor : valor == 'True',
            widget= forms.Select(attrs={
                'class': 'form-control'
            })
            )
        }
    @transaction.atomic    
    def save(self, commit=True):
        cliente = super().save(commit = False)
        
        if commit:
            ahora= timezone.now()
            nuevo_usuario = usuario(
                Correo_Usuario = self.cleaned_data['correo'],
                Contrasena_Usuario = make_password(self.cleaned_data['contrasena']),
                Rol_Usuario = 'cliente',
                Estado_Usuario = True,
                Fecha_Registro = ahora
             )            
            
            nuevo_usuario.save()
            cliente.usuario = nuevo_usuario
            cliente.Fecha_Registro = ahora
            cliente.save()
        return Cliente     
    
        self.fields['usuario'].queryset =(
        self.fields['usuario'].queryset.order_by('Correo_Usuario')  
        )
        self.fields['Fecha_Nacimiento'].input_formats = [
            '%Y-%m-%d'
        ]
class ClienteEditarForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'Nombre_Cliente',
            'Telefono_Cliente',
            'Fecha_Nacimiento',
            'Estado_Cliente',
        ]
        label = {
            'Nombre_Cliente': 'Nombre completo',
            'Telefono_Cliente': 'Telefono',
            'Fecha_Nacimiento': 'Fecha de nacimiento',
            'Estado_Cliente': 'Cliente activo',
        }
        widgets = {
            'Fecha_Nacimiento':
            forms.DateInput(attrs={'type':'date'},
              format = '%Y-%m-%d'               
            ),
        }       