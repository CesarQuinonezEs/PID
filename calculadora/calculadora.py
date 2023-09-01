import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import imageio

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
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        self.image1_display.config(image=photo)
        self.image1_display.image = photo

    def display_image2(self, file_path):
        image = imageio.imread(file_path)
        image = Image.fromarray(image)
        photo = ImageTk.PhotoImage(image)
        self.image2_display.config(image=photo)
        self.image2_display.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageLoaderApp(root)
    root.mainloop()
