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
                                obtener_version_tipos_trastornos, nombre_tabla_trastornos, nombre_tabla_tipotrastornos

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
        self.mi_intro_parametro = tk.StringVar()
        self.entry_intro_parametro = tk.Entry(self, textvariable = self.mi_intro_parametro)
        self.entry_intro_parametro.config(width=30, state='disable', font=('Arial', 12))
        self.entry_intro_parametro.place(x=250, y=15, height=20)

        self.mi_eliminar_parametro = tk.StringVar()
        columnas_par = []
        for x in range(1, len(self.obtener_param())):
            param = self.obtener_param()[x]
            columnas_par.insert(x, param)
        self.columnas_par = columnas_par
        self.entry_eliminar_parametro = ttk.Combobox(self, state="readonly",
                                                     width=43, height=50, values = self.columnas_par,
                                                     textvariable=self.mi_eliminar_parametro)
        self.entry_eliminar_parametro.place(x=250, y=55)
        self.entry_eliminar_parametro.config(state='disable')

        self.mi_intro_transtorno = tk.StringVar()
        self.entry_intro_transtorno = tk.Entry(self, textvariable = self.mi_intro_transtorno)
        self.entry_intro_transtorno.config(width=30, state='disable', font=('Arial', 12))
        self.entry_intro_transtorno.place(x=780, y=15)


        self.mi_eliminar_transtorno = tk.StringVar()
        self.entry_eliminar_transtorno = ttk.Combobox(self, state="readonly",
                                                     width=43, height=50, values = obtener_tipos_trastornos(),
                                                     textvariable=self.mi_eliminar_transtorno)
        self.entry_eliminar_transtorno.place(x=780, y=55)
        self.entry_eliminar_transtorno.config(state='disable')

        # Botones
        self.boton_intro_parametro = tk.Button(self, text='Insertar parámetro', command = self.habilitar_intro_parametro)
        self.boton_intro_parametro.config(width=15, font=('Arial', 10, 'bold'), fg='blue', bg='white', activebackground='blue')
        self.boton_intro_parametro.grid(row = 0, column = 0)
        self.boton_intro_parametro.place(x=70, y=10)

        self.boton_eliminar_parametro = tk.Button(self, text='Eliminar parámetro', command = self.habilitar_eliminar_parametro)
        self.boton_eliminar_parametro.config(width=15, font=('Arial', 10, 'bold'), fg='red', bg='white', activebackground='red')
        self.boton_eliminar_parametro.place(x=70, y=50)

        self.boton_intro_transtorno = tk.Button(self, text='Insertar transtorno', command = self.habilitar_intro_transtorno)
        self.boton_intro_transtorno.config(width=15, font=('Arial', 10, 'bold'), fg='blue', bg='white', activebackground='blue')
        self.boton_intro_transtorno.place(x=600, y=10)

        self.boton_eliminar_transtornos = tk.Button(self, text='Eliminar transtorno', command = self.habilitar_eliminar_transtorno)
        self.boton_eliminar_transtornos.config(width=15, font=('Arial', 10, 'bold'), fg='red', bg='white', activebackground='red')
        self.boton_eliminar_transtornos.place(x=600, y=50)

        self.boton_guardar = tk.Button(self, text='Guardar', command = self.guardar)
        self.boton_guardar.config(width=15, font=('Arial', 10, 'bold'), fg='green', bg='white', activebackground='green')
        self.boton_guardar.place(x=70, y=100)

        self.boton_cancelar = tk.Button(self, text='Cancelar', command = self.deshabilitar_campos)
        self.boton_cancelar.config(width=15, font=('Arial', 10, 'bold'), fg='red', bg='white', activebackground='red')
        self.boton_cancelar.place(x=250, y=100)

        self.boton_actualizar = tk.Button(self, text='Actualizar', command = self.actualizar)
        self.boton_actualizar.config(width=15, font=('Arial', 10, 'bold'), fg='black', bg='white')
        self.boton_actualizar.place(x=925, y=100)

        self.boton_eliminar = tk.Button(self, text='Eliminar', command = self.eliminar_fila)
        self.boton_eliminar.config(width=15, font=('Arial', 10, 'bold'), fg='red', bg='white')
        self.boton_eliminar.place(x=70, y=400)

    def obtener_param(self):
        x = obtener_parametros()
        return x

    def tabla_info(self):

        parametros = obtener_parametros()

        #Se indica el id de las columnas_trastornos que se ingresaran
        self.tabla = ttk.Treeview(self, columns=parametros)
        self.tabla.place(x=70,y=150,width=1015)

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

    def guardar_tipotrastornos(self):

        user, version, date = obtener_infoversion()
        flag = 0

        if self.mi_intro_transtorno.get() != "":
            try:
                for i in obtener_tipos_trastornos():
                    if self.mi_intro_transtorno.get() == i:
                        flag = 1
                if flag != 1:
                    guardar_tipotrastornos(version,self.mi_intro_transtorno.get())
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
        self.entry_intro_transtorno.config(state='disable')
        self.entry_eliminar_transtorno.config(state='disable')

    def habilitar_eliminar_parametro(self):
        self.entry_intro_parametro.config(state='disable')
        self.entry_eliminar_parametro.config(state='normal')
        self.entry_intro_transtorno.config(state='disable')
        self.entry_eliminar_transtorno.config(state='disable')

    def habilitar_intro_transtorno(self):
        self.entry_intro_parametro.config(state='disable')
        self.entry_eliminar_parametro.config(state='disable')
        self.entry_intro_transtorno.config(state='normal')
        self.entry_eliminar_transtorno.config(state='disable')

    def habilitar_eliminar_transtorno(self):
        self.entry_intro_parametro.config(state='disable')
        self.entry_eliminar_parametro.config(state='disable')
        self.entry_intro_transtorno.config(state='disable')
        self.entry_eliminar_transtorno.config(state='normal')

    def deshabilitar_campos(self):
        self.entry_intro_parametro.config(state='disable')
        self.entry_eliminar_parametro.config(state='disable')
        self.entry_intro_transtorno.config(state='disable')
        self.entry_eliminar_transtorno.config(state='disable')

        self.mi_intro_parametro.set('')
        self.mi_intro_transtorno.set('')
        self.mi_eliminar_transtorno.set('')
        self.entry_eliminar_parametro.set(" ")

def barra_menu(app):
    barra_menu =  tk.Menu(app)
    app.config(menu = barra_menu, width = 300, height = 300)

    # Definir secciones
    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    menu_configuracion =  tk.Menu(barra_menu, tearoff = 0)
    menu_ayuda =  tk.Menu(barra_menu, tearoff = 0)


    # -- Seccion: Inicio
    barra_menu.add_cascade(label='Inicio', menu = menu_inicio)

    menu_inicio.add_command(label='Crear Base de datos', command= lambda: crear_tabla(columnas_trastornos))
    menu_inicio.add_command(label='Eliminar Base de datos',command= lambda: borrar_tabla())
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
