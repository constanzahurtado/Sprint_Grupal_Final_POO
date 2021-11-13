# Se crea una clase Bodega con los atributos solicitados
class Bodega:
    def __init__(self, id_bodega, nombre_bodega, total_producto): # Constructor
        self.id_bodega = id_bodega 
        self.nombre_bodega = nombre_bodega
        self.total_producto = total_producto
        self.lista_proveedores = []
        self.stock_producto = {}
        self.total_productos_transferidos = 0
        self.lista_transferidos = []
        
    #Este método permite generar una lista con proveedores, mediante la función *args porque no se sabe la cantidad de proveedores a agregar.

    def agregar_proveedor(self, *proveedores): 
        for proveedor in proveedores: # Este ciclo for permite que la tupla generada con la función *args se convierta en una lista.
            self.lista_proveedores.append(proveedor) # Utilizamos la función append para agrgar un proveedor.
        return self.lista_proveedores # retornamos la lista creada. 
 
    #Este método permite eliminar un proveedor de la lista creada anteriormente.
 
    def eliminar_proveedor(self): 
        proveedor = input('Ingrese proveedor a eliminar: ') # Solicitamos el nombre del proveedor a eliminar.
        self.lista_proveedores.remove(proveedor) # Con la función remove eliminamos al proveedor.
        return self.lista_proveedores # Retornamos la lista para mostrar que efectivamente ha sido eliminado el proveedor.

    # Este método permite crear un diccionario con un nombre como clave y un stock como clave. 
    def agregar_producto(self, producto, cantidad):
        self.stock_producto[producto] = cantidad
        return self.stock_producto # Retornamos el diccionario creado. 
    
    # Esta función permite realizar transferencias de productos de una bodega a otra. 
    def transferir_bodega(self, monto, bodega_destino, producto):
        self.total_producto = self.total_producto - monto # Se resta a la bodega de origen el monto a transferir.
        bodega_destino.total_producto = monto + bodega_destino.total_producto # Se suma a la bodega destino el monto a transferir.
        self.lista_transferidos.append(producto) # Se crea un lista para indicar que producto será transferido. 
        self.total_productos_transferidos += monto # Total de producto transferido
        return self.total_productos_transferidos 
    
    def mostrar_productos_transferidos(self):
        return self.total_productos_transferidos # Con este método mostramos la cantidad de producto transferido. 
  
    def mostrar_tipo_producto(self):
        return self.lista_transferidos # Con este método mostramos el tipo de producto transferido. 
  
    def mostrar_total_productos(self): # Con este método mostramos el total de producto transferido. 
        return self.total_producto

# Se crea una clase Proveedor con los atributos solicitados.

class Proveedor:
    def __init__(self, id_proveedor, nombre_proveedor, tipo_producto): # Constructor
        self.id_proveedor = id_proveedor
        self.nombre_proveedor = nombre_proveedor
        self.tipo_producto = tipo_producto
    
# Se crea un método que permite que el proveedor se pueda inscribir en una determinada bodega. 
# Esta inscripción se realiza en la misma lista descrita en la clase Bodega. 

    def inscripcion_bodega(self, bodega:Bodega):
        bodega.lista_proveedores.append(self.nombre_proveedor) # Utilizamos la función append para agrgar un proveedor.
        return bodega.lista_proveedores # Retornamos la lista de proveedores nuevamente para comprobar que se realizó la acción.  
        
    def modificar_producto(self, a): # Este método permite actualizar un producto de un proveedor, 
        self.tipo_producto = a # entregando un parámetro que reemplazará al anterior.
        return self.tipo_producto # Mostramos el cambio realizado. 

# Se crea la clase Operarios solicitada.

class Operarios(): 
    def cantidad_proveedores(self, bodega:Bodega): # Este método nos permite concultar el número de proveedores, mediante la función len().
        return f'La cantidad de proveedores de la bodega {bodega.nombre_bodega} es de {len(bodega.lista_proveedores)} proveedores'
        
# Se crea la clase Administrador solicitada. Esta hereda de operarios la función que permite saber el número de proveedores.

class Administrador(Operarios): # Además, se crea una función que le permite a un administrador saber la cantidad de stock. 
    def stock_bodega(self, bodega:Bodega):
        return f'El stock de la bodega {bodega.nombre_bodega} es de {bodega.total_producto}'

# Instancias clase Bodega

bodega1 = Bodega('001', 'bodega1', 200)
bodega2 = Bodega('002', 'bodega2', 10)

# Instancias clase Proveedor
proveedor1 = Proveedor(1, "Proveedor1", "Carne")
proveedor2 = Proveedor(2, "Proveedor2", "Cerdo")

# Instancia clase Operarios
operario1 = Operarios()

# Instancia clase Administrador
administrador1 = Administrador()

# Comenzamos llamando a los métodos de la clase Bodega.

print("Lista Proveedores")
print(bodega1.agregar_proveedor('Sony', 'Casa Ideas'))
print('---------------------------------------------------------------------------')
print(bodega1.eliminar_proveedor())
print('---------------------------------------------------------------------------')

bodega1.agregar_producto('Electrónico', 100)
bodega1.agregar_producto('Decoración', 50)
print(bodega1.stock_producto)
print('---------------------------------------------------------------------------')

print("Transferencia de productos")
print(bodega1.transferir_bodega(30, bodega2,'Electrónico'))
print("--------------------------------------------")
print(bodega1.mostrar_productos_transferidos())
print("--------------------------------------------")
print(bodega1.mostrar_total_productos())
print(bodega2.mostrar_total_productos())
print('---------------------------------------------------------------------------')
print(bodega1.mostrar_tipo_producto())
print('---------------------------------------------------------------------------')

# Llamamos a los métodos de la clase Proveedor.
print(proveedor1.inscripcion_bodega(bodega1))
print('---------------------------------------------------------------------------')
print("Antes del cambio")
print(proveedor1.tipo_producto)
print(proveedor2.tipo_producto)
print('---------------------------------------------------------------------------')
print("Después del cambio")
proveedor1.modificar_producto("Pollo")
proveedor2.modificar_producto("Conejo")
print(proveedor1.id_proveedor, proveedor1.tipo_producto)
print(proveedor2.id_proveedor, proveedor2.tipo_producto)
print('---------------------------------------------------------------------------')

# Llamamos a los métodos de la clase Operarios.
print("Datos que puede ver un operario")
print(operario1.cantidad_proveedores(bodega1))
print("---------------------------------------------------------")

# Llamamos a los métodos de la clase Administrador.
print("Datos que puede ver un administrador")
print(administrador1.stock_bodega(bodega1))
print(administrador1.cantidad_proveedores(bodega1))


