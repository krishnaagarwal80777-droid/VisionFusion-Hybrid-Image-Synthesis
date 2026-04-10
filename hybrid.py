import numpy as np
from filters import low_pass,high_pass

def create_hybrid(img1, img2):

    img1 = img1.astype(np.float32)
    img2 = img2.astype(np.float32)

    low_img = low_pass(img1, 41, 10)   # strong blur
    high_img = high_pass(img2, 15, 3)  # sharper high freq

    # Proper blending
    hybrid =   low_img +  high_img
    # Normalize at END only
    hybrid = np.clip(hybrid, 0, 255)

    return hybrid.astype(np.uint8)