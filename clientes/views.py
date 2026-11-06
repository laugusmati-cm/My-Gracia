
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from.models import Cliente
from.forms import Clienteform, ClienteEditarForm

def lista(request):
    clientes = Cliente.objects.all()
    return render(request,'clientes/lista.html',{'clientes': clientes})

def crear(request):
    if request.method == 'POST':      
        formulario = Clienteform (request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(
                request,
                'Cliente registrado correctamente.'   
            )
            return redirect('clientes:lista')
        
        else:
            messages.error(
                request,
                'no se pudo registrar el cliente. Revisa los campos.'
            )
    else:                          
        formulario = Clienteform()
    return render(
        request,
        'clientes/formulario.html', 
        {
            'formulario': formulario,'titulo': 'Registrar cliente'
        }
        )

def editar(request, Id_Cliente):
    cliente = get_object_or_404(Cliente, pk=Id_Cliente )
    if request.method == 'POST':
        formulario = ClienteEditarForm(
            request.POST,
             instance=cliente
        )
        if formulario.is_valid():
            formulario.save()
            messages.success(
                request,
                'Cliente actualizado correctamente.'
            )
            return redirect('clientes:lista')
    else: 
        formulario = ClienteEditarForm(instance = cliente)
    return render(
        request,
        'clientes/editar_cliente.html',
            {
             'formulario' : formulario,
             'cliente': cliente
            }
        )    
@require_POST
def desactivar_cliente(request, pk):
    cliente = get_object_or_404(
        Cliente,
        Id_Cliente = pk
    )
    cliente.Estado_Cliente = False
    cliente.save(update_fields = ['Estado_Cliente'])
    messages.success(
        request,
        'El cliente fue desactivado correctamente.'
    )
    return redirect('clientes:lista')

