from.conexion_db import ConexionDB
from mensajes import mensaje
import constantes.constantes as cte

columnas_trastornos = cte.columnas_trastornos_default
columnas_categoria = cte.columnas_categoria_default
columnas_tipotrastornos = cte.columnas_tipotrastornos_default

nombre_tabla_trastornos = cte.nombre_tabla_trastornos
nombre_tabla_categoria = cte.nombre_tabla_categoria
nombre_tabla_tipotrastornos = cte.nombre_tabla_tipotrastornos


# Tabla principal
def crear_tabla(columnas):

    conexion = ConexionDB()

    try:
        for i in range(0,len(columnas)):
            create_sql = f'''
            CREATE TABLE {nombre_tabla_trastornos}(
            id_trastornos INTEGER,
            {columnas[i]} VARCHAR(100),
            PRIMARY KEY(id_trastornos AUTOINCREMENT)
            ) '''
            conexion.cursor.execute(create_sql)
        conexion.cerrar()
        mensaje('Crear Registro',
                'Se ha creado registro en la Base de Datos',
                0)
    except:
        mensaje('Crear Registro',
                'Ya existe registro en la Base de Datos',
                1)

    insertar_col(columnas[1])

def borrar_tabla():
    conexion = ConexionDB()
    sql = f'DROP TABLE {nombre_tabla_trastornos}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        mensaje('Eliminar Registro',
                'Se ha eliminado el registro en la Base de Datos',
                0)
    except:
        mensaje('Eliminar Registro',
                'No existe ningun registro en la Base de Datos',
                1)

def check_tabla_parametros():
    conexion = ConexionDB()

    sql = f'SELECT * from {nombre_tabla_trastornos}'

    try:
        conexion.cursor.execute(sql)
    except:
        checkbox = False
    else:
        checkbox = True

    return checkbox

class Transtorno:
    def __init__(self,transtorno ,columnas):
        self.id_transtornos = None
        self.transtorno = transtorno
        for i in columnas:
            self.i = i

def insertar_col(new_col):

    conexion = ConexionDB()

    sql = f'''ALTER TABLE {nombre_tabla_trastornos}
          ADD {new_col} VARCHAR(100)'''
    conexion.cursor.execute(sql)

def eliminar_col(name_col):

    conexion = ConexionDB()

    sql = f'''ALTER TABLE {nombre_tabla_trastornos}
          DROP COLUMN {name_col}'''

    conexion.cursor.execute(sql)

def eliminar_fila(id_trastornos):
    conexion = ConexionDB()

    sql = f"""DELETE FROM {nombre_tabla_trastornos} WHERE id_trastornos = {id_trastornos}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        mensaje('Eliminar datos',
                'No se ha podido eliminar de la tabla',
                2)

def obtener_parametros():

    conexion = ConexionDB()

    lista_trast = []

    sql = f'PRAGMA table_info({nombre_tabla_trastornos})'

    try:
        conexion.cursor.execute(sql)
        lista_parametros = conexion.cursor.fetchall()
        conexion.cerrar()

    except:
        pass

    try:
        for x in range(1, len(lista_parametros)):
            param = lista_parametros[x]
            param = param[1]
            lista_trast.insert(x, param)

    except:
        pass

    return lista_trast

def obtener_contenido():

    conexion = ConexionDB()

    lista_cont = []
    cont = 0

    sql = f'SELECT * FROM {nombre_tabla_trastornos}'

    try:
        conexion.cursor.execute(sql)
        lista_contenido = conexion.cursor.fetchall()
    except:
        pass

    try:
        for x in lista_contenido:
            lista_cont.insert(cont, x)
            cont = +1
    except:
        pass

    return lista_cont


# Tabla Categoria de Trastornos
def crear_tabla_categoria(columnas):

    conexion = ConexionDB()

    try:
        for i in range(0, len(columnas)):
            create_sql = f'''
            CREATE TABLE {nombre_tabla_categoria}(
            id_trastornos INTEGER,
            {columnas[0]} VARCHAR(100),
            PRIMARY KEY(id_trastornos AUTOINCREMENT)
            ) '''
        conexion.cursor.execute(create_sql)
        conexion.cerrar()
    except:
        mensaje('Crear Registro',
                'Ya existe registro en la Base de Datos de categoria',
                1)
    else:
        mensaje('Crear Registro',
                'Se ha creado registro en la Base de Datos',
                0)

    #insertar_col_categoria(columnas[0])

def borrar_tabla_categoria():
    conexion = ConexionDB()
    sql = f'DROP TABLE {nombre_tabla_categoria}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        mensaje('Eliminar Registro',
                'Se ha eliminado el registro en la Base de Datos',
                0)
    except:
        mensaje('Eliminar Registro',
                'No existe ningun registro en la Base de Datos',
                1)

def check_tabla_categoria():
    conexion = ConexionDB()

    sql = f'SELECT * from {nombre_tabla_categoria}'

    try:
        conexion.cursor.execute(sql)
    except:
        checkbox = False
    else:
        checkbox = True

    return checkbox

class Categoria:
    def __init__(self,categoria):
        self.id_categoria = None
        self.categoria = categoria

    def __str__(self):
        return f'Categoria[{self.categoria}]'

def guardar_categoria(categoria,checkbox_value):

    conexion = ConexionDB()

    sql = f"""INSERT INTO categoria (categoria) 
    VALUES('{categoria}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        mensaje('Conexion al Registro',
                'La tabla no está creada en la base de datos',
                2)
    else:
        checkbox_value = True

