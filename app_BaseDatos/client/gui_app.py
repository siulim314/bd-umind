import sqlite3
import tkinter as tk
from tkinter import ttk
#import version.version_window as version
from version.version_window import *
from mensajes import mensaje
import exp_imp.exportar_importar as exim
from model.transtornos_dao import crear_tabla, borrar_tabla, crear_tabla_sec, borrar_tabla_sec,\
                                insertar_col, eliminar_col, obtener_parametros, columnas_trastornos, \
                                guardar_tipotrastornos, eliminar_tipotrastornos, obtener_tipos_trastornos,\
                                obtener_contenido,eliminar_fila, columnas_tipotrastornos, \
                                obtener_version_tipos_trastornos, nombre_tabla_trastornos, nombre_tabla_tipotrastornos, \
                                guardar_categoria, crear_tabla_categoria, borrar_tabla_categoria, columnas_categoria, \
                                insertar_col_categoria, obtener_categoria
import constantes.constantes as cte

class Frame(tk.Frame):

    def __init__(self, ancho, largo, app = None):
        super().__init__(app)
        self.ancho = ancho
        self.largo = largo
        self.app = app
        self.pack()
        self.config(width=ancho , height=largo)

        self.tabla_info()
        self.parametros()

    def parametros(self):
        # Entry

        # Columna 1 Fila 1
        self.mi_intro_parametro = tk.StringVar()
        self.entry_intro_parametro = tk.Entry(self, textvariable = self.mi_intro_parametro)
        self.entry_intro_parametro.config(width=cte.dimension_x_entry, state='disable', font=(cte.fuente_tipo_entry, cte.fuente_tamaño_entry))
        self.entry_intro_parametro.place(x=cte.posicion_x_col1_fil1_entry, y=cte.posicion_y_col1_fil1_entry)

        # Columna 1 Fila 2
        self.mi_eliminar_parametro = tk.StringVar()
        columnas_par = []
        for x in range(1, len(self.obtener_param())):
            param = self.obtener_param()[x]
            columnas_par.insert(x, param)
        self.columnas_par = columnas_par
        self.entry_eliminar_parametro = ttk.Combobox(self, state="readonly",
                                                     width=cte.dimension_x_comb, height=cte.dimension_y_comb, values = self.columnas_par,
                                                     textvariable=self.mi_eliminar_parametro)
        self.entry_eliminar_parametro.place(x=cte.posicion_x_col1_fil2_entry, y=cte.posicion_y_col1_fil2_entry)
        self.entry_eliminar_parametro.config(state='disable')

        # Columna 2 Fila 1
        self.mi_intro_categoria = tk.StringVar()
        self.mi_intro_categoria_comb = tk.StringVar()
        columnas_cat = []
        for x in range(0, len(self.obtener_categoria())):
            cat = self.obtener_categoria()[x]
            columnas_cat.insert(x, cat)
        self.columnas_cat = columnas_cat
        self.entry_intro_categoria = tk.Entry(self, textvariable=self.mi_intro_categoria)
        self.entry_intro_categoria.config(width=cte.dimension_x_entry, state='disable', font=(cte.fuente_tipo_entry, cte.fuente_tamaño_entry))
        self.entry_intro_categoria.place(x=cte.posicion_x_col2_fil1_entry, y=cte.posicion_y_col2_fil1_entry)

        # Columna 3 Fila 1
        self.entry_intro_categoria_comb = ttk.Combobox(self, state="readonly",
                                                     width=cte.dimension_x_comb, height=cte.dimension_y_comb, values = self.columnas_cat,
                                                     textvariable=self.mi_intro_categoria_comb)
        self.entry_intro_categoria_comb.config(state='disable')
        self.entry_intro_categoria_comb.place(x=cte.posicion_x_col3_fil1_entry, y=cte.posicion_y_col3_fil1_entry)

        # Columna 3 Fila 2
        self.mi_intro_transtorno = tk.StringVar()
        self.entry_intro_transtorno = tk.Entry(self, textvariable = self.mi_intro_transtorno)
        self.entry_intro_transtorno.config(width=cte.dimension_x_entry, state='disable', font=(cte.fuente_tipo_entry, cte.fuente_tamaño_entry))
        self.entry_intro_transtorno.place(x=cte.posicion_x_col3_fil2_entry, y=cte.posicion_y_col3_fil2_entry)

        # Columna 2 Fila 2
        self.mi_eliminar_transtorno = tk.StringVar()
        self.entry_eliminar_transtorno = ttk.Combobox(self, state="readonly",
                                                     width=cte.dimension_x_comb, height=cte.dimension_y_comb, values = obtener_tipos_trastornos(),
                                                     textvariable=self.mi_eliminar_transtorno)
        self.entry_eliminar_transtorno.place(x=cte.posicion_x_col2_fil2_entry, y=cte.posicion_y_col2_fil2_entry)
        self.entry_eliminar_transtorno.config(state='disable')

        # Botones
        self.boton_intro_parametro = tk.Button(self, text=cte.boton_InsertarParametro, command = self.habilitar_intro_parametro)
        self.boton_intro_parametro.config(width=cte.dimension_x_boton, font=(cte.fuente_tipo_boton, cte.fuente_tamaño_boton, cte.fuente_diseño_boton),
                                          fg=cte.colorFront_insertar_boton, bg=cte.colorBack_insertar_boton, activebackground=cte.colorActive_insertar_boton)
        self.boton_intro_parametro.place(x=cte.posicion_x_InsertarParametro_boton, y=cte.posicion_y_InsertarParametro_boton)

        self.boton_eliminar_parametro = tk.Button(self, text=cte.boton_EliminarParametro, command = self.habilitar_eliminar_parametro)
        self.boton_eliminar_parametro.config(width=cte.dimension_x_boton, font=(cte.fuente_tipo_boton, cte.fuente_tamaño_boton, cte.fuente_diseño_boton),
                                             fg=cte.colorFront_eliminar_boton, bg=cte.colorBack_eliminar_boton, activebackground=cte.colorActive_eliminar_boton)
        self.boton_eliminar_parametro.place(x=cte.posicion_x_EliminarParametro_boton, y=cte.posicion_y_EliminarParametro_boton)

        self.boton_intro_categoria = tk.Button(self, text=cte.boton_InsertarCategoria, command = self.habilitar_intro_categoria)
        self.boton_intro_categoria.config(width=cte.dimension_x_boton, font=(cte.fuente_tipo_boton, cte.fuente_tamaño_boton, cte.fuente_diseño_boton),
                                          fg=cte.colorFront_insertar_boton, bg=cte.colorBack_insertar_boton, activebackground=cte.colorActive_insertar_boton)
        self.boton_intro_categoria.place(x=cte.posicion_x_InsertarCategoria_boton, y=cte.posicion_y_InsertarCategoria_boton)

        self.boton_intro_transtorno = tk.Button(self, text=cte.boton_InsertarTrasnstorno, command = self.habilitar_intro_transtorno)
        self.boton_intro_transtorno.config(width=cte.dimension_x_boton, font=(cte.fuente_tipo_boton, cte.fuente_tamaño_boton, cte.fuente_diseño_boton),
                                           fg=cte.colorFront_insertar_boton, bg=cte.colorBack_insertar_boton, activebackground=cte.colorActive_insertar_boton)
        self.boton_intro_transtorno.place(x=cte.posicion_x_InsertarTranstornos_boton, y=cte.posicion_y_InsertarTranstornos_boton)

        self.boton_eliminar_transtornos = tk.Button(self, text=cte.boton_EliminarTrasnstorno, command = self.habilitar_eliminar_transtorno)
        self.boton_eliminar_transtornos.config(width=cte.dimension_x_boton, font=(cte.fuente_tipo_boton, cte.fuente_tamaño_boton, cte.fuente_diseño_boton),
                                               fg=cte.colorFront_eliminar_boton, bg=cte.colorBack_eliminar_boton, activebackground=cte.colorActive_eliminar_boton)
        self.boton_eliminar_transtornos.place(x=cte.posicion_x_EliminarTranstornos_boton, y=cte.posicion_y_EliminarTranstornos_boton)

        self.boton_guardar = tk.Button(self, text=cte.boton_Guardar, command = self.guardar)
        self.boton_guardar.config(width=cte.dimension_x_boton, font=(cte.fuente_tipo_boton, cte.fuente_tamaño_boton, cte.fuente_diseño_boton),
                                  fg=cte.colorFront_guardar_boton, bg=cte.colorBack_guardar_boton, activebackground=cte.colorActive_guardar_boton)
        self.boton_guardar.place(x=cte.posicion_x_Guardar_boton, y=cte.posicion_y_Guardar_boton)

        self.boton_cancelar = tk.Button(self, text=cte.boton_Cancelar, command = self.deshabilitar_campos)
        self.boton_cancelar.config(width=cte.dimension_x_boton, font=(cte.fuente_tipo_boton, cte.fuente_tamaño_boton, cte.fuente_diseño_boton),
                                   fg=cte.colorFront_cancelar_boton, bg=cte.colorBack_cancelar_boton, activebackground=cte.colorActive_cancelar_boton)
        self.boton_cancelar.place(x=cte.posicion_x_Cancelar_boton, y=cte.posicion_y_Cancelar_boton)

        self.boton_actualizar = tk.Button(self, text=cte.boton_Actualizar, command = self.actualizar)
        self.boton_actualizar.config(width=cte.dimension_x_boton, font=(cte.fuente_tipo_boton, cte.fuente_tamaño_boton, cte.fuente_diseño_boton),
                                     fg=cte.colorFront_actualizar_boton, bg=cte.colorBack_actualizar_boton)
        self.boton_actualizar.place(x=cte.posicion_x_Actualizar_boton, y=cte.posicion_y_Actualizar_boton)

        self.boton_eliminar = tk.Button(self, text=cte.boton_Eliminar, command = self.eliminar_fila)
        self.boton_eliminar.config(width=cte.dimension_x_boton, font=(cte.fuente_tipo_boton, cte.fuente_tamaño_boton, cte.fuente_diseño_boton),
                                   fg=cte.colorFront_eliminar_boton, bg=cte.colorBack_eliminar_boton)
        self.boton_eliminar.place(x=cte.posicion_x_Eliminar_boton, y=cte.posicion_y_Eliminar_boton)

    def obtener_param(self):
        x = obtener_parametros()
        return x

    def obtener_categoria(self):
        x = obtener_categoria()
        return x

    def tabla_info(self):

        parametros = obtener_parametros()

        #Se indica el id de las columnas_trastornos que se ingresaran
        self.tabla = ttk.Treeview(self, columns=parametros)
        self.tabla.place(x=cte.posicion_x_tabla,y=cte.posicion_y_tabla,width=cte.dimension_x_tabla)

        #Se indica el nombre de las columnas_trastornos que se ingresaran respecto al id introducido
        self.tabla.heading('#0', text='ID')
        for i in range(len(parametros)):
            self.tabla.heading(parametros[i], text=parametros[i])

        #Añadir a la lista el contenido de BD
        for j in obtener_contenido():
            conte = []
            for t in range(1, len(obtener_parametros())+1):
                conte.insert(3,j[t])
            self.tabla.insert('', 1, text=j[0], values=(conte))

        self.scroll_v = ttk.Scrollbar(self,
                                    orient=tk.VERTICAL, command=self.tabla.yview)
        self.scroll_v.place(in_=self.tabla, relx=1, relheight=1, anchor='ne')
        self.tabla.configure(yscrollcommand=self.scroll_v.set)

        self.scroll_h = ttk.Scrollbar(self,
                                    orient=tk.HORIZONTAL, command=self.tabla.xview)
        self.scroll_h.place(in_=self.tabla, relx=0, rely=1, relwidth=1)
        self.tabla.configure(xscrollcommand=self.scroll_h.set)

    # Acciones
    def guardar_parametro(self):

        if self.mi_intro_parametro.get() != "":
            try:
                insertar_col(self.mi_intro_parametro.get())
            except sqlite3.OperationalError:
                mensaje('Introducir parámetros',
                        'Parámetro incorrecto o repetido',
                        2)
            else:
                mensaje('Introducir parámetros',
                        'Parámetro introducido',
                        0)
            finally:
                self.deshabilitar_campos()

        self.actualizar()

    def guardar_categoria(self):
        if self.mi_intro_categoria.get() != "":
            try:
                insertar_col_categoria(self.mi_intro_categoria.get())
            except sqlite3.OperationalError:
                mensaje('Introducir parámetros',
                        'Parámetro incorrecto o repetido',
                        2)
            else:
                mensaje('Introducir categoria',
                        'Categoria introducido',
                        0)
            finally:
                self.deshabilitar_campos()

        self.actualizar()

    def guardar_tipotrastornos(self):

        user, version, date = obtener_infoversion()
        flag = 0

        if self.mi_intro_transtorno.get() != "":
            try:
                for i in obtener_tipos_trastornos():
                    if self.mi_intro_transtorno.get() == i:
                        flag = 1
                if flag != 1:
                    guardar_tipotrastornos(version, self.mi_intro_categoria_comb.get(), self.mi_intro_transtorno.get())
                    mensaje('Introducir trastornos',
                            'Trastornos introducido',
                            0)
                else:
                    mensaje('Introducir trastornos',
                            'Trastornos repetido',
                            2)
            except sqlite3.OperationalError:
                mensaje('Introducir trastornos',
                        'Trastorno incorrecto o repetido',
                        2)
            finally:
                self.deshabilitar_campos()

        self.actualizar()

    def eliminar_parametro(self):
        eliminar_col(self.mi_eliminar_parametro.get())
        self.actualizar()

    def eliminar_trastornos(self):
        eliminar_tipotrastornos(self.mi_eliminar_transtorno.get())
        self.actualizar()

    def eliminar_fila(self):

        self.id_trastornos = self.tabla.item(self.tabla.selection())['text']
        eliminar_fila(self.id_trastornos)
        self.actualizar()

    def guardar(self):
        #Introducir parámetros
        if self.mi_intro_parametro.get() != "":
            self.guardar_parametro()
        #Eliminar parámetros
        if self.mi_eliminar_parametro.get() != "":
            self.eliminar_parametro()
        #Introducir categoria
        if self.mi_intro_categoria.get() != "":
            self.guardar_categoria()
        #Introducir transtorno
        if self.mi_intro_transtorno.get() != "":
            self.guardar_tipotrastornos()
        #Eliminar transtorno
        if self.mi_eliminar_transtorno.get() != "":
            self.eliminar_trastornos()

        self.actualizar()

    def actualizar(self):
        self.tabla.destroy()
        self.parametros()
        self.tabla_info()

    def exportar_plantilla(self):

        exim.exportar(False,obtener_parametros(),obtener_contenido(),obtener_tipos_trastornos())

    def exportar(self):

        exim.exportar(True,obtener_parametros(),obtener_contenido(),obtener_tipos_trastornos())

    def importar(self):

        exim.importar(nombre_tabla_trastornos)

    def version_inf(self):

        abrir_ventana_version()

    # Habilitar/Deshabilitar
    def habilitar_intro_parametro(self):
        self.entry_intro_parametro.config(state='normal')
        self.entry_eliminar_parametro.config(state='disable')
        self.entry_intro_categoria.config(state='disable')
        self.entry_intro_categoria_comb.config(state='disable')
        self.entry_intro_transtorno.config(state='disable')
        self.entry_eliminar_transtorno.config(state='disable')

    def habilitar_eliminar_parametro(self):
        self.entry_intro_parametro.config(state='disable')
        self.entry_eliminar_parametro.config(state='normal')
        self.entry_intro_categoria.config(state='disable')
        self.entry_intro_categoria_comb.config(state='disable')
        self.entry_intro_transtorno.config(state='disable')
        self.entry_eliminar_transtorno.config(state='disable')

    def habilitar_intro_categoria(self):
        self.entry_intro_parametro.config(state='disable')
        self.entry_eliminar_parametro.config(state='disable')
        self.entry_intro_categoria.config(state='normal')
        self.entry_intro_categoria_comb.config(state='disable')
        self.entry_intro_transtorno.config(state='disable')
        self.entry_eliminar_transtorno.config(state='disable')

    def habilitar_intro_transtorno(self):
        self.entry_intro_parametro.config(state='disable')
        self.entry_eliminar_parametro.config(state='disable')
        self.entry_intro_categoria.config(state='disable')
        self.entry_intro_categoria_comb.config(state='normal')
        self.entry_intro_transtorno.config(state='normal')
        self.entry_eliminar_transtorno.config(state='disable')

    def habilitar_eliminar_transtorno(self):
        self.entry_intro_parametro.config(state='disable')
        self.entry_eliminar_parametro.config(state='disable')
        self.entry_intro_categoria.config(state='disable')
        self.entry_intro_categoria_comb.config(state='disable')
        self.entry_intro_transtorno.config(state='disable')
        self.entry_eliminar_transtorno.config(state='normal')

    def deshabilitar_campos(self):
        self.entry_intro_parametro.config(state='disable')
        self.entry_eliminar_parametro.config(state='disable')
        self.entry_intro_categoria.config(state='disable')
        self.entry_intro_categoria_comb.config(state='disable')
        self.entry_intro_transtorno.config(state='disable')
        self.entry_eliminar_transtorno.config(state='disable')

        self.mi_intro_parametro.set('')
        self.mi_intro_transtorno.set('')
        self.mi_eliminar_transtorno.set('')
        self.mi_intro_categoria.set('')
        self.mi_intro_categoria_comb.set('')
        self.entry_eliminar_parametro.set(" ")

