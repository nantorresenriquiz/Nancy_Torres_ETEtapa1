from django.db import models

# Create your models here.

class Colaborador (models.Model):
    rutColaborador =models.IntegerField(primary_key=True, verbose_name='Rut de Colaborador')    
    nomColaborador =models.CharField(max_length=60,verbose_name='Nombre de Colaborador')
    fonoColaborador =models.IntegerField(verbose_name='Teléfono de Colaborador')
    dirColaborador =models.CharField(max_length=60,verbose_name='Dirección de Colaborador')
    emailColaborador= models.EmailField(verbose_name='Email de Colaborador')
    paisColaborador= models.CharField(max_length=20,verbose_name='Pais de Colaborador')
    contrasenaColaborador= models.CharField(max_length=20,verbose_name='Contraseña de Colaborador')
    imagen= models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return self.nomColaborador