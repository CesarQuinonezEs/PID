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
entry_fields = []
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
    
    kernel = np.array(matrix)
    kernel = kernel/np.sum(kernel)
    print(kernel)
    fl.suav(img,kernel)
    
def get_matrix_values2():
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
    
    kernel = np.array(matrix)
    kernel = kernel/np.sum(kernel)
    print(kernel)
    fl.con(img,kernel)



def open_new_window(flg):
    new_window = tk.Toplevel(root)
    new_window.title("Matriz para el filtrado")
    
    for i in range(3):
        row_entries = []
        for j in range(3):
            entry = tk.Entry(new_window, width=10)
            entry.grid(row = i, column= j)
            row_entries.append(entry)
        entry_fields.append(row_entries)
# Botón para enviar la matriz
    if flg == 1:
        submit_button = tk.Button(new_window, text="Enviar Matriz", command=get_matrix_values)
    else:
        submit_button = tk.Button(new_window, text="Enviar Matriz", command=get_matrix_values2)
    submit_button.grid(row=3, columnspan=3)
    
def seleccionar_opcion():
    opcion_seleccionada = opcion.get()
    
    if opcion_seleccionada == "Suavizado":
        open_new_window(1)
    elif opcion_seleccionada == "BORDER_CONSTANT":
       fl.bc(img)
    elif opcion_seleccionada == "BORDER_REPLICATE":
        fl.brp(img)
    elif opcion_seleccionada == "BORDER_REFLECT":
        fl.brf(img)
    elif opcion_seleccionada == "BORDER_WRAP":
        fl.bw(img)
    elif opcion_seleccionada == "Filtro promedio":
        messagebox.showinfo("Opción seleccionada", "Has seleccionado Filtro promedio")
    elif opcion_seleccionada == "Filtro gaussiano":
        fl.fgausiano(img)
    elif opcion_seleccionada == "Media":
        fl.media(img)
    elif opcion_seleccionada == "Gradiente en X":
        fl.gradX(img)
    elif opcion_seleccionada == "Gradiente en Y":
        fl.gradY(img)
    elif opcion_seleccionada == "Noisy":
        fl.noisy(img)
    elif opcion_seleccionada == "Laplaciano":
        fl.lap(img)
    elif opcion_seleccionada == "Convoluciones":
        open_new_window(2)
# Crear la ventana principal
root = tk.Tk()
root.title("Selección de Opción")

# Variable para almacenar la opción seleccionada
opcion = tk.StringVar()
opcion.set("Suavizado")

# Crear lista de opciones
opciones = ["Suavizado", "BORDER_CONSTANT", "BORDER_REPLICATE", "BORDER_REFLECT", "BORDER_WRAP",
            "Filtro promedio", "Filtro gaussiano", "Media", "Gradiente en X", "Gradiente en Y", "Laplaciano", "Noisy", "Convoluciones"]

# Crear lista desplegable
opcion_lista = tk.OptionMenu(root, opcion, *opciones)
opcion_lista.pack()

# Botón para activar la opción seleccionada
boton_activar = tk.Button(root, text="Activar Opción", command=seleccionar_opcion)
boton_activar.pack()

root.mainloop()
