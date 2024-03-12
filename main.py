from tkinter import *
from tkinter.ttk import Notebook
TEAL="#76ABAE"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#TODO: CONFIGURACION INICIAL DE LA VENTANA
window=Tk()
window.config(padx=5, pady=5, bg=TEAL)

#titulo para nuestra ventana
window.title('Password Manager') 


#TODO:QUIERO QUE MI APP TENGA 2 TABS POR ESO USARE EL WIDGET NOTEBOOK

notebook=Notebook(window)

#pongo el widget Notebook dentro de mi ventana "window"
notebook.pack(padx = 5, pady = 5, expand = True)

#frame de mi primera tab, creo el frame en mi "Notebook"
frame1=Frame(notebook,   padx=20, pady=20)
#Empaqueto 'frame1' para que se expanda y llene todo el espacio disponible
frame1.pack(fill= BOTH, expand=True)

#  Creo un segundo Frame llamado 'frame2' en el notebook
frame2=Frame(notebook)
# Empaquetar 'frame2' para que se expanda y llene todo el espacio disponible
frame2.pack(fill= BOTH, expand=True)

# El método 'add' es específico de la clase Notebook en el módulo ttk de Tkinter. Se utiliza para añadir un marco como una nueva pestaña en el 
# notebook. El argumento text proporciona la etiqueta que se mostrará para esa pestaña en la interfaz de usuario.
notebook.add(frame1, text = "Window 1")
# Añadir 'frame2' al notebook con la etiqueta "Window 2"
notebook.add(frame2, text = "Window 2")


#TODO: #CREAMOS AREA RECTANGULAR  EN NUESTRO 'FRAME1' CONOCIDA COMO 'CANVAS' PARA PONER NUESTRA FOTO ALLI 
canvas=Canvas(frame1, width=200, height=200)
canvas.grid(row=0, column=1)

#cargando imagen
filename=PhotoImage(file="logo.png")

#creamos la imagen en nuestra ventana, definimos la posicion 'x' y 'y' 100 respectivamente
imagen=canvas.create_image(100, 100, image=filename)


#TODO: CREANDO DEMAS ELEMTOS DE NUESTRA APP "LABELS WIDGET, ENTRY WIDGET" 
#labels "website, email, password"
website_label=Label(frame1, text='Website', pady=5, font=('helvetica', 12))
website_label.grid(row=1, column=0)

Email_label=Label(frame1, text='Email/Username', pady=5, font=('helvetica', 12))
Email_label.grid(row=2, column=0)

password_label=Label(frame1, text='Password', pady=5, font=('helvetica', 12))
password_label.grid(row=3, column=0)

#entry widgets para cada label
website_entry=Entry(frame1, width=35, relief=SOLID)
website_entry.grid(row=1, column=1, columnspan=2)

email_entry=Entry(frame1, width=35, relief=SOLID)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry=Entry(frame1, width=21, relief=SOLID)
password_entry.grid(row=3, column=1)

#Boton generate password
generate_password_button=Button(frame1, text='Generate Password', relief=GROOVE, bg=TEAL)
generate_password_button.grid(row=3, column=2)

window.mainloop()