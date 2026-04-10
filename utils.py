import numpy as np
import matplotlib.pyplot as plt

def compute_fft(image):
    image=image.astype(np.float32)

    f=np.fft.fft2(image)

    fshift=np.fft.fftshift(f)

    magnitude=20*np.log(np.abs(fshift)+1)

    return magnitude

def frequency_filter(image, radius=30, high_pass=False):
    
    image = image.astype(np.float32)
    
    # FFT
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    
    rows, cols = image.shape
    crow, ccol = rows//2 , cols//2
    
    # Create mask
    mask = np.zeros((rows, cols), np.uint8)
    
    if high_pass:
        mask[:] = 1
        mask[crow-radius:crow+radius, ccol-radius:ccol+radius] = 0
    else:
        mask[crow-radius:crow+radius, ccol-radius:ccol+radius] = 1
    
    # Apply mask
    fshift = fshift * mask
    
    # Inverse FFT
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    
    img_back = np.abs(img_back)
    
    return img_back