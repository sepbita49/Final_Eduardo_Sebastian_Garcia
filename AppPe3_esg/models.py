from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre      = models.CharField(max_length=60)
    apellido    = models.CharField(max_length=60)
    documento   = models.IntegerField()
    email       = models.EmailField()

    def __str__(self):
        
        return f'Nombre y Apellido: {self.nombre} {self.apellido} / email: {self.email} / documento: {self.documento}'


class Proveedores(models.Model):
    razon_social= models.CharField(max_length=60)
    cuit        = models.CharField(max_length=20)
    email       = models.EmailField()
    telefono    = models.IntegerField()

    def __str__(self):
        
        return f'Razon Social: {self.razon_social} / Email: {self.email} / Telefono: {self.telefono}'    

class Pedidos(models.Model):
    fecha_pedido= models.DateField()
    cantidad_p  = models.IntegerField()
    monto       = models.FloatField()
    doc_cliente = models.IntegerField()
    
    def __str__(self):
        
        return f'Fecha Pedido: {self.fecha_pedido} / Documento: {self.doc_cliente} / cantidad: {self.cantidad_p} / monto: {self.monto}'    


class Compras(models.Model):
    producto    = models.CharField(max_length=60)
    cantidad    = models.IntegerField()
    cuit_prov   = models.CharField(max_length=20)
    fecha_comp  = models.DateField()
    
    def __str__(self):
        
        return f'Fecha compra: {self.fecha_comp} / producto: {self.producto} / cantidad: {self.cantidad}'       