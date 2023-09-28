import numpy as np
import cv2
import matplotlib.pylab as plt
from urllib.request import urlopen
from random import randint
from skimage.util import random_noise
from skimage import img_as_float
# la siguiente URL apunta a una imagen:
url = "https://placekitten.com/500/500"

# Extraer el contenido de la URL:
url_response = urlopen(url)

# Convertir a matriz numpyarray:
img_array = np.asarray(bytearray(url_response.read()), dtype="uint8")

# decodifica la imagen
img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)


def con(img, kernel):
    # tamano de la imagen
    (img_row, img_col) = img.shape[:2]

    # centro del filtro
    centro = kernel.shape[0] // 2
    # para almacenar el resultado
    res = np.zeros((img_row, img_col), np.uint8)
    # implementa proceso de convolución/correlación
    for ii in range(centro, img_row-centro):
        for jj in range(centro, img_col-centro):
            res[ii, jj] = np.uint8(
                np.sum(img[ii-centro:ii+centro+1, jj-centro:jj+centro+1]*kernel))
    plt.figure(figsize=[20, 20])
    plt.imshow(res, cmap='gray')
    plt.title('imagen suavisada')
    plt.show()


def suav(img, kernel):
    dst = cv2.filter2D(img, -1, kernel)
    plt.figure(figsize=[20, 20])
    plt.imshow(dst, cmap='gray')
    plt.title('imagen suavisada')
    plt.show()


def dif(img):
    kernel_size = 15
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size * kernel_size)
    ddepth = -1
    dst = cv2.filter2D(img, ddepth, kernel)
    plt.figure(figsize=[20, 20])
    plt.imshow(img - dst, cmap='gray', vmin=0, vmax=255)
    plt.title('Diferencia')
    plt.show()


def bc(img):
    top = int(.5 * img.shape[0])  # shape[0] = rows
    bottom = top
    left = int(.5 * img.shape[1])  # shape[1] = cols
    right = left
    value = [randint(0, 255), randint(0, 255), randint(0, 255)]
    dst = cv2.copyMakeBorder(img, top, bottom, left, right, 0, None, value)
    plt.figure(figsize=[30, 30])
    plt.imshow(dst, cmap='gray', vmin=0, vmax=255)
    plt.title('BORDER_CONSTANT')
    plt.show()


def brp(img):
    top = int(.5 * img.shape[0])  # shape[0] = rows
    bottom = top
    left = int(.5 * img.shape[1])  # shape[1] = cols
    right = left
    value = [randint(0, 255), randint(0, 255), randint(0, 255)]
    dst = cv2.copyMakeBorder(img, top, bottom, left, right, 1, None, value)
    plt.figure(figsize=[30, 30])
    plt.imshow(dst, cmap='gray', vmin=0, vmax=255)
    plt.title('BORDER_REPLICATE')
    plt.show()


def brf(img):
    top = int(.5 * img.shape[0])  # shape[0] = rows
    bottom = top
    left = int(.5 * img.shape[1])  # shape[1] = cols
    right = left
    value = [randint(0, 255), randint(0, 255), randint(0, 255)]
    dst = cv2.copyMakeBorder(img, top, bottom, left, right, 2, None, value)
    plt.figure(figsize=[30, 30])
    plt.imshow(dst, cmap='gray', vmin=0, vmax=255)
    plt.title('BORDER_REFLECT')
    plt.show()


def bw(img):
    top = int(.5 * img.shape[0])  # shape[0] = rows
    bottom = top
    left = int(.5 * img.shape[1])  # shape[1] = cols
    right = left
    value = [randint(0, 255), randint(0, 255), randint(0, 255)]
    dst = cv2.copyMakeBorder(img, top, bottom, left, right, 3, None, value)
    plt.figure(figsize=[30, 30])
    plt.imshow(dst, cmap='gray', vmin=0, vmax=255)
    plt.title('BORDER_WRAP')
    plt.show()


def fgausiano(img):
    kernel_size = 3
    sigma = .85
    kernelG = cv2.getGaussianKernel(kernel_size, sigma)
    kernelG = kernelG * kernelG.transpose(1, 0)
    blurG1 = cv2.filter2D(img, -1, kernelG)
    kernel_size = 15
    blurG2 = cv2.GaussianBlur(img, (kernel_size, kernel_size), 1)

    plt.figure(figsize=[30, 30])
    plt.imshow(blurG2, cmap='gray', vmin=0, vmax=255)
    plt.title('Filtro gausiano')
    plt.show()


def noisy(img):
    noisy = img_as_float(img)
    noisy = np.uint8(random_noise(noisy, 's&p', amount=0.5) * 255)
    plt.figure(figsize=[30, 30])
    plt.imshow(noisy, cmap='gray', vmin=0, vmax=255)
    plt.title('Filtro noisy')
    plt.show()


def media(img):
    noisy = img_as_float(img)
    noisy = np.uint8(random_noise(noisy, 's&p', amount=0.5) * 255)
    median = cv2.medianBlur(noisy, 5)
    plt.figure(figsize=[30, 30])
    plt.imshow(median, cmap='gray', vmin=0, vmax=255)
    plt.title('Filtro media')
    plt.show()


def gradX(img):
    scale = 1
    delta = 0
    ddepth = cv2.CV_16S
    grad_x = cv2.Sobel(img, ddepth, 1, 0, ksize=3, scale=scale,
                       delta=delta, borderType=cv2.BORDER_DEFAULT)
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    plt.figure(figsize=[30, 30])
    plt.imshow(grad_x, cmap='gray', vmin=grad_x.min(), vmax=grad_x.max())
    plt.title('Filtro gradiente en X')
    plt.show()


def gradY(img):
    scale = 1
    delta = 0
    ddepth = cv2.CV_16S
    grad_y = cv2.Sobel(img, ddepth, 0, 1, ksize=3, scale=scale,
                       delta=delta, borderType=cv2.BORDER_DEFAULT)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    plt.imshow(grad_y, cmap='gray', vmin=grad_y.min(), vmax=grad_y.max()),
    plt.title('Gradiente en Y')
    plt.show()


def lap(img):
    ddepth = cv2.CV_16S
    kernel_size = 3

    # Remove noise by blurring with a Gaussian filter
    src = cv2.GaussianBlur(img, (3, 3), 0)

    # Apply Laplace function
    dst = cv2.Laplacian(src, ddepth, ksize=kernel_size)
    # converting back to uint8
    abs_dst = cv2.convertScaleAbs(dst)
    plt.figure(figsize=[30, 30])
    plt.imshow(dst, cmap='gray', vmin=dst.min(), vmax=dst.max())
    plt.title('Filtro lapaciano')
    plt.show()
