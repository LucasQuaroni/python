from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()

# funciones
def crear():
    conexion=sqlite3.connect("usuarios")
    cursor=conexion.cursor()
    try:
        cursor.execute("CREATE TABLE datosUsuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(50), pass VARCHAR(50), apellido VARCHAR(50), direccion VARCHAR(50), comentarios VARCHAR(100))")
        messagebox.showinfo("BBDD", "BBDD creada con éxito")
    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")
    conexion.commit()
    conexion.close()
    
def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    if valor=="yes":
        root.destroy()
        
def limpiarCampos():
    cuadroID.delete(0, END)
    cuadroNombre.delete(0, END)
    cuadroPass.delete(0, END)
    cuadroApellido.delete(0, END)
    cuadroDireccion.delete(0, END)
    cuadroComentarios.delete(1.0, END)
    
def crearUsuario():
    conexion=sqlite3.connect("usuarios")
    cursor=conexion.cursor()
    cursor.execute("INSERT INTO datosUsuarios VALUES (NULL, '" + cuadroNombre.get() + "', '" + cuadroPass.get() + "','" + cuadroApellido.get() + "', '" + cuadroDireccion.get() + "', '" + cuadroComentarios.get("1.0", END) + "')")
    conexion.commit()
    
    messagebox.showinfo("BBDD", "Registro insertado con éxito")
    conexion.close()
    
def leerUsuario():
    conexion=sqlite3.connect("usuarios")
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM datosUsuarios WHERE id=" + cuadroID.get())
    elUsuario=cursor.fetchall()
    for usuario in elUsuario:
        cuadroNombre.insert(0, usuario[1])
        cuadroPass.insert(0, usuario[2])
        cuadroApellido.insert(0, usuario[3])
        cuadroDireccion.insert(0, usuario[4])
        cuadroComentarios.insert(1.0, usuario[5])
    conexion.commit()
    conexion.close()
    
def actualizarUsuario():
    conexion=sqlite3.connect("usuarios")
    cursor=conexion.cursor()
    cursor.execute("UPDATE datosUsuarios SET nombre='" + cuadroNombre.get() + "', pass='" + cuadroPass.get() + "', apellido='" + cuadroApellido.get() + "', direccion='" + cuadroDireccion.get() + "', comentarios='" + cuadroComentarios.get("1.0", END) + "' WHERE id=" + cuadroID.get())
    conexion.commit()
    conexion.close()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito")
    
def borrarUsuario():
    conexion=sqlite3.connect("usuarios")
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM datosUsuarios WHERE id=" + cuadroID.get())
    conexion.commit()
    conexion.close()
    messagebox.showinfo("BBDD", "Registro borrado con éxito")



# navbar
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=crear)
bbddMenu.add_command(label="Desconectar", command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crearUsuario)
crudMenu.add_command(label="Leer", command=leerUsuario)
crudMenu.add_command(label="Actualizar", command=actualizarUsuario)
crudMenu.add_command(label="Borrar", command=borrarUsuario)

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)


# inputs
miFrame=Frame(root)
miFrame.pack()

cuadroID=Entry(miFrame)
cuadroID.grid(row=0, column=1, padx=10, pady=10)
cuadroID.config(fg="blue", justify="center")

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="blue", justify="center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)
cuadroApellido.config(fg="blue", justify="center")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(fg="blue", justify="center")
cuadroPass.config(show="*")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)
cuadroDireccion.config(fg="red", justify="center")

cuadroComentarios=Text(miFrame, width=16, height=5)
cuadroComentarios.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=cuadroComentarios.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
cuadroComentarios.config(yscrollcommand=scrollVert.set)


# labels
idLabel=Label(miFrame, text="ID:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Contraseña:")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Dirección:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)
    

# botones
botonesFrame = Frame(root)
botonesFrame.pack(pady=10)

botonCrear = Button(botonesFrame, text="Crear", command=crearUsuario)
botonCrear.pack(side=LEFT, padx=10)

botonLeer = Button(botonesFrame, text="Leer", command=leerUsuario)
botonLeer.pack(side=LEFT, padx=10)

botonActualizar = Button(botonesFrame, text="Actualizar", command=actualizarUsuario)
botonActualizar.pack(side=LEFT, padx=10)

botonBorrar = Button(botonesFrame, text="Borrar", command=borrarUsuario)
botonBorrar.pack(side=LEFT, padx=10)

root.mainloop()