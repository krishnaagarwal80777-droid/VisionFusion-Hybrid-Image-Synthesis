# Hybrid Image Generator  
### Image Processing and Digital Signal Processing Implementation

---

## 1. Introduction

This project implements the concept of **Hybrid Images**, a technique in image processing where two different images are combined in such a way that:

- One image is perceived when viewed from a distance  
- Another image becomes visible when viewed from close range  

This effect is achieved by manipulating the **frequency components** of images and leveraging the characteristics of the **human visual system**, which responds differently to low and high spatial frequencies.

---

## 2. Fundamental Concept

Any image can be interpreted as a 2D signal composed of different frequency components:

- **Low-frequency components** represent smooth variations such as overall shapes, illumination, and large structures  
- **High-frequency components** represent sharp changes such as edges, fine textures, and details  

The hybrid image is constructed by combining:

- Low-frequency content from one image  
- High-frequency content from another image  

Mathematically:

Hybrid Image = LowPass(Image₁) + HighPass(Image₂)

---

## 3. Spatial Domain Implementation

The first approach implemented in this project is based on **spatial domain filtering**, where operations are performed directly on pixel values.

---

### 3.1 Low-Pass Filtering (Gaussian Blur)

Low-frequency components are extracted using a **Gaussian filter**.

A Gaussian filter smooths an image by averaging pixel values with their neighbors, weighted by a Gaussian distribution.

Implementation:

cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

Effect:
- Removes high-frequency details (edges and noise)
- Preserves overall structure

---

### 3.2 High-Pass Filtering

High-frequency components are extracted by subtracting the low-pass version from the original image:

High = Image − LowPass(Image)

Interpretation:
- The subtraction removes smooth components
- Remaining signal contains edges and fine details

Important detail:
The high-pass result contains both positive and negative values. These represent intensity transitions and must be preserved for correct reconstruction.

---

### 3.3 Data Type Consideration

Before performing operations, images are converted to floating-point format:

image = image.astype(np.float32)

This is necessary to:
- Prevent overflow and underflow
- Maintain precision during subtraction and addition

---

### 3.4 Image Fusion

The hybrid image is formed by combining the filtered components:

hybrid = low_img + high_img

To ensure valid pixel values:

hybrid = np.clip(hybrid, 0, 255)  
hybrid = hybrid.astype(np.uint8)

This completes the spatial domain implementation.

---

## 4. Frequency Domain Implementation (FFT)

The second approach uses **frequency domain processing**, which provides a more direct and precise way to manipulate image frequencies.

---

### 4.1 Fourier Transform

The **Fast Fourier Transform (FFT)** converts an image from spatial domain to frequency domain.

f = np.fft.fft2(image)  
fshift = np.fft.fftshift(f)

- fft2 computes the 2D Fourier transform  
- fftshift moves the zero-frequency component to the center  

---

### 4.2 Frequency Representation

In the frequency domain:

- The center represents low frequencies  
- The outer regions represent high frequencies  

This allows direct control over which frequency components are retained or removed.

---

### 4.3 Magnitude Spectrum

To visualize frequency content:

magnitude = 20 * log(|F|)

This shows:
- Bright center → strong low-frequency content  
- Distributed patterns → high-frequency details  

---

### 4.4 Frequency Masking

Instead of using convolution (like Gaussian blur), we create masks to isolate frequency regions.

Low-pass mask:
- Keeps only central frequencies  

High-pass mask:
- Removes central frequencies  

---

### 4.5 Applying Mask

fshift_filtered = fshift * mask

---

### 4.6 Inverse Transform

f_ishift = np.fft.ifftshift(fshift_filtered)  
img_back = np.fft.ifft2(f_ishift)  
img_back = np.abs(img_back)

---

### 4.7 Hybrid Image using FFT

Steps:
1. Extract low-frequency component of first image  
2. Extract high-frequency component of second image  
3. Combine both:

hybrid_fft = low_freq + alpha * high_freq

---

## 5. Comparison of Approaches

Spatial domain uses convolution and is simpler, while frequency domain allows precise control over frequency components.

---

## 6. Role of Perceptual Scaling

High-frequency components are often weak, so scaling is applied:

hybrid = low + alpha * high

---

## 7. Key Observations

- Low-frequency images dominate perception at a distance  
- High-frequency components become visible at close range  
- Proper alignment is essential  

---

## 8. Learning Outcomes

- Images as signals  
- Spatial vs frequency filtering  
- FFT usage  
- Importance of scaling and alignment  

---

## 9. Applications

- Computational photography  
- Visual illusions  
- Signal processing education  
