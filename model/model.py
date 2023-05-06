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
            vals = (zip, )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err: 
            self.cnx.rollback()
            return err


