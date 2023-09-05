import tkinter as tk

# Funciones que quieres ejecutar
def funcion1():
    resultado_label.config(text="Función 1 ejecutada")

def funcion2():
    resultado_label.config(text="Función 2 ejecutada")

def funcion3():
    resultado_label.config(text="Función 3 ejecutada")

# Crear una ventana de tkinter
root = tk.Tk()
root.title("Ejemplo de Opciones de Funciones")

# Crear una lista de opciones de funciones
opciones_funciones = ["Función 1", "Función 2", "Función 3"]
opcion_seleccionada = tk.StringVar(root)
opcion_seleccionada.set(opciones_funciones[0])  # Establecer la opción predeterminada

opcion_menu = tk.OptionMenu(root, opcion_seleccionada, *opciones_funciones)
opcion_menu.pack(pady=10)

# Label para mostrar el resultado
resultado_label = tk.Label(root, text="")
resultado_label.pack()

# Botón para ejecutar la función seleccionada
boton_ejecutar = tk.Button(root, text="Ejecutar Función", command=lambda: ejecutar_funcion(opcion_seleccionada.get()))
boton_ejecutar.pack()

# Función para ejecutar la función seleccionada
def ejecutar_funcion(opcion):
    if opcion == "Función 1":
        funcion1()
    elif opcion == "Función 2":
        funcion2()
    elif opcion == "Función 3":
        funcion3()

# Ejecutar la ventana de tkinter
root.mainloop()