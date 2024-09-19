import cv2
import numpy as np

def single_scale_retinex(image, sigma):
    """
    Apply Single-Scale Retinex (SSR) to enhance the image.
    
    :param image: Input image (in BGR format)
    :param sigma: Standard deviation for Gaussian filter
    :return: Enhanced image
    """
    image_float = np.float32(image) + 1.0  # Avoid log(0)
    log_image = np.log(image_float)
    
    kernel_size = int(6 * sigma + 1)
    kernel_size = kernel_size + 1 if kernel_size % 2 == 0 else kernel_size
    gaussian_blur = cv2.GaussianBlur(np.float32(image), (kernel_size, kernel_size), sigma)
    gaussian_blur_float = np.float32(gaussian_blur) + 1.0  # Avoid log(0)
    
    log_blur = np.log(gaussian_blur_float)
    retinex = log_image - log_blur
    retinex_normalized = cv2.normalize(retinex, None, 0, 255, cv2.NORM_MINMAX)
    
    retinex_image = np.uint8(retinex_normalized)
    
    return retinex_image

def gamma_correction(image, gamma):
    """
    Apply gamma correction to an image.
    
    :param image: Input image (in grayscale format)
    :param gamma: Gamma value for correction
    :return: Gamma-corrected image
    """
    image_float = np.float32(image) / 255.0
    gamma_corrected = np.power(image_float, gamma)
    gamma_corrected_image = np.uint8(gamma_corrected * 255.0)
    
    return gamma_corrected_image

def histogram_equalization(image):
    """
    Apply histogram equalization to a grayscale image.
    
    :param image: Input image (in grayscale format)
    :return: Equalized image
    """
    return cv2.equalizeHist(image)

def process_image(image_path, sigma, gamma):
    """
    Read an image, apply Single-Scale Retinex, gamma correction, and histogram equalization, and save the result.
    
    :param image_path: Path to the input image
    :param sigma: Standard deviation for Gaussian filter in SSR
    :param gamma: Gamma value for gamma correction
    """
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError("Image not found or unable to read.")
    
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Apply Single-Scale Retinex
    retinex_image = single_scale_retinex(image_rgb, sigma)
    
    # Apply gamma correction to the Retinex output
    gamma_corrected_image = gamma_correction(retinex_image, gamma)
    
    # Convert the gamma-corrected image to grayscale for histogram equalization
    gamma_corrected_gray = cv2.cvtColor(gamma_corrected_image, cv2.COLOR_RGB2GRAY)
    
    # Apply histogram equalization
    equalized1_image = histogram_equalization(gamma_corrected_gray)
    
    # Convert back to BGR (if needed)
    equalized1_image_bgr = cv2.cvtColor(equalized1_image, cv2.COLOR_GRAY2BGR)
    
    # Save the result
    cv2.imwrite('enhanced_image.jpg', equalized1_image_bgr)

    print("Image processing complete. Saved as 'enhanced1_image.jpg'.")

# Parameters
image_path = r"C:\Users\NNR DREANSCAPE\OneDrive\Desktop\meghanath\SIH\data\psr.jpg"
sigma = 30.0  # Standard deviation for Gaussian filter in SSR
gamma = 1.2   # Gamma value for correction

# Process the image
process_image(image_path, sigma, gamma)
