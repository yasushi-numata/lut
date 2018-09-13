import cv2
import pandas as pd
import numpy as np
import os

lutRGBpath = "lut_rgb.csv"
df_lutrgb = pd.read_csv(lutRGBpath)
imgpath = "256img.bmp"

img = cv2.imread(imgpath)

# create img
# img = np.array(range(256))
# img = img.reshape((16,16,1))
# print(img)
# cv2.imwrite(imgpath, img)

# B
img[:, :, 0] = cv2.LUT(img[:, :, 0], np.array(df_lutrgb['B'], dtype=np.uint8))
# G
img[:, :, 1] = cv2.LUT(img[:, :, 1], np.array(df_lutrgb['G'], dtype=np.uint8))
# R
img[:, :, 2] = cv2.LUT(img[:, :, 2], np.array(df_lutrgb['R'], dtype=np.uint8))

cv2.imwrite("out.bmp", img)

