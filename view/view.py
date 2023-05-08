class View:
    def start(self): 
        print('==========================')
        print('=   STOCK DE PRODUCTOS   =')
        print('==========================')

    def end(self):
        print('==========================')
        print('=          BYE           =')
        print('==========================')       

    def main_menu(self):
        print('==== ======================')
        print('=      MENU PRINCIPAL    =')
        print('==========================')
        print('1.Productos')  
        print('2.Clientes')  
        print('3. Corte de caja')  
        print('4. Salir')
    
    def option(self, last):
        print('Selecciona una opción (1-'+last+'):', end = '')

    def not_valid_option(self):
        print('Opción no valida \nIntenta de nuevo')

    def ask(self, output):
        print(output, end = '')

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24)) #repite carácter 24 veces
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' ¡ERROR! '.center(len(err)+4, '-'))
        print('- '+err+ ' -')
        print('+'*(len(err)+4))


    def productos_menu(self):
        print('==========================')
        print('=      PRODUCTOS         =')
        print('==========================')
        print('1. Agregar producto')  
        print('2. Leer un producto')  
        print('3. Leer todos los productos') 
        print('4. Actualizar un producto') 
        print('5. Borrar un producto') 
        print('6. Regresar') 

    def show_a_producto(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Stock:', record[2])
        print('Descripcion:', record[3])
        print('Precio:', record[4])
        print('Iva:', record[5])
        #print('Imagen:', record[0])

    def show_producto_header(self, header):
        print(header.center(48, '*'))
        print('-'*48)

    def show_producto_middler(self):
        print('-'*48)

    def show_producto_footer(self):
        print('*'*48)

    def clientesConsentidos_menu(self):
        print('==========================')
        print('=  CLIENTES CONSENTIDOS  =')
        print('==========================')
        print('1. Agregar Cliente Consentido')  
        print('2. Leer un Cliente Consentido')  
        print('3. Leer todos los Cliente Consentidos') 
        print('4. Actualizar un Cliente Consentido') 
        print('5. Borrar un Cliente Consentido') 
        print('6. Regresar') 

    def show_a_clienteConsentido(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Credito disponible:', record[2])
        print('Credito que debe:', record[3])
        print('Credito asignado:', record[4])

    def show_clienteConsentido_header(self, header):
        print(header.center(48, '*'))
        print('-'*48)
        
    def show_clienteConsentido_middler(self):
        print('-'*48)

    def show_clienteConsentido_footer(self):
        print('*'*48)
