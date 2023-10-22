from tkinter import messagebox

def mensaje(titulo,mensaje,tipo):

    # Info
    if tipo == 0:
        messagebox.showinfo(titulo,mensaje)
    # Warning
    if tipo == 1:
        messagebox.showwarning(titulo, mensaje)
    # Error
    if tipo == 2:
        messagebox.showerror(titulo, mensaje)
