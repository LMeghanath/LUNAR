import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, UpSampling2D
from tensorflow.keras.optimizers import Adam

# Gamma correction function
def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

# Define a simple CNN model
def create_model():
    model = Sequential()
    # Encoder
    model.add(Conv2D(64, (3, 3), activation='relu', padding='same', input_shape=(256, 256, 1)))
    model.add(MaxPooling2D((2, 2), padding='same'))
    # Bottleneck
    model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
    # Decoder
    model.add(UpSampling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
    model.add(Conv2D(1, (3, 3), activation='sigmoid', padding='same'))
    model.compile(optimizer=Adam(), loss='mean_squared_error')
    return model

# Load and preprocess the image
def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (256, 256))
    image = image.astype('float32') / 255.0
    image = np.expand_dims(image, axis=-1)
    image = np.expand_dims(image, axis=0)
    return image

# Main function to process and display all images
def process_and_display_images(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply various image processing techniques
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    equalized_image = cv2.equalizeHist(image)
    denoised_image = cv2.fastNlMeansDenoising(image, None, 30, 7, 21)
    bilateral_filtered_image = cv2.bilateralFilter(image, 9, 75, 75)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_image = clahe.apply(image)
    gamma_corrected_image = adjust_gamma(image, gamma=2.0)

    # Load and preprocess the image for CNN
    input_image = preprocess_image(image_path)

    # Create the model
    model = create_model()

    # For demonstration, predict using the model
    output_image = model.predict(input_image)

    # Display all processed images and CNN enhanced image
    plt.figure(figsize=(200, 200))  # Increased figure size for better visibility
    titles = [
        'Original Image', 'Gaussian Blurred Image', 'Histogram Equalized Image',
        'Denoised Image (Non-Local Means)', 'Bilateral Filtered Image', 'CLAHE Enhanced Image',
        'Gamma Corrected Image', 'CNN Enhanced Image'
    ]
    images = [
        image, blurred_image, equalized_image, denoised_image, bilateral_filtered_image,
        clahe_image, gamma_corrected_image, output_image[0, :, :, 0]
    ]
    
    for i in range(len(images)):
        plt.subplot(3, 3, i + 1)
        plt.title(titles[i])
        plt.imshow(images[i], cmap='gray')
        plt.axis('off')
    
    plt.subplots_adjust(wspace=0.3, hspace=0.3)  # Adjust spacing between images
    plt.show()

# Run the combined image processing and display
image_path = r"C:\Users\NNR DREANSCAPE\OneDrive\Desktop\meghanath\SIH\data\psr.jpg"
process_and_display_images(image_path)
