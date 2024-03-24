from django.shortcuts import render
from django.http import HttpResponse



# importo los models de la App
from AppPe3_esg.models import *

# importo los forms de la app 
from AppPe3_esg.forms import *

from django.contrib.auth.forms import *
from django.contrib.auth import *


# Create your views here.

# INICIO

def inicio(request):
     
     return render(request, 'inicio.html')

# Iniciar Sesion

def iniciar_sesion (request):

    if request.method == 'POST':

        formulario = AuthenticationForm(request, data = request.POST) #Esto almacena la informacion ingresada en el formulario

        if formulario.is_valid():

            info_usu = formulario.cleaned_data # convierte la info del form en diccionario
            
            usuario     = authenticate(username = info_usu['username'],  password = info_usu['password'])

            if usuario is not None:

                login(request, usuario)

                return render(request, 'inicio.html',{'Mensaje':f'Bienvenido {usuario}'})
            
        else:

            return render(request, 'inicio.html', {'Mensaje':'Error al iniciar sesion'})


    else:

        formulario = AuthenticationForm() 

    return render(request, "registro/inicio_sesion.html", {'formu': formulario})

# Registrarse
def registrar_usu(request):

    if request.method == 'POST':

        form    =  UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']    
            form.save()

            return render(request, 'inicio.html', {'Mensaje': 'Usuario creado'})
        
    else:

        form = UsuarioRegistro()

    return(request, "registro/registrar.html", {'formu_reg': form})





# ************************ CLIENTES ***********************
# creacion
def ver_clientes(request):

    return render(request, 'clientes/ver_clientes.html')


def crear_cliente(request):

    if request.method == 'POST':

        formularioCli = Clientesforms(request.POST) #Esto almacena la informacion ingresada en el formulario

        if formularioCli.is_valid():

            info_cli = formularioCli.cleaned_data # convierte la info del form en diccionario

            nvo_cli= Clientes(  nombre      = info_cli['nombre'], 
                                apellido    = info_cli['apellido'],
                                documento   = info_cli['documento'],
                                email       = info_cli['email'])
            
            nvo_cli.save()

            return render(request, 'inicio.html')

    else:

        formulario = Clientesforms() 

    return render(request, 'clientes/crear_cliente.html', {'formu_cli':formulario})

## busqueda
def buscar_cliente(request):

    if request.GET:

        documento   = request.GET['documento']
        clientebus  = Clientes.objects.filter(documento__icontains=documento)

        mensaje = f'Estos son los datos del cliente obtenidos para documento ingresado: {documento}'

        return render(  request, 'clientes/buscar_cliente.html',{'mensaje':mensaje,'resultados':clientebus})
    
    else:
    
        return render(request, 'clientes/buscar_cliente.html')
    


# update
def actualizar_cliente(request, documentoupdate):

    cliente_sel = Clientes.objects.get(documento=documentoupdate)

    if request.method == 'POST':

        formularioCli = Clientesforms(request.POST) #Esto almacena la informacion ingresada en el formulario

        if formularioCli.is_valid():

            info_cli = formularioCli.cleaned_data # convierte la info del form en diccionario

            cliente_sel.nombre     = info_cli['nombre']
            cliente_sel.apellido   = info_cli['apellido']
            cliente_sel.documento  = info_cli['documento']
            cliente_sel.email      = info_cli['email']

            cliente_sel.save()

            return render(request, 'inicio.html')

    else:

        formulario = Clientesforms(initial={'nombre'    :cliente_sel.nombre,
                                            'apellido'  :cliente_sel.apellido,
                                            'documento' :cliente_sel.documento,
                                            'email'     :cliente_sel.email}) 


    return render(request, 'clientes/actualizar_cliente.html', {'formu_cli':formulario})

# borrar
def borrar_cliente(request, documento_del):

    cliente_sel = Clientes.objects.get(documento=documento_del)

    cliente_sel.delete()

    return render(request, 'inicio.html')    
    

