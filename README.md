# Final_Eduardo_Sebastian_Garcia

1- Para compilar la base de datos, luego de descargar los archivos en el VSC ejecutar _python manage.py makemigrations

2- Si todo esta correcto, se deberia generar el archivo AppPe3_esg\migrations\0001_initial.py

3- Ahora ejecutamos python manage.py migrate

4- Comenzara a generar los logs de la generacion de la estructura de tablas y nos creara el db.sqlite3, donde se puede chequear las tablas generadas por el model y otras generadas por el mismo django

5- Para visualizar la pagina Web, en el terminal ejecutamos python manage.py runserver

6- en la pagina encontraras 3 botones funcionales, Clientes, Proveedores y Pedidos, mientras que el boton Inicio nos lleva a la pagina de inicio.

7- Botones:

a) Clientes: nos redirecciona al Portal de Clientes, donde podemos registrar un nuevo Cliente (Crear Cliente) o Buscar los datos de un cliente existente (Buscar Cliente)

b) Proveedores: nos redireciona al Portal de Proveedores, donde podemos dar de alta un nuevo proveedor (Crear Proveedor), consultar los datos de los proveedores existentes en base de datos (Buscar Proveedor), registrar las compras de mercaderias (Registrar Compra) y consultar las compras de insumos realizadas (Buscar Compra).

c) Pedidos: Redirecciona al portal de Pedidos realizados por nuestros clientes, en ella podemos generar un nuevo pedido (Generar Pedido) y Buscar los pedidos realizados por un Cliente (Buscar Pedido).

8- Para cada uno de estos botones se generaron sus Urls: inicio - http://127.0.0.1:8000/APesg/

portal cliente       - http://127.0.0.1:8000/APesg/cliente/
portal proveedores   - http://127.0.0.1:8000/APesg/proveedores/
portal pedidos       - http://127.0.0.1:8000/APesg/pedidos/

crear cliente        - http://127.0.0.1:8000/APesg/crear_cliente/
crear proveedor      - http://127.0.0.1:8000/APesg/crear_proveedor/
crear compra         - http://127.0.0.1:8000/APesg/crear_compra/
crear pedido         - http://127.0.0.1:8000/APesg/crear_pedido/ 

buscar cliente      - http://127.0.0.1:8000/APesg/buscar_cliente/
buscar proveedor    - http://127.0.0.1:8000/APesg/buscar_proveedor/
buscar compra       - http://127.0.0.1:8000/APesg/buscar_compra/
buscar pedido       - http://127.0.0.1:8000/APesg/buscar_pedido/
9- Portal Administrador. accediendo desde http://127.0.0.1:8000/admin/. desde aqui se puede administrar los permisos y realizar modificaciones en la base de datos. Acceder se utilizan los siguientes datos.

Usuario: Admin

Passw: administrador

10- Para el registro de un nuevo user ejecutar en el terminal: python manage.py createsuperuser Solicitara el nombre de usuario, email y passw. Esto detiene el server, con lo cual se debe ejecutar nuevamente python manage.py runserver

11- se modifico el idioma desde settings.py del proyecto ProjPe3.py en LANGUAGE_CODE = 'es' y se paso a español.
