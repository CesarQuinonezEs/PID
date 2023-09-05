import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import imageio
import cv2
import numpy as np
import cl
class ImageLoaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cargar y Mostrar Imágenes")

        self.image1_label = tk.Label(self.root, text="Imagen 1:")
        self.image1_label.pack()

        self.image1_path = tk.StringVar()
        self.image1_entry = tk.Entry(self.root, textvariable=self.image1_path)
        self.image1_entry.pack()

        self.image1_button = tk.Button(self.root, text="Cargar Imagen 1", command=self.load_image1)
        self.image1_button.pack()

        self.image2_label = tk.Label(self.root, text="Imagen 2:")
        self.image2_label.pack()

        self.image2_path = tk.StringVar()
        self.image2_entry = tk.Entry(self.root, textvariable=self.image2_path)
        self.image2_entry.pack()

        self.image2_button = tk.Button(self.root, text="Cargar Imagen 2", command=self.load_image2)
        self.image2_button.pack()
        
        self.image1_display = tk.Label(self.root)
        self.image1_display.pack()

        self.image2_display = tk.Label(self.root)
        self.image2_display.pack()
        
        self.opciones_funciones = ["Función 1", "Función 2", "Función 3"]
        self.opcion_seleccionada = tk.StringVar(root)
        self.opcion_seleccionada.set(self.opciones_funciones[0]) 
        self.opcion_menu = tk.OptionMenu(root, self.opcion_seleccionada, *self.opciones_funciones)
        self.opcion_menu.pack(pady=10)
        self.resultado_label = tk.Label(root, text="")
        self.resultado_label.pack()
        self.boton_ejecutar = tk.Button(root, text="Ejecutar Función", command=self.ejecutar_funcion)
        self.boton_ejecutar.pack()
        
        
        
    def load_image1(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.tiff *.tif")])
        if file_path:
            self.image1_path.set(file_path)
            self.display_image1(file_path)

    def load_image2(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.tiff *.tif")])
        if file_path:
            self.image2_path.set(file_path)
            self.display_image2(file_path)

    def display_image1(self, file_path):
        image = cv2.imread(file_path)
        image = cv2.resize(image,(200,200))
        self.image1 = image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(Image.fromarray(image))
        self.image1_display.config(image=photo)
        self.image1_display.image = photo

    def display_image2(self, file_path):
        image = cv2.imread(file_path)
        image = cv2.resize(image,(200,200))
        self.image2 = image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(Image.fromarray(image))
        self.image2_display.config(image=photo)
        self.image2_display.image = photo
        
    def ejecutar_funcion(self):
        opcion = self.opcion_seleccionada.get()
        img = self.image1  
        if opcion == "Función 1":
                img = cl.invColor(self.image1)
        elif opcion == "Función 2":
                img = cl.invGray(self.image1)
        elif opcion == "Función 3":
                img = cl.umbral(self.image1, 120) 
        cv2.imshow("Resultado", img)
        cv2.waitKey(0)
        cv2.destroyWindow(winname="Resultado")
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageLoaderApp(root)
    root.mainloop()
