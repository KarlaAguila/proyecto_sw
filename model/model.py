from mysql import connector

class Model: 
    #modelo de datos con MySQL para una tienda de abarrotes 
    def __init__(self, config_db_file = 'config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    #leer archivo de configuración
    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val #transformo archivo en diccionario

        return d
    
    #Crear conexión a base de datos
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()
    
    #cerrar conexión
    def close_db(self):
        self.cnx.close()

    #MÉTODOS RELACIONADOS CON ENCARGADO
    #CREAR UN NUEVO ENCARGADO
    def create_encargado(self, id_encargado, nombre_encargado): 
        try:
            sql = 'INSERT INTO encargado (`id_encargado`, `nombre_encargado`) VALUES (%s, %s)'
            vals = (id_encargado, nombre_encargado)
            self.cursor.execute(sql, vals)
            self.cnx.commit() #confirmar cambios dentro de bd
            return True
        except connector.Error as err:
            self.cnx.rollback() #si hay error regresa a la forma normal
            return err
        
    #LEER UN USUARIO ENCARGADO
    def read_a_encargado(self, id_encargado): 
        try:
            sql = 'SELECT * FROM encargado WHERE id_encargado = %s'
            vals = (id_encargado,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 

    #LEER TODOS LOS ENCARGADO  
    def read_all_encargados(self):
        try: 
            sql = 'SELECT * FROM encargado'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err     
        
    #recuperar id con un nombre
    def read_encargado_nombre(self, nombre_encargado):
        try: 
            sql = 'SELECT * FROM encargado WHERE nombre_encargado = %s'
            vals = (nombre_encargado,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #actualizar un encargado
    def update_encargado(self, fields, vals):
        try: 
            sql = 'UPDATE encargado SET' + ','.join(fields)+'WHERE id_encargado = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err: 
            self.cnx.rollback()
            return err

    #borrar un encargado
    def delete_encargado(self, id_encargado): 
        try: 
            sql = 'DELETE FROM encargo WHERE id_encargado = %s'
            vals = (id_encargado, )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err: 
            self.cnx.rollback()
            return err


    #MÉTODOS RELACIONADOS CON PRODUCTO
    #CREAR UN PRODUCTO
    def create_producto(self, nombre_producto, stock, descripcion, precio, iva, imagen): 
        try:
            sql = 'INSERT INTO producto (`nombre_producto`, `stock`, `descripcion`, `precio`, `iva`, `imagen`) VALUES (%s, %s, %s, %s, %s, %s)'
            vals = (nombre_producto, stock, descripcion, precio, iva, imagen)
            self.cursor.execute(sql, vals)
            self.cnx.commit() #confirmar cambios dentro de bd
            return True
        except connector.Error as err:
            self.cnx.rollback() #si hay error regresa a la forma normal
            return err
        
    #LEER UN PRODUCTO
    def read_a_producto(self, id_producto): 
        try:
            sql = 'SELECT * FROM producto WHERE id_producto = %s'
            vals = (id_producto,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 
    #LEER TODOS LOS PRODUCTOS (INVENTARIO) 
    def read_all_productos(self):
        try: 
            sql = 'SELECT * FROM producto'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err     

    #ACTUALIZAR UN PRODUCTO
    def update_producto(self, fields, vals):
        try: 
            sql = 'UPDATE producto SET' + ','.join(fields)+'WHERE id_producto = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err: 
            self.cnx.rollback()
            return err

    #BORRAR UN PRODUCTO
    def delete_producto(self, id_producto): 
        try: 
            sql = 'DELETE FROM producto WHERE id_producto = %s'
            vals = (id_producto, )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err: 
            self.cnx.rollback()
            return err       

    #MÉTODOS RELACIONADOS CON CLIENTE CONSENTIDO
    #CREAR UN CLIENTE CONSENTIDO
    def create_cliente(self, id_cliente, nombre_cliente, credito_disponible, credito_debe, credito_asignado): 
        try:
            sql = 'INSERT INTO clienteconsentido (`id_cliente`, `nombre_cliente`, `credito_disponible`, `credito_debe`, `credito_asignado`) VALUES (%s, %s, %s, %s, %s)'
            vals = (id_cliente, nombre_cliente, credito_disponible, credito_debe, credito_asignado)
            self.cursor.execute(sql, vals)
            self.cnx.commit() #confirmar cambios dentro de bd
            return True
        except connector.Error as err:
            self.cnx.rollback() #si hay error regresa a la forma normal
            return err
        
    #LEER UN CLIENTE
    def read_a_cliente(self, id_cliente): 
        try:
            sql = 'SELECT * FROM clienteconsentido WHERE id_cliente = %s'
            vals = (id_cliente,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 
    #LEER TODOS LOS CLIENTES (INVENTARIO) 
    def read_all_clientes(self):
        try: 
            sql = 'SELECT * FROM clienteconsentido'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err     

    #ACTUALIZAR UN CLIENTE
    def update_cliente(self, fields, vals):
        try: 
            sql = 'UPDATE clienteconsentido SET' + ','.join(fields)+'WHERE id_cliente = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err: 
            self.cnx.rollback()
            return err

    #BORRAR UN CLIENTE
    def delete_cliente(self, id_cliente): 
        try: 
            sql = 'DELETE FROM clienteconsentido WHERE id_cliente = %s'
            vals = (id_cliente, )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err: 
            self.cnx.rollback()
            return err
    
    
#MÉTODOS RELACIONADOS CON DUENO
    #CREAR UN NUEVO DUENO
    def create_dueno(self, id_dueno, nombre_dueno): 
        try:
            sql = 'INSERT INTO dueno (`id_dueno`, `nombre_dueno`) VALUES (%s, %s)'
            vals = (id_dueno, nombre_dueno)
            self.cursor.execute(sql, vals)
            self.cnx.commit() #confirmar cambios dentro de bd
            return True
        except connector.Error as err:
            self.cnx.rollback() #si hay error regresa a la forma normal
            return err
        
    #LEER UN USUARIO DUENO
    def read_a_dueno(self, id_dueno): 
        try:
            sql = 'SELECT * FROM dueno WHERE id_dueno = %s'
            vals = (id_dueno,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 

    #LEER TODOS LOS DUENO
    def read_all_duenos(self):
        try: 
            sql = 'SELECT * FROM dueno'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err     
        
    #recuperar id con un nombre
    def read_dueno_nombre(self, nombre_dueno):
        try: 
            sql = 'SELECT * FROM dueno WHERE nombre_dueno = %s'
            vals = (nombre_dueno,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #actualizar un dueno
    def update_dueno(self, fields, vals):
        try: 
            sql = 'UPDATE dueno SET' + ','.join(fields)+'WHERE id_dueno = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err: 
            self.cnx.rollback()
            return err

    #borrar un DUENO
    def delete_dueno(self, id_dueno): 
        try: 
            sql = 'DELETE FROM encargo WHERE id_dueno = %s'
            vals = (id_dueno, )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err: 
            self.cnx.rollback()
            return err
