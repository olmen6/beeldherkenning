# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 12:44:26 2025

@author: olmen
"""
import cv2
vidcap = cv2.VideoCapture('IMG_3747.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("01_frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1