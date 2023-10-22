import tkinter as tk
from tkinter import ttk

ruta_archivo = "./version/version_app.txt"

# Obtenemos los datos del documento de version del responsable del registro, la versión y la fecha del mismo
def obtener_infoversion():

    user_list = []
    version_list = []
    date_list = []

    with open(ruta_archivo, mode="r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            linea = linea.split(":")
            if linea[0] == "usuario":
                linea = linea[1]
                linea = linea.replace("\n", "")
                linea = linea.replace(" ", "", 1)
                user_ = linea
                user_list.append(user_)

            if linea[0] == "version":
                linea = linea[1]
                linea = linea.replace("\n", "")
                linea = linea.replace(" ", "", 1)
                version_ = linea
                version_list.append(version_)
                print(version_)

            if linea[0] == "date":
                linea = linea[1]
                linea = linea.replace("\n", "")
                linea = linea.replace(" ", "", 1)
                date_ =  linea
                date_list.append(date_)

    return user_list,version_list,date_list

# Función de apoyo para añadir en arrays las lineas leidas en el documento de version
def recorrer_listas(lista):
    lista_añadir = []
    cont = 0
    if lista != "":
        lista = lista.split(",",-1)
        for elemento in lista:
            cont = cont + 1
            lista_añadir.append(elemento)

    return lista_añadir, cont



# Funciones de las ventanas de version
def abrir_ventana_version(obtener_infoversion):

    user, version, date = obtener_infoversion

    # Crear una ventana secundaria.
    ventana_version = tk.Toplevel()
    ventana_version.title("Version")
    ventana_version.config(width=800, height=500)

    _version = tk.Text(ventana_version, background="white", width=40, height=10)
    _version.config(state='normal', font=('Arial', 10))
    _version.grid(row=0, column=0, padx=10, pady=10, columnspan=1)
    for i in range(len(user)):
        info = ("Usuario: " + user[i] + "\n" +
                "Version: " + version[i] + "\n" +
                "Fecha: " + date[i] + "\n")
        _version.insert(tk.INSERT, info)
    _version.configure(state="disabled")
    _version.pack()

    ventana_version.focus()
    ventana_version.mainloop()

def abrir_ventana_historialapp(obtener_version_tipos_trastornos):

    list_tt_aux = []

    list_tt = obtener_version_tipos_trastornos

    # Crear una ventana secundaria.
    ventana_historialapp = tk.Toplevel()
    ventana_historialapp.title("Historial APP")
    ventana_historialapp.config(width=800, height=500)

    _historial = tk.Text(ventana_historialapp, background="white", width=40, height=10)
    _historial.config(state='normal', font=('Arial', 10))
    _historial.grid(row=0, column=0, padx=10, pady=10, columnspan=1)

    for i in range(len(list_tt)):
        if list_tt[i][1] not in list_tt_aux:
            list_tt_aux.append(list_tt[i][1])
            print(list_tt[i][1])
    list_tt_aux.sort()

    for j in range(len(list_tt_aux)):
        cont = 0
        info = ("Versión: " + list_tt_aux[j] + "\n" + "-" * 50 + "\n")
        _historial.insert(tk.INSERT, info)
        for i in range(len(list_tt)):
            if list_tt[i][1] == list_tt_aux[j]:
                info = (str(cont+1) + " - " + list_tt[i][2] + "\n")
                _historial.insert(tk.INSERT, info)
                cont = cont + 1
        info = ("\n\n")
        _historial.insert(tk.INSERT, info)

    _historial.configure(state="disabled")
    _historial.pack()

    ventana_historialapp.focus()
    ventana_historialapp.mainloop()
