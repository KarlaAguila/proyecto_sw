from model.model import Model
from view.view import View

class Controller: 
    #Controlador de mi tiendita de abarrotes
    def __init__(self):
        self.model = Model() 
        self.view = View() 

    def start(self): 
        self.view.start() 
        self.main_menu() #este quitar el view

    #Controles generales
    def main_menu(self):
        o = '0'
        while o !='4':
            self.view.main_menu()
            self.view.option('4')
            o = input()
            if o == '1':
                self.productos_menu()
            elif o == '2': 
                self.clientesConsentidos_menu()
            elif o =='4':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    #Controlador para actualizar lista
    def update_lists(self, fs, vs): #lista de campos y valores
        fields = []
        vals = []
        for f, v in zip(fs, vs):
            if v != '': #Lo modifica
                fields.append(f+' = %s')
                vals.append(v)
            return fields, vals
        
    
#****************CONTROLADOR PARA PRODUCTOS********************************
    def productos_menu(self):
        o = '0'
        while o != '6':
            self.view.productos_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_producto()
            elif o == '2': 
                self.read_a_producto()
            elif o =='3':
                self.read_all_productos()
            elif o =='4':
                self.update_producto()
            elif o =='5':
                self.delete_producto()
            elif o =='6':
                return
            else:
                self.view.not_valid_option()
        return
    
    #Solicitar datos para escribir o actualizar info
    def ask_producto(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Stock: ')
        stock = input()
        self.view.ask('Descripcion: ')
        descripcion = input()
        self.view.ask('Precio: ')
        precio = input()
        self.view.ask('IVA: ')
        iva = input()
        return[nombre, stock, descripcion, precio, iva]
    
    #Crear un producto 
    def create_producto(self):
        nombre, stock, descripcion, precio, iva = self.ask_producto()
        out = self.model.create_producto(nombre, stock, descripcion, precio, iva)
        if out == True:
            self.view.ok(nombre +'agrego')
        else: 
            self.view.error('NO SE PUDO AGREGAR EL PRODUCTO. REVISA.')
            return
        
    #leer un producto, usuario indica ID
    def read_a_producto(self):
        self.view.ask('ID producto: ')
        id_producto = input()
        producto = self.model.read_a_producto(id_producto)
        if type(producto) == tuple:
            self.view.show_producto_header(' Datos del producto' + id_producto + ' ')
            self.view.show_a_producto(producto)
            self.view.show_producto_middler()
            self.view.show_producto_footer()
        else: 
            if producto == None:
                self.view.error('EL PRODUCTO NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER EL PRODUCTO. REVISA')
        return
    
    #LEER TODOS LOS PRODUCTOS
    def read_all_productos(self):
        productos = self.model.read_all_productos()
        if type(productos) == list:
            self.view.show_producto_header(' Todos los productos ')
            for producto in productos:
                self.view.show_a_producto(producto)
                self.view.show_producto_middler()
            self.view.show_producto_footer()
        else: 
            self.view.error('PROBLEMA AL LEER LOS PRODUCTOS. REVISA')
        return
    #ACTUALIZAR UN PRODUCTO
    def update_producto(self):
        self.view.ask('ID  de producto a modificar: ')
        id_producto = input()
        producto = self.model.read_a_producto(id_producto)
        if type(producto) == tuple: #Si se pudo recuperar el producto
            self.view.show_producto_header(' Datos del producto' + id_producto + ' ')
            self.view.show_a_producto(producto)
            self.view.show_producto_middler()
            self.view.show_producto_footer()
        else: 
            if producto == None:
                self.view.error('EL PRODUCTO NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER EL PRODUCTO. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacío para dejarlo igual):')
        whole_vals = self.ask_producto()
        fields, vals = self.update_lists(['nombre_producto','stock','descripcion','precio','iva'], whole_vals)    
        vals.append(id_producto)
        vals = tuple(vals)
        out = self.model.update_producto(fields, vals)
        if out == True: 
            self.view.ok(id_producto, 'actualizado')
        else: 
            self.view.ok(' NO SE PUDO ACTUALIZAR EL PRODUCTO. REVISA')
        return

    #ELIMINAR UN PRODUCTO 
    def delete_producto(self):
        self.view.ask('Id de producto a borrar: ')
        id_producto = input()
        count = self.model.delete_producto(id_producto)
        if count != 0:
            self.view.ok(id_producto, 'borro')
        else: 
            if count == 0:
                self.view.error(' EL PRODUCTO NO EXISTE ')
            else: 
                self.view.error('PROBLEMA AL BORRAR EL PRODUCTO. REVISA.')
        return
    
#****************CONTROLADOR PARA CLIENTES CONSENTIDOS********************************
    def clientesConsentidos_menu(self):
        o = '0'
        while o != '6':
            self.view.clientesConsentidos_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_clienteConsentido()
            elif o == '2': 
                self.read_a_clienteConsentido()
            elif o =='3':
                self.read_all_clientesConsentidos()
            elif o =='4':
                self.update_clienteConsentido()
            elif o =='5':
                self.delete_clienteConsentido()
            elif o =='6':
                return
            else:
                self.view.not_valid_option()
        return
    
    #Solicitar datos para escribir o actualizar info
    def ask_clienteConsentido(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Credito disponible: ')
        credito_disponible = input()
        self.view.ask('Credito que debe: ')
        credito_debe = input()
        self.view.ask('Credito asignado: ')
        credito_asignado = input()
        return[nombre, credito_disponible, credito_debe, credito_asignado]
    
    #Crear un clienteConsentido
    def create_clienteConsentido(self):
        self.view.ask('ID: ')
        id_clienteConsentido = input()
        nombre, credito_disponible, credito_debe, credito_asignado = self.ask_clienteConsentido()
        out = self.model.create_producto(id_clienteConsentido, nombre, credito_disponible, credito_debe, credito_asignado)
        if out == True:
            self.view.ok(id_clienteConsentido, 'agrego')
        else: 
            if out.errno == 1062:
                self.view.error('EL ID ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL cliente consentido. REVISA.')
            return
        
    #leer un clienteConsentido, usuario indica ID
    def read_a_clienteConsentido(self):
        self.view.ask('ID cliente consentido: ')
        id_clienteConsentido = input()
        clienteConsentido = self.model.read_a_clienteConsentido(id_clienteConsentido)
        if type(clienteConsentido) == tuple:
            self.view.show_clienteConsentido_header(' Datos del cliente Consentido' + id_clienteConsentido + ' ')
            self.view.show_a_clienteConsentido(clienteConsentido)
            self.view.show_clienteConsentido_middler()
            self.view.show_clienteConsentido_footer()
        else: 
            if clienteConsentido == None:
                self.view.error('EL Cliente consentido NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER cliente consentido. REVISA')
        return
    
    #LEER TODOS LOS CLIENTES CONSENTIDOS
    def read_all_clientesConsentidos(self):
        clientesConsentidos = self.model.read_all_clientesConsentidos()
        if type(clientesConsentidos) == list:
            self.view.show_clienteConsentido_header(' Todos los clientes consentidos ')
            for clienteConsentido in clientesConsentidos:
                self.view.show_a_clienteConsentido(clienteConsentido)
                self.view.show_clienteConsentido_middler()
            self.view.show_clienteConsentido_footer()
        else: 
            self.view.error('PROBLEMA AL LEER LOS clientes Consentidos. REVISA')
        return
    #ACTUALIZAR UN CLIENTE CONSENTIDO
    def update_clienteConsentido(self):
        self.view.ask('ID  de cliente consentido a modificar: ')
        id_clienteConsentido = input()
        clienteConsentido = self.model.read_a_cliente(id_clienteConsentido)
        if type(clienteConsentido) == tuple: #Si se pudo recuperar el producto
            self.view.show_clienteConsentido_header(' Datos del cliente consentido' + id_clienteConsentido + ' ')
            self.view.show_a_clienteConsentido(clienteConsentido)
            self.view.show_clienteConsentido_middler()
            self.view.show_clienteConsentido_footer()
        else: 
            if clienteConsentido == None:
                self.view.error('EL CLIENTE CONSENTIDO NO EXISTE')
            else: 
                self.view.error('PROBLEMA AL LEER EL CLIENTE CONSENTIDO. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacío para dejarlo igual):')
        whole_vals = self.ask_clienteConsentido()
        fields, vals = self.update_lists(['nombre', 'credito_disponible', 'credito_debe', 'credito_asignado'], whole_vals)    
        vals.append(id_clienteConsentido)
        vals = tuple(vals)
        out = self.model.update_cliente(fields, vals)
        if out == True: 
            self.view.ok(id_clienteConsentido, 'actualizado')
        else: 
            self.view.ok(' NO SE PUDO ACTUALIZAR EL CLIENTE CONSENTIDO. REVISA')
        return

    #ELIMINAR UN CLIENTE CONSENTIDO
    def delete_clienteConsentido(self):
        self.view.ask('Id de cliente consentido a borrar: ')
        id_clienteConsentido = input()
        count = self.model.delete_cliente(id_clienteConsentido)
        if count != 0:
            self.view.ok(id_clienteConsentido, 'borro')
        else: 
            if count == 0:
                self.view.error(' EL CLIENTE CONSENTIDO NO EXISTE ')
            else: 
                self.view.error('PROBLEMA AL BORRAR EL CLIENTE CONSENTIDO. REVISA.')
        return

