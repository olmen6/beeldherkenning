# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 17:50:26 2025

@author: olmen
"""

import cv2
import numpy as np
#import matplotlib.pyplot as plt
import os


def whitefilter(foto):
    mask = (image[:, :, 0] > 200) & (image[:, :, 1] > 200) & (image[:, :, 2] > 200)
    filtered = np.zeros_like(image)
    filtered[mask] = image[mask]
    cv2.imshow("whitefiler", filtered)
    
def canny_edge(foto):
    gray = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 1.0) 
    edges = cv2.Canny(blur, 50, 150)                 
    cv2.imwrite(foto, edges)
    cv2.imshow("canny edge", foto)

def contrast(foto):
    import cv2
    alpha = 1.5  # Contrast (1-3)
    beta = 20    # Brightness(0-100)
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    cv2.imshow('Original', foto)
    cv2.imshow('Contrast Adjusted', adjusted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
    
input_folder = r"C:\Users\olmen\OneDrive - Stichting Hogeschool Utrecht\schooljaar 2025-2026nhhlockin\beeldherkenning\testset"
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    print("%s"%filename)
    image = cv2.imread(file_path)
    #whitefilter(image)
    canny_edge(image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

    