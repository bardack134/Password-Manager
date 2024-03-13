from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Notebook
from PasswordGenerator import *
#modulo utilizado para copiar automaticamente el la password generada
import pyperclip

TEAL="#76ABAE"
BEIGE="#F9E8C9"

# ------------------------------CALL PASSWORD-----------------------------------------
#TODO: LLAMAR O BUSCAR UNA PASSWORD ESPECIFICA DENTRO DE NUESTRO ARCHIVO .TXT file
def search_password():
    #llamamos al archivo que tiene guardada nuestras password
    with open('data.txt', 'r') as file:
        #retornamos todas las lineas en el archivo como una lista
        file_as_a_list = file.readlines()
        
        # Obtenemos la entrada del usuario y la convertimos a minúsculas
        data_to_search = website_entry.get().lower()
        
        # Inicializamos una variable para verificar si encontramos el elemento
        element_found=False
        
        for i in file_as_a_list:
            # Si los datos a buscar están en la línea actual
            if data_to_search   in i:
                
                # Limpiamos la línea removiendo el caracter "|"
                i_clean=i.replace("|","")
                
                
                # Convertimos la línea limpia en una lista
                i_as_a_list=i_clean.split()
                
                
                # Extraemos el nombre del sitio web, el correo electrónico y la contraseña
                website_name=i_as_a_list[0]
                email_name=i_as_a_list[1]
                password_name=i_as_a_list[2]
                
                
                # Creamos la información a mostrar
                information=f'Website:{website_name}\n Email:{email_name}\n Password:{password_name}'
                
                
                # Mostramos la información en un cuadro de mensaje
                messagebox.showinfo("showinfo", information) 

                
                # Marcamos que encontramos el elemento
                element_found=True
        
        # Si no encontramos el elemento, mostramos un mensaje indicando que no se encontró
        if element_found==False:    
            messagebox.showinfo("showinfo", 'Element not found') 
                  
            
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#TODO: CREAMOS FUNCION QUE CREARA NUESTRAS PASSWORDS AL OPRIMIR EL BOTON "generate password"
#funcion que llama a la funcion password_create del archivo PasswordGenerator.py
def call_password_create():
    
    #insertaremos nuestra password en el password entry
    password_entry.insert(0, password_create())
    
    
    #funcion para copiar automaticamente la password generada
    pyperclip.copy(password_create())
    
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
#TODO: ALMACENAR LA INFORMACION INGRESADA POR EL USUARIO EN UN ARCHIVO TXT.file
def save_data():
    # Obteniendo los datos ingresados por el usuario
    website_data=website_entry.get().lower()
    email_data=email_entry.get()
    password_data=password_entry.get()
        
        
    #puedepasar que el usuario no ha ingresado informacion, miramos si el usuario ingreso o no informacion
    if len(website_data)==0 or len(email_data)==0 or len(password_data)==0:
        messagebox.showerror(title='opps', message="Please do not leave any fields empty")
    
    
    #es decir el usuario si ingreso informacion
    else:
        #preguntamos al usuario  si la informacion agregada es correcta
        yes_or_not=messagebox.askyesno(title=website_data, message=f"Email:{email_data} \nPassword:{password_data} \n\nIs it ok to save?" )
        
        
        if yes_or_not == True:
            
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
window.title('Password Manager') #titulo para nuestra ventana


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
#entry widgets para cada label
website_entry=Entry(frame1,  width=32, relief=SOLID)
website_entry.grid(row=1, column=1)
#establesiendo el foco en nuestro website_entry, es decir al arrancar la app, el mause aparece inmediatamente ahi
website_entry.focus()


email_entry=Entry(frame1,  width=50, relief=SOLID)
email_entry.grid(row=2, column=1, columnspan=2)
#insertamos el sgt msj en el widget 'email_entry' para que se muestre apenas corre el programa
email_entry.insert(0,'@gmail.com')


password_entry=Entry(frame1,  width=32, relief=SOLID)
password_entry.grid(row=3, column=1)


#BOTON GENERATE PASSWORD, ADD, SEARCH
generate_password_button=Button(frame1, text='Generate Password', relief=GROOVE, bg=BEIGE, command=call_password_create)
generate_password_button.grid(row=3, column=2)


add_button=Button(frame1, text='Add', width=43, relief=GROOVE, bg="white", command=save_data)
add_button.grid(row=4, column=1, columnspan=2)


search_button=Button(frame1, text='Search', width=13, relief=GROOVE, bg=BEIGE, command=search_password)
search_button.grid(row=1, column=2 )


#TODO: CREAMOS NUESTRA SEGUNDA VENTANA PARA QUE EL USUARIO BUSQUE SUS PASSWORDS

window.mainloop()