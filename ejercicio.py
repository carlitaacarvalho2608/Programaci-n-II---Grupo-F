import tkinter as tk
from tkinter import messagebox
#pacientes
def nuevoPaciente():
    ventanaRegistro=tk.Toplevel(ventanaPrincipal)
    ventanaRegistro.title("Registro de Paciente")
    ventanaRegistro.geometry("400x400")
    ventanaRegistro.configure(bg="#00FF0D")
    #nombre
    nombreLabel=tk.Label(ventanaRegistro, text="Nombre: ", bg="#00FF0D")
    nombreLabel.grid(row=0, column=0, padx=10, pady=5, sticky="w")#n=norte, s=sur, e=este, w=oeste, we, ns,
    entryNombre=tk.Entry(ventanaRegistro)
    entryNombre.grid(row=0, column=1, padx=10, pady=5, sticky="we")
    #Direccion
    direccionLabel=tk.Label(ventanaRegistro, text="Direccion: ", bg="#00FF0D")
    direccionLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w")#n=norte, s=sur, e=este, w=oeste, we, ns,
    entryDireccion=tk.Entry(ventanaRegistro)
    entryDireccion.grid(row=1, column=1, padx=10, pady=5, sticky="we")
    #Telefono
    TelefonoLabel=tk.Label(ventanaRegistro, text="Telefono: ", bg="#00FF0D")
    TelefonoLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w")#n=norte, s=sur, e=este, w=oeste, we, ns,
    entryTelefono=tk.Entry(ventanaRegistro)
    entryTelefono.grid(row=2, column=1, padx=10, pady=5, sticky="we")
    #sexo(radiobutton)
    sexoLabel=tk.Label(ventanaRegistro, text="Sexo:")
    sexoLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    sexo=tk.StringVar(value="Masculino")
    sexoLabel=tk.StringVar(value="Masculino")
    rbMasculino=tk.Radiobutton(ventanaRegistro, text="Masculino", variable=sexo,value="Masculino")
    rbMasculino.grid(row=3, column=1, sticky="w")
    rbFemenino=tk.Radiobutton(ventanaRegistro, text="Femenino", variable=sexo,value="Femenino")
    rbFemenino.grid(row=4, column=1, sticky="w")
    #enfermedades base(checkbutton)
    enfLabel=tk.Label(ventanaRegistro,text="Enfermedades base:")
    enfLabel.grid(row=5,column=0,padx=10,pady=5,sticky="w")
    diabetes=tk.BooleanVar()
    hipertension=tk.BooleanVar()
    asma=tk.BooleanVar()
    #enfermedades base(checkbutton)
    cbDiabetes=tk.Checkbutton(ventanaRegistro,text="Diabetes",variable=diabetes)
    cbDiabetes.grid(row=5,column=1,sticky="w")
    cbHipertension=tk.Checkbutton(ventanaRegistro,text="Hipertensión",variable=hipertension)
    cbHipertension.grid(row=6,column=1,sticky="w")
    cbAsma=tk.Checkbutton(ventanaRegistro,text="Asma",variable=asma)
    cbAsma.grid(row=7,column=1,sticky="w")    
    #Cadena para mostrar todos los datos del formulario
    def registrarDatos():
        enfermedades=[]
        if diabetes.get():
            enfermedades.append("Diabetes")
        if hipertension.get():
            enfermedades.append("Hipertensión")
        if asma.get():
            enfermedades.append("Asma") 
        if len(enfermedades)>0:
            enfermedadesTexto=','.join(enfermedades)
        else:
            enfermedadesTexto="Ninguna"
        info=(
        f"Nombre: {entryNombre.get()}\n"
        f"Direccion:{entryDireccion.get()}\n"
        f"Telefono: {entryTelefono.get()}\n"
        f"Sexo: {sexo.get()}\n"
        f"Enfermedades:{enfermedadesTexto}"
        )
        messagebox.showinfo("Datos Registrados", info)
        ventanaRegistro.destroy()
    btnRegistrar=tk.Button(ventanaRegistro, text="Datos Registrados", command=registrarDatos)
    btnRegistrar.grid(row=9, column=0, columnspan=2, pady=15)
def buscarPaciente():
    messagebox.showinfo("Buscar Paciente", "Busqueda de Pacientes")
def eliminarPaciente():
    messagebox.showinfo("Eiminar Paciente", "Eliminación de Pacientes")
#doctores
def nuevoDoctor():
    messagebox.showinfo("Nuevo Doctor", "Registrar Doctor")
def buscarDoctor():
    messagebox.showinfo("Buscar Doctor", "Busqueda de Doctores")
def eliminarDoctor():
    messagebox.showinfo("Eiminar Doctor", "Eliminación de Doctores")
ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Sistema de registro de pacientes")
ventanaPrincipal.geometry("800x600")
ventanaPrincipal.configure(bg="#442BD3")
#Barra de menú
barraMenu=tk.Menu(ventanaPrincipal)
ventanaPrincipal.configure(menu=barraMenu)
#Menu Pacientes
menuPacientes=tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Pacientes", menu=menuPacientes)
menuPacientes.add_command(label="Nuevo Paciente", command=nuevoPaciente)
menuPacientes.add_command(label="Eliminar Paciente", command=eliminarPaciente)
menuPacientes.add_command(label="Buscar Paciente", command=buscarPaciente)
menuPacientes.add_separator()
menuPacientes.add_command(label="salir", command=ventanaPrincipal.quit)
#Menu doctores
menuDoctores=tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Doctores", menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor", command=nuevoDoctor)
menuDoctores.add_command(label="Eliminar Doctor", command=eliminarDoctor)
menuDoctores.add_command(label="Buscar Doctor", command=buscarDoctor)
menuDoctores.add_separator()
menuDoctores.add_command(label="salir", command=ventanaPrincipal.quit)   
#Menu Ayuda
menuAyuda=tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
menuAyuda.add_command(label="Acerca de", command=lambda:messagebox.showinfo("Acerca de","Version 1.0 - Sistema Biomedicina"))
ventanaPrincipal.mainloop()
 
 
 
 
 