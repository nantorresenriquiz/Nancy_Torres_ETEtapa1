from django.shortcuts import render, redirect
from .models import Colaborador
from .forms import ColaboradorForm
# Create your views here.

def Index(request):
    colaboradores= Colaborador.objects.all()
    return render(request, 'Index.html')

def form_crear(request):
    if request.method=='POST': 
        colaborador_form = ColaboradorForm(request.POST, request.FILES)
        if colaborador_form.is_valid():
            colaborador_form.save()
            return redirect('form_ver')
    else:
       colaborador_form= ColaboradorForm()
    return render(request, 'caosnews/form_crear.html', {'colaborador_form': colaborador_form})

def form_ver(request):
    colaboradores = Colaborador.objects.all() 
    datos = {
        'colaboradores': colaboradores
    }       
    return render(request, 'caosnews/form_ver.html', {'colaboradores':colaboradores})

def form_modificar(request,id):
    colaborador = Colaborador.objects.get(rutColaborador=id)

    datos ={
        'form': ColaboradorForm(instance=colaborador)
    }
    if request.method == 'POST': 
        formulario = ColaboradorForm(data=request.POST,  instance = colaborador)
        if formulario.is_valid: 
            formulario.save()
            return redirect('form_ver')
    return render(request, 'caosnews/form_modificar.html', datos)


def form_eliminar(request,id):
    colaborador = Colaborador.objects.get(rutColaborador=id)
    colaborador.delete()
    return redirect('form_ver')
