from django import forms
from django.forms import ModelForm, widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Colaborador



class ColaboradorForm(forms.ModelForm):

    class Meta:
        model = Colaborador
        
        fields = ['rutColaborador', 'nomColaborador', 'fonoColaborador','dirColaborador','emailColaborador','paisColaborador','contrasenaColaborador','imagen']
        labels ={
            'rutColaborador': 'Rut', 
            'nomColaborador': 'Nombre', 
            'fonoColaborador': 'Teléfono',
            'dirColaborador': 'Dirección',
            'emailColaborador': 'Email',
            'paisColaborador' : 'Pais',
            'contrasenaColaborador' : 'Contraseña',
            'imagen': 'Imagen',
        }
        widgets={
            'rutColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut sin dígito verificador', 
                    'id': 'rutColaborador'
                }
            ), 
               
            'nomColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nomColaborador'
                }
            ), 
            'fonoColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese teléfono', 
                    'id': 'fonoColaborador',
                }
            ),
            'dirColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese dirección', 
                    'id': 'dirColaborador',
                }
            ),
            'emailColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese email', 
                    'id': 'emailColaborador',
                }
            ),
            'paisColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese pais', 
                    'id': 'paisColaborador',
                }
            ),
            'contrasenaColaborador': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese contraseña', 
                    'id': 'contrasenaColaborador',
                }
            ),
              'imagen': forms.ClearableFileInput(
                attrs={'class': 'form-control',
                'id': 'imagen','name': 'imagen',
                'accept':"imagen/*"}

            ),

        }