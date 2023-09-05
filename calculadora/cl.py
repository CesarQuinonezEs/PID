import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import numpy as np

img1 = cv2.imread(
    '/home/cesar/Desktop/PDI/PID/calculadora/imgs/Baboon.tiff', 1)
img2 = cv2.imread(
    '/home/cesar/Desktop/PDI/PID/calculadora/imgs/Splash.tiff', 1)
img1 = cv2.resize(img1, (200, 200))
img2 = cv2.resize(img2, (200, 200))


def invColor(img):
    auxIm = 255 - img
    return auxIm


def invGray(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    auxIm = 255 - img
    return auxIm


def umbral(img, umb):
    img2 = img
    indx = img <= umb
    img2[indx] = 0
    indx2 = img > umb
    img2[indx2] = 255
    return img2


def umbralinv(img, umb):
    imagen_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imagen_umbral_inverso = 255 - (imagen_gris > umb) * 255
    return imagen_umbral_inverso


def umBin(img, umbral_min, umbral_max):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imagen_binarizada = np.zeros_like(img)
    imagen_binarizada[(img >= umbral_min) & (img <= umbral_max)] = 255
    return imagen_binarizada


def umBinInv(img, umbral_min, umbral_max):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imagen_binarizada = np.zeros_like(img)
    imagen_binarizada[(img < umbral_min) & (img > umbral_max)] = 255
    return imagen_binarizada


def opExt(img, valor_minimo, valor_maximo):
    imagen_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    min_valor_original = np.min(imagen_gris)
    max_valor_original = np.max(imagen_gris)
    imagen_extendida = np.interp(
        imagen_gris, (min_valor_original, max_valor_original), (valor_minimo, valor_maximo))
    imagen_extendida = imagen_extendida.astype(np.uint8)
    return imagen_extendida


def opRedLvlGray(img, niveles_de_gris_reducidos):
    imagen_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rangos_de_gris = np.linspace(0, 255, niveles_de_gris_reducidos + 1)
    imagen_reducida = np.digitize(imagen_gris, rangos_de_gris)
    imagen_reducida = (255.0 / niveles_de_gris_reducidos) * imagen_reducida
    imagen_reducida = imagen_reducida.astype(np.uint8)
    return imagen_reducida


def andLogi(img1, img2):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    resultado_and = np.logical_and(img1, img2).astype(np.uint8) * 255
    return resultado_and


def orLogi(img1, img2):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    resultado = np.logical_or(img1, img2).astype(np.uint8) * 255
    return resultado


def notLogic(img1, img2):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    resultado = np.logical_not(img1, img2).astype(np.uint8) * 255
    return resultado


def xorLogi(img1, img2):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    resultado = np.logical_xor(img1, img2).astype(np.uint8) * 255
    return resultado
# Aritmetica basica con dos imagenes


def sum(img1, img2):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    resultado = img1 + img2
    return resultado


def res(img1, img2):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    resultado = img1 - img2
    return resultado


def mul(img1, img2):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    resultado = img1 * img2
    return resultado


def div(img1, img2):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    divisor = np.where(img2 == 0, 1, img2)
    resultado = img1 / divisor
    return resultado


def absRes(img1, img2):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    resultado = np.abs(img1 - img2)
    return resultado

# Aritmetica basica con escalar


def sumEs(img1, num):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    resultado = img1 + num
    return resultado


def resEs(img1, num):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    resultado = img1 - num
    return resultado


def mulEs(img1, num):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    resultado = img1 * num
    return resultado


def divEs(img1, num):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    if num > 0:
        resultado = img1 / num
    return resultado

def pow(img, num):
    res = np.power(img, num)
    res  = res.astype(np.uint8)
    return res