from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Notebook
TEAL="#76ABAE"
BEIGE="#F9E8C9"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
#TODO: ALMACENAR LA INFORMACION INGRESADA POR EL USUARIO EN UN ARCHIVO TXT.file
def save_data():
    # Obteniendo los datos ingresados por el usuario
    website_data=website_var.get()
    email_data=email_var.get()
    password_data=password_var.get()
    
    #abrimos el archivo donde vamos aguardar nuestras passwords, si el archivo no esta, se crea automaticamente
    with open("data.txt", "a") as file:
        # Creando una cadena de texto con los datos para guardar
        data_to_Save=(website_data + " | " + email_data+ " | " + password_data)
        file.write(data_to_Save + "\n")

    # Borrando los datos ingresados en los campos de entrada
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    
    #mensaje indicando al usuario que la informacion fue guardada con exito
    messagebox.showinfo("showinfo", "Information added correctly" )
    
    
    
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
frame1=Frame(notebook,   padx=50, pady=50,  bg="white")
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
#highlightthickness remove the light grey border around my Canvas widget?
canvas=Canvas(frame1, width=200, height=200,  bg="white",  highlightthickness=0)
canvas.grid(row=0, column=1)

#cargando imagen
filename=PhotoImage(file="logo.png")

#creamos la imagen en nuestra ventana, definimos la posicion 'x' y 'y' 100 respectivamente
imagen=canvas.create_image(100, 100, image=filename)


#TODO: CREANDO DEMAS ELEMTOS DE NUESTRA APP "LABELS WIDGET, ENTRY WIDGET" 
#labels "website, email, password"
website_label=Label(frame1, text='Website:',  bg="white", pady=5, font=('helvetica', 12))
website_label.grid(row=1, column=0)

Email_label=Label(frame1, text='Email/Username:',  bg="white", pady=5, font=('helvetica', 12))
Email_label.grid(row=2, column=0)

password_label=Label(frame1, text='Password:',  bg="white", pady=5,  font=('helvetica', 12))
password_label.grid(row=3, column=0)


#VARIABLES DONDE SE ALMACENARA LOS DATOS INGRESADOS POR EL USUARIO
#declaro variables string 'StringVar class' para guardar el nombre del website, email y password
website_var=StringVar()
email_var=StringVar()
password_var=StringVar()

#entry widgets para cada label
website_entry=Entry(frame1, textvariable=website_var, width=50, relief=SOLID)
website_entry.grid(row=1, column=1, columnspan=2)
#establesiendo el foco en nuestro website_entry, es decir al arrancar la app, el mause aparece inmediatamente ahi
website_entry.focus()

email_entry=Entry(frame1, textvariable=email_var, width=50, relief=SOLID)
email_entry.grid(row=2, column=1, columnspan=2)
#insertamos el sgt msj en el widget 'email_entry' para que se muestre apenas corre el programa
email_entry.insert(0,'@gmail.com')

password_entry=Entry(frame1, textvariable=password_var, width=32, relief=SOLID)
password_entry.grid(row=3, column=1)


#Boton generate password y add
generate_password_button=Button(frame1, text='Generate Password', relief=GROOVE, bg=BEIGE)
generate_password_button.grid(row=3, column=2)

add_button=Button(frame1, text='Add', width=43, relief=GROOVE, bg="white", command=save_data)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()