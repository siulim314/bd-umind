import tkinter as tk
from client.gui_app import Frame, barra_menu

app_title= 'Umind'
app_size = [1700,500]


def main():
    #Init Tkinter
    app = tk.Tk()
    app.title(app_title)
    app.resizable(True, True)
    app.iconbitmap('C:\\Users\\luism\\Desktop\\Umind\\app\\app_BaseDatos\\img\\u_alphabet_letter_letters_icon_209052.ico')
    #app.geometry(app_size)

    #Configurate frames
    Frame(app_size[0], app_size[1], app = app)

    barra_menu(app)

    app.mainloop()

if __name__ == '__main__':
    main()
