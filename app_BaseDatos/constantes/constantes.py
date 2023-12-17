##############################################################
######################### CONSTANTES #########################
##############################################################

#--------------------------> ENTRY
##### Fuentes
# Tipo
fuente_tipo_entry = 'Arial'
# Tamaño
fuente_tamaño_entry = 12

#### Posicion
posicion_x_col1_fil1_entry = 250
posicion_y_col1_fil1_entry = 15
posicion_x_col1_fil2_entry = 250
posicion_y_col1_fil2_entry = 55

posicion_x_col2_fil1_entry = 720
posicion_y_col2_fil1_entry = 15
posicion_x_col2_fil2_entry = 720
posicion_y_col2_fil2_entry = 55

posicion_x_col3_fil1_entry = 1210
posicion_y_col3_fil1_entry = 15
posicion_x_col3_fil2_entry = 1210
posicion_y_col3_fil2_entry = 55

#### Dimension
dimension_x_entry = 30
dimension_y_entry = 50

dimension_x_comb = 43
dimension_y_comb = 50
#--------------------------------------#
#--------------------------------------#


#--------------------------> BOTONES
##### Fuentes
# Tipo
fuente_tipo_boton = 'Arial'
# Tamaño
fuente_tamaño_boton = 10
# Diseño
fuente_diseño_boton = 'bold'

#### Nombres
boton_InsertarParametro = 'Insertar parámetro'
boton_EliminarParametro = 'Eliminar parámetro'
boton_InsertarCategoria = 'Insertar categoría'
boton_InsertarTrasnstorno = 'Insertar transtorno'
boton_EliminarTrasnstorno = 'Eliminar transtorno'
boton_Guardar = 'Guardar'
boton_Cancelar = 'Cancelar'
boton_Actualizar = 'Actualizar'
boton_Eliminar = 'Eliminar'

#### Posicion
posicion_x_InsertarParametro_boton = 70
posicion_y_InsertarParametro_boton = 10

posicion_x_EliminarParametro_boton = 70
posicion_y_EliminarParametro_boton = 50

posicion_x_InsertarCategoria_boton = 550
posicion_y_InsertarCategoria_boton = 15

posicion_x_InsertarTranstornos_boton = 1020
posicion_y_InsertarTranstornos_boton = 10

posicion_x_EliminarTranstornos_boton = 550
posicion_y_EliminarTranstornos_boton = 50

posicion_x_Guardar_boton = 70
posicion_y_Guardar_boton = 100

posicion_x_Cancelar_boton = 250
posicion_y_Cancelar_boton = 100

posicion_x_Actualizar_boton = 925
posicion_y_Actualizar_boton = 100

posicion_x_Eliminar_boton = 70
posicion_y_Eliminar_boton = 400

#### Dimension
dimension_x_boton = 15

#### Color
# Front
colorFront_insertar_boton = 'blue'
colorFront_eliminar_boton = 'red'
colorFront_guardar_boton = 'green'
colorFront_cancelar_boton = colorFront_eliminar_boton
colorFront_actualizar_boton = 'black'
# Back
colorBack_insertar_boton = 'white'
colorBack_eliminar_boton = 'white'
colorBack_guardar_boton = 'white'
colorBack_cancelar_boton = colorBack_eliminar_boton
colorBack_actualizar_boton = 'white'
# Active
colorActive_insertar_boton = 'blue'
colorActive_eliminar_boton = 'red'
colorActive_guardar_boton = 'green'
colorActive_cancelar_boton = colorActive_eliminar_boton
colorActive_actualizar_boton = 'black'
#--------------------------------------#
#--------------------------------------#


#--------------------------> CHECKBOX
#### Nombres
checkbox_BDParametros = 'DB parámetros'
checkbox_BDCategoria = 'DB categoria'
checkbox_BDTranstornos = 'DB transtornos'
#### Posicion
posicion_x_BDParametros_checkbox = 1500
posicion_y_BDParametros_checkbox = 150

posicion_x_BDCategoria_checkbox = 1500
posicion_y_BDCategoria_checkbox = 250

posicion_x_BDTranstornos_checkbox = 1500
posicion_y_BDTranstornos_checkbox = 350
### Valor Default
checkbox_valor_default = False
#--------------------------------------#
#--------------------------------------#


#--------------------------> TABLA
#### Posicion
posicion_x_tabla = 70
posicion_y_tabla = 150

#### Dimension
dimension_x_tabla = 1400
#--------------------------------------#
#--------------------------------------#


#--------------------------> RUTAS
#### Archivos
ruta_plantilla = "./plantilla/"
ruta_name_archivo = "umind_bd.xlsx"
#### Base de datos
ruta_DB = "database/transtornos.db"
#--------------------------------------#
#--------------------------------------#


#--------------------------> COLUMNAS DB
columnas_trastornos_default =  ['categoria', 'transtornos']
columnas_categoria_default = ['categoria']
columnas_tipotrastornos_default = ['version', 'categoria', 'tipo_trastornos']

nombre_tabla_trastornos = 'transtornos'
nombre_tabla_categoria = 'categoria'
nombre_tabla_tipotrastornos = 'tipo_trastornos'