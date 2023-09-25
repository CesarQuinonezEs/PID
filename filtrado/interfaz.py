import numpy as np
import cv2
import matplotlib.pylab as plt
from urllib.request import urlopen
import tkinter as tk
from tkinter import messagebox
import filtradoEsp as fl
# Función para manejar la selección de la opción
url = "https://placekitten.com/500/500"

# Extraer el contenido de la URL:
url_response = urlopen (url)

# Convertir a matriz numpyarray:
img_array = np.asarray(bytearray(url_response.read()), dtype="uint8")

# decodifica la imagen
img = cv2.imdecode (img_array, cv2.IMREAD_GRAYSCALE)

def get_matrix_values():
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            try:
                value = float(entry_fields[i][j].get())
                row.append(value)
            except ValueError:
                return None  # Si no se ingresó un número válido, retorna None
        matrix.append(row)
    return matrix


def submit_matrix():
    matrix = get_matrix_values()
    if matrix:
        print("Matriz ingresada:")
        for row in matrix:
            print(row)
    else:
        print("Por favor, ingresa valores numéricos válidos en todos los campos.")


def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Matriz para el filtrado")
    
    label = tk.Label(new_window, text="Matriz 3X3")
    label.pack()
    entry_fields = []
    for i in range(3):
        row_entries = []
        for j in range(3):
            entry = tk.Entry(new_window, width=10)
            entry.grid(row = i, column= j)
            row_entries.append(entry)
        entry_fields.append(row_entries)
# Botón para enviar la matriz
    submit_button = tk.Button(new_window, text="Enviar Matriz", command=submit_matrix)
    submit_button.grid(row=3, columnspan=3)
    
def seleccionar_opcion():
    opcion_seleccionada = opcion.get()
    
    if opcion_seleccionada == "Suavizado":
        open_new_window()
    elif opcion_seleccionada == "BORDER_CONSTANT":
       fl.bc()
    elif opcion_seleccionada == "BORDER_REPLICATE":
        messagebox.showinfo("Opción seleccionada", "Has seleccionado BORDER_REPLICATE")
    elif opcion_seleccionada == "BORDER_REFLECT":
        messagebox.showinfo("Opción seleccionada", "Has seleccionado BORDER_REFLECT")
    elif opcion_seleccionada == "BORDER_WRAP":
        messagebox.showinfo("Opción seleccionada", "Has seleccionado BORDER_WRAP")
    elif opcion_seleccionada == "Filtro promedio":
        messagebox.showinfo("Opción seleccionada", "Has seleccionado Filtro promedio")
    elif opcion_seleccionada == "Filtro gaussiano":
        messagebox.showinfo("Opción seleccionada", "Has seleccionado Filtro gaussiano")
    elif opcion_seleccionada == "Media":
        messagebox.showinfo("Opción seleccionada", "Has seleccionado Media")
    elif opcion_seleccionada == "Gradiente en X":
        messagebox.showinfo("Opción seleccionada", "Has seleccionado Gradiente en X")
    elif opcion_seleccionada == "Gradiente en Y":
        messagebox.showinfo("Opción seleccionada", "Has seleccionado Gradiente en Y")
    elif opcion_seleccionada == "Laplaciano":
        messagebox.showinfo("Opción seleccionada", "Has seleccionado Laplaciano")

# Crear la ventana principal
root = tk.Tk()
root.title("Selección de Opción")

# Variable para almacenar la opción seleccionada
opcion = tk.StringVar()
opcion.set("Suavizado")

# Crear lista de opciones
opciones = ["Suavizado", "BORDER_CONSTANT", "BORDER_REPLICATE", "BORDER_REFLECT", "BORDER_WRAP",
            "Filtro promedio", "Filtro gaussiano", "Media", "Gradiente en X", "Gradiente en Y", "Laplaciano"]

# Crear lista desplegable
opcion_lista = tk.OptionMenu(root, opcion, *opciones)
opcion_lista.pack()

# Botón para activar la opción seleccionada
boton_activar = tk.Button(root, text="Activar Opción", command=seleccionar_opcion)
boton_activar.pack()

root.mainloop()
