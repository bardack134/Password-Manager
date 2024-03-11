from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#TODO: CONFIGURACION INICIAL DE LA VENTANA
window=Tk()
window.config(padx=20, pady=20)

#titulo para nuestra ventana
window.title('Password Manager') 

#creamos area rectangular conocida como canvas para poner nuestra foto alli
canvas=Canvas(window, width=200, height=200)
canvas.pack()

#cargando imagen
filename=PhotoImage(file="logo.png")

#creamos la imagen en nuestra ventana, definimos la posicion 'x' y 'y' 100 respectivamente
imagen=canvas.create_image(100, 100, image=filename)


window.mainloop()