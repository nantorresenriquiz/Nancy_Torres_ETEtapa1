from django.urls import path
from .views import Index, form_ver, form_crear, form_modificar, form_eliminar

urlpatterns = [
    path('', Index,name="Index"),
    path('form_ver', form_ver, name="form_ver"),
    path('form_crear', form_crear, name="form_crear"),
    path('form_modificar/<id>', form_modificar, name="form_modificar"),
    path('form_eliminar/<id>', form_eliminar, name="form_eliminar"),
]