# ************************ PROVEEDORES ***********************
# creacion
def ver_proveedores(request):

    return render(request, 'proveedores/ver_proveedores.html')


def crear_proveedor(request):

    if request.method == 'POST':

        formularioProv = Proveedoresforms(request.POST) #Esto almacena la informacion ingresada en el formulario

        if formularioProv.is_valid():

            info_prov = formularioProv.cleaned_data # convierte la info del form en diccionario

            nvo_prov= Proveedores(  razon_social= info_prov['razon_social'], 
                                    cuit        = info_prov['cuit'],
                                    email       = info_prov['email'],
                                    telefono    = info_prov['telefono'])
            
            nvo_prov.save()

            return render(request, 'inicio.html')

    else:

        formulario = Proveedoresforms() 

    return render(request, 'proveedores/crear_proveedor.html', {'formu_prov':formulario})

## busqueda
def buscar_proveedor(request):

    if request.GET:

        cuit   = request.GET['cuit']
        provbus  = Proveedores.objects.filter(cuit__icontains=cuit)

        mensaje = f'Estos son los datos del Porveedor obtenidos para la cuit ingresada: {cuit}'

        return render(  request, 
                        'proveedores/buscar_proveedor.html',
                        {'mensaje':mensaje, 
                        'resultados':provbus})
    
    else:
    
        return render(request, 'proveedores/buscar_proveedor.html')  



# update
def actualizar_Proveedor(request, cuit_update):

    Prov_update_sel = Proveedores.objects.get(cuit=cuit_update)

    if request.method == 'POST':

        formularioProv = Proveedoresforms(request.POST) #Esto almacena la informacion ingresada en el formulario

        if formularioProv.is_valid():

            info_prov = formularioProv.cleaned_data # convierte la info del form en diccionario

            Prov_update_sel.razon_social= info_prov['razon_social']
            Prov_update_sel.cuit        = info_prov['cuit']
            Prov_update_sel.email       = info_prov['enail']
            Prov_update_sel.telefono    = info_prov['telefono']

            Prov_update_sel.save()

            return render(request, 'inicio.html')

    else:

        formulario = Proveedoresforms(initial   ={  'razon_social'  :Prov_update_sel.razon_social,
                                                    'cuit'          :Prov_update_sel.cuit,
                                                    'email'         :Prov_update_sel.email,
                                                    'telefono'      :Prov_update_sel.telefono}) 


    return render(request, 'proveedores/actualizar_Proveedor.html', {'formu_prov':formulario})

# borrar
def borrar_proveedor(request, cuit_del):

    proveedor_del = Clientes.objects.get(cuit=cuit_del)

    proveedor_del.delete()

    return render(request, 'inicio.html')         
    

# ************************ COMPRAS ***********************
# creacion

def registrar_compra(request):

    if request.method == 'POST':

        formularioCompras = Comprasforms(request.POST) #Esto almacena la informacion ingresada en el formulario

        if formularioCompras.is_valid():

            info_compras = formularioCompras.cleaned_data # convierte la info del form en diccionario

            nva_compra  = Compras(  producto    = info_compras['producto'], 
                                    cantidad    = info_compras['cantidad'],
                                    cuit_prov   = info_compras['cuit_prov'],
                                    fecha_comp  = info_compras['fecha_comp'])
            
            nva_compra.save()

            return render(request, 'proveedores/ver_proveedores.html')

    else:

        formulario = Comprasforms() 

    return render(request, 'compras/crear_compra.html', {'formu_compra':formulario})

## busqueda
def buscar_compras(request):

    if request.GET:

        cuit_prov   = request.GET['cuit_prov']
        comprabus   = Compras.objects.filter(cuit_prov__icontains=cuit_prov)

        mensaje = f'Estas son las compras realizadas al Porveedor con cuit: {cuit_prov}'

        return render(  request, 
                        'compras/buscar_compra.html',
                        {'mensaje':mensaje, 
                        'resultados':comprabus})
    
    else:
    
        return render(request, 'compras/buscar_compra.html')       
    