def barra_menu(app):
    barra_menu =  tk.Menu(app)
    app.config(menu = barra_menu)

    # Definir secciones
    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    menu_configuracion =  tk.Menu(barra_menu, tearoff = 0)
    menu_ayuda =  tk.Menu(barra_menu, tearoff = 0)


    # -- Seccion: Inicio
    barra_menu.add_cascade(label='Inicio', menu = menu_inicio)

    menu_inicio.add_command(label='Crear Base de datos', command= lambda: crear_tabla(columnas_trastornos))
    menu_inicio.add_command(label='Eliminar Base de datos',command= lambda: borrar_tabla())
    menu_inicio.add_separator()
    menu_inicio.add_command(label='Crear BD para categorias', command= lambda: crear_tabla_categoria(columnas_categoria))
    menu_inicio.add_command(label='Eliminar BD para categorias',command= lambda: borrar_tabla_categoria())
    menu_inicio.add_separator()
    menu_inicio.add_command(label='Crear BD para tipos de trastornos', command= lambda: crear_tabla_sec(columnas_tipotrastornos))
    menu_inicio.add_command(label='Eliminar BD para tipos de trastornos',command= lambda: borrar_tabla_sec())
    menu_inicio.add_separator()
    menu_inicio.add_command(label='Salir', command=app.destroy)

    # -- Seccion: Configuracion
    barra_menu.add_cascade(label='Configuración', menu = menu_configuracion)

    menu_configuracion.add_command(label='Importar datos', command= lambda: Frame.importar(self=app))
    menu_configuracion.add_command(label='Exportar report', command= lambda: Frame.exportar(self=app))
    menu_configuracion.add_separator()
    menu_configuracion.add_command(label='Exportar plantilla', command=lambda: Frame.exportar_plantilla(self=app))

    # -- Seccion: Ayuda
    barra_menu.add_cascade(label='Ayuda', menu = menu_ayuda)

    menu_ayuda.add_command(label='Version', command=lambda: abrir_ventana_version(obtener_infoversion()))
    menu_ayuda.add_command(label='Historial de la app', command=lambda: abrir_ventana_historialapp(obtener_version_tipos_trastornos()))
