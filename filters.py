import cv2
import numpy as np

# Low pass filter (Gaussian Blur)
def low_pass(img, kernel_size=21, sigma=5):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma)
def high_pass(img, kernel_size=21, sigma=5):
    low = low_pass(img, kernel_size, sigma)
    high = img - low
    return high   # NO normalization here