# update
def actualizar_compra(request, id_compra):

    compras_update = Compras.objects.get(id=id_compra)

    if request.method == 'POST':

        formularioCompras = Comprasforms(request.POST) #Esto almacena la informacion ingresada en el formulario

        if formularioCompras.is_valid():

            info_Compra = formularioCompras.cleaned_data # convierte la info del form en diccionario

            compras_update.producto     = info_Compra['producto']
            compras_update.cantidad     = info_Compra['cantidad']
            compras_update.cuit_prov    = info_Compra['cuit_prov']
            compras_update.fecha_comp   = info_Compra['fecha_comp']

            compras_update.save()

            return render(request, 'inicio.html')

    else:

        formulario = Comprasforms(initial   ={  'producto'  :compras_update.producto,
                                                'cantidad'  :compras_update.cantidad,
                                                'cuit_prov' :compras_update.cuit_prov,
                                                'fecha_comp':compras_update.fecha_comp}) 


    return render(request, 'compras/actualizar_compra.html', {'formu_compra':formulario})


# borrar
def borrar_compra(request, id_compra_del):

    compra_del = Compras.objects.get(id=id_compra_del)

    compra_del.delete()

    return render(request, 'inicio.html')   

# ************************ PEDIDOS ***********************
# creacion
def ver_pedidos(request):

    return render(request, 'pedidos/ver_pedidos.html')

def crear_pedido(request):

    if request.method == 'POST':

        formularioPedido = Pedidosforms(request.POST) #Esto almacena la informacion ingresada en el formulario

        if formularioPedido.is_valid():

            info_pedido = formularioPedido.cleaned_data # convierte la info del form en diccionario

            nva_pedido  = Pedidos(  fecha_pedido    = info_pedido['fecha_pedido'], 
                                    cantidad_p      = info_pedido['cantidad_p'],
                                    monto           = info_pedido['monto'],
                                    doc_cliente     = info_pedido['doc_cliente'])
            
            nva_pedido.save()

            return render(request, 'pedidos/ver_pedidos.html')

    else:

        formulario = Pedidosforms() 

    return render(request, 'pedidos/crear_pedido.html', {'formu_pedido':formulario})


## busqueda
def buscar_pedido(request):

    if request.GET:

        doc_cliente = request.GET['documento']
        pedidobus   = Pedidos.objects.filter(doc_cliente__icontains=doc_cliente)

        mensaje = f'Estos son los pedidos realizados Cliente: {doc_cliente}'

        return render(  request, 
                        'pedidos/buscar_pedido.html',
                        {'mensaje':mensaje, 
                        'resultados':pedidobus})
    
    else:
    
        return render(request, 'pedidos/buscar_pedido.html')          
    
# update
def actualizar_pedido(request, id_pedido):

    pedido_update = Pedidos.objects.get(id=id_pedido)

    if request.method == 'POST':

        formularioPedido = Pedidosforms(request.POST) #Esto almacena la informacion ingresada en el formulario

        if formularioPedido.is_valid():

            info_Pedido = formularioPedido.cleaned_data # convierte la info del form en diccionario

            pedido_update.fecha_pedido      = info_Pedido['fecha_pedido']
            pedido_update.cantidad_p        = info_Pedido['cantidad_p']
            pedido_update.monto             = info_Pedido['monto']
            pedido_update.doc_cliente       = info_Pedido['doc_cliente']

            pedido_update.save()

            return render(request, 'inicio.html')

    else:

        formulario = Pedidosforms(initial   ={  'fecha_pedido'  :pedido_update.fecha_pedido,
                                                'cantidad_p'    :pedido_update.cantidad_p,
                                                'monto'         :pedido_update.monto,
                                                'doc_cliente'   :pedido_update.doc_cliente}) 


    return render(request, 'pedidos/actualizar_pedido.html', {'formu_pedido':formulario})


# borrar
def borrar_pedido(request, id_pedido_del):

    pedido_del = Pedidos.objects.get(id=id_pedido_del)

    pedido_del.delete()

    return render(request, 'inicio.html')   