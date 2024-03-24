from django.urls import path
from AppPe3_esg.views import *

urlpatterns = [
    path(''                                     ,inicio             ,name = 'molde_inicio'),
    path('login/'                               ,iniciar_sesion     ,name = 'iniciar sesion'),
    path('registrar/'                           ,registrar_usu      ,name = 'Registrar usuario'),    

    path('clientes/'                            ,ver_clientes       ,name = 'clientes'),
    path('crear_cliente/'                       ,crear_cliente),
    path('buscar_cliente/'                      ,buscar_cliente),
    path('actualizar_cliente/<documentoupdate>/',actualizar_cliente),    
    path('borrar_cliente/<documento_del>/'      ,borrar_cliente), 

    path('proveedores/'                         ,ver_proveedores,   name = 'proveedores'),  
    path('crear_proveedor/'                     ,crear_proveedor),
    path('buscar_proveedor/'                    ,buscar_proveedor),
    path('actualizar_proveedor/<cuit_update>/'  ,actualizar_Proveedor),   
    path('borrar_proveedor/<cuit_del>/'         ,borrar_proveedor),         

    path('pedidos/'                             ,ver_pedidos,       name = 'pedidos'),     
    path('crear_pedido/'                        ,crear_pedido),
    path('buscar_pedido/'                       ,buscar_pedido),
    path('actualizar_pedido/<id_pedido>/'       ,actualizar_pedido),     
    path('borrar_pedido/<id_pedido_del>/'       ,borrar_pedido),       

    path('crear_compra/'                        ,registrar_compra),
    path('buscar_compra/'                       ,buscar_compras),
    path('actualizar_compra/<id_compra>/'       ,actualizar_compra),     
    path('borrar_compra/<id_compra_del>/'       ,borrar_compra),         



]