def insertar_col_categoria(new_col):

    conexion = ConexionDB()

    sql = f"""INSERT INTO categoria (categoria) 
    VALUES('{new_col}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        mensaje('Conexion al Registro',
                'La tabla no está creada en la base de datos',
                2)

def eliminar_categoria(categoria,checkbox_value):

    conexion = ConexionDB()

    sql = f"""DELETE FROM categoria WHERE categoria = '{categoria}'"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        mensaje('Eliminar datos',
                'No se ha podido eliminar de la tabla',
                2)
    else:
        checkbox_value = False

def obtener_categoria():

    conexion = ConexionDB()

    lista_categoria_ = []
    cont=0

    sql = f'SELECT categoria FROM {nombre_tabla_categoria}'

    try:
        conexion.cursor.execute(sql)
        lista_categoria = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        pass

    try:
        for x in lista_categoria:
            lista_categoria_.insert(cont, x[0])
            cont = +1
    except:
        pass

    return lista_categoria_


# Tabla Tipo de Trastornos
def crear_tabla_sec(columnas):

    conexion = ConexionDB()

    try:
        for i in range(0, len(columnas)+1):
            create_sql = f'''
            CREATE TABLE {nombre_tabla_tipotrastornos}(
            id_trastornos INTEGER,
            {columnas[0]} VARCHAR(100),
            PRIMARY KEY(id_trastornos AUTOINCREMENT)
            ) '''
        conexion.cursor.execute(create_sql)
        conexion.cerrar()
    except:
        mensaje('Crear Registro',
                'Ya existe registro en la Base de Datos de tipo de trastornos',
                1)
    else:
        mensaje('Crear Registro',
                'Se ha creado registro en la Base de Datos',
                0)

    insertar_col_tt(columnas[1])
    insertar_col_tt(columnas[2])

def borrar_tabla_sec():
    conexion = ConexionDB()
    sql = f'DROP TABLE {nombre_tabla_tipotrastornos}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        mensaje('Eliminar Registro',
                'Se ha eliminado el registro en la Base de Datos',
                0)
    except:
        mensaje('Eliminar Registro',
                'No existe ningun registro en la Base de Datos',
                1)

def check_tabla_trastornos():
    conexion = ConexionDB()

    sql = f'SELECT * from {nombre_tabla_tipotrastornos}'

    try:
        conexion.cursor.execute(sql)
    except:
        checkbox = False
    else:
        checkbox = True

    return checkbox

class Tipo_Trastornos:
    def __init__(self,tipo_trastorno):
        self.id_tipo_trastornos = None
        self.tipo_trastorno = tipo_trastorno

    def __str__(self):
        return f'Tipo_Trastornos[{self.tipo_trastorno}]'

def guardar_tipotrastornos(version,categoria,tipo_trastornos):

    conexion = ConexionDB()

    sql = f"""INSERT INTO tipo_trastornos (version,categoria,tipo_trastornos) 
    VALUES('{version[0]}','{categoria}','{tipo_trastornos}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        mensaje('Conexion al Registro',
                'La tabla no está creada en la base de datos',
                2)

def insertar_col_tt(new_col):

    conexion = ConexionDB()

    sql = f'''ALTER TABLE {nombre_tabla_tipotrastornos}
          ADD {new_col} VARCHAR(100)'''
    conexion.cursor.execute(sql)

def eliminar_tipotrastornos(tipo_trastornos):

    conexion = ConexionDB()

    sql = f"""DELETE FROM tipo_trastornos WHERE tipo_trastornos = '{tipo_trastornos}'"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        mensaje('Eliminar datos',
                'No se ha podido eliminar de la tabla',
                2)

def obtener_tipos_trastornos():

    conexion = ConexionDB()

    lista_trast = []
    cont = 0

    sql = 'SELECT tipo_trastornos FROM tipo_trastornos'

    try:
        conexion.cursor.execute(sql)
        lista_trastornos_tt = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        pass

    try:
        for x in lista_trastornos_tt:
            x = x[0]
            lista_trast.insert(cont, x)
            cont = +1
    except:
        pass

    return lista_trast

def obtener_Categoria_tipostrastornos():

    conexion = ConexionDB()

    lista_categoria_trast = []
    cont = 0

    sql = 'SELECT categoria, tipo_trastornos FROM tipo_trastornos'

    try:
        conexion.cursor.execute(sql)
        lista_trastornos_tt = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        pass

    try:
        for x in lista_trastornos_tt:
            lista_categoria_trast.insert(cont, x[0] + " - " + x[1])
            cont = +1
    except:
        pass

    return lista_categoria_trast

def obtener_version_tipos_trastornos():
    conexion = ConexionDB()

    sql = 'SELECT * FROM tipo_trastornos'

    try:
        conexion.cursor.execute(sql)
        lista_trastornos_tt = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        pass

    return lista_trastornos_tt