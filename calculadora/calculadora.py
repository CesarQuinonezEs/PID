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
        
        self.opciones_funciones = ["1- Invertido en color"
                                   , "2- invertido en escala de grises"
                                   , "3- Umbral","4- Umbral invertido"
                                   ,"5 - umbral binario"
                                   ,"7 - umbral binario invertido"
                                   ,"8 - Operador exponente"
                                   ,"9 - Operador niveles de gris"
                                   ,"10 - AND"
                                   ,"11 - OR"
                                   ,"12 - XOR"
                                   ,"13 - NOT"
                                   ,"14 - suma (dos imgenes)"
                                   ,"15 - Resta (dos imgenes)"
                                   ,"16 - Multiplicacion (dos imgenes)"
                                   ,"17 - Division (dos imgenes)"
                                   ,"18 - suma (Escalar)"
                                   ,"19 - Resta (Escalar)"
                                   ,"20 - Multiplicacion (Escalar)"
                                   ,"21 - Division (Escalar)"
                                   ,"22 - Valor absolluto"
                                   ,"23- Potencia"]
        self.opcion_seleccionada = tk.StringVar(root)
        self.opcion_seleccionada.set(self.opciones_funciones[0]) 
        self.opcion_menu = tk.OptionMenu(root, self.opcion_seleccionada, *self.opciones_funciones)
        self.opcion_menu.pack(pady=10)
        
        self.min_leabel = tk.Label(root,text="Minimo")
        self.min_leabel.pack()
        
        self.min = tk.IntVar()
        self.min_entry = tk.Entry(root, textvariable=self.min)
        self.min_entry.pack()
        
        self.min_leabel = tk.Label(root,text="Maximo")
        self.min_leabel.pack()
        
        self.max = tk.IntVar()
        self.max_entry = tk.Entry(root, textvariable=self.max)
        self.max_entry.pack()
        
        self.num_leabel = tk.Label(root,text="Escalar o umbral, o cualquier numero")
        self.num_leabel.pack()
        
        self.num = tk.IntVar()
        self.num_entry = tk.Entry(root, textvariable=self.num)
        self.num_entry.pack()
        
        self.resultado_label = tk.Label(root, text="")
        self.resultado_label.pack()
        self.boton_ejecutar = tk.Button(root, text="Ejecutar Función", command=self.ejecutar_funcion)
        self.boton_ejecutar.pack()
        self.image1 = np.zeros((200,200,3))
        self.image2 =   np.zeros((200,200,3))
        
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
        img = np.zeros((200,200,3))
        opcion = self.opcion_seleccionada.get()
        num = self.num.get()
        min = self.min.get()
        max = self.max.get()
        
        if self.image1.max() > 0:
            self.image1 = cv2.resize(self.image1, (200,200))
            print(img.shape)
        if self.image2.max() > 0: 
            self.image2 = cv2.resize(self.image2, (200,200))
         
        if opcion == "1- Invertido en color":
                img = cl.invColor(self.image1)
        elif opcion == "2- invertido en escala de grises":
                img = cl.invGray(self.image1)
        elif opcion == "3- Umbral":
                img = cl.umbral(self.image1, num)
        elif opcion == "4- Umbral invertido":
                img = cl.umbralinv(self.image2, num)
        elif opcion == "5 - umbral binario":
                img = cl.umBin(self.image1, min,max)  
        elif opcion == "7 - umbral binario invertido":
            img = cl.umBinInv(self.image1, min, max)  
        elif opcion == "8 - Operador exponente":
            img = cl.opExt(self.image1, min, max)  
        elif opcion == "9 - Operador niveles de gris":
            img = cl.umBin(self.image1, min, max)  
        elif opcion == "10 - AND":
            img = cl.andLogi(self.image1, self.image2)  
        elif opcion == "11 - OR":
            img = cl.orLogi(self.image1, self.image2)  
        elif opcion == "12 - XOR":
            img = cl.xorLogi(self.image1, self.image2)  
        elif opcion == "13 - NOT":
            img = cl.notLogic(self.image1, self.image2)  
        elif opcion == "14 - suma (dos imgenes)":
            img = cl.sum(self.image1, self.image2)  
        elif opcion == "15 - Resta (dos imgenes)":
            img = cl.res(self.image1, self.image2)  
        elif opcion == "16 - Multiplicacion (dos imgenes)":
            img = cl.mul(self.image1, self.image2)  
        elif opcion == "17 - Division (dos imgenes)":
            img = cl.div(self.image1, self.image2)  
        elif opcion == "18 - suma (Escalar)":
            print(self.num)
            img = cl.sumEs(self.image1, num) 
        elif opcion == "19 - Resta (Escalar)":
            img = cl.resEs(self.image1, num)
        elif opcion == "20 - Multiplicacion (Escalar)":
            img = cl.mulEs(self.image1, num)
        elif opcion == "21 - Division (Escalar)":
            img = cl.divEs(self.image1, num)
        elif opcion == "22 - Valor absolluto":
            img = cl.absRes(self.image1, self.image2)
        elif opcion == "23- Potencia":
            img = cl.pow(self.image1, num)    
        cv2.imshow("Resultado", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageLoaderApp(root)
    root.mainloop()
