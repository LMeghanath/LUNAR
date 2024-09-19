# LUNAR-VISION
Enhancement of psr images.
Intially the demo1.py is program for individual application of image processing techniques for the given image i,e, here it is psr.jpg.
image processing general techniques like
     
      -Gaussian Blurr
      -Histogram Equalization
      -Denoising by Non-Local means
      -Bilateral filter
      -CLAHE Enhancement
      -Gamma correction

The output of this is output1.png
      
The python file ssrtogrtohe.py is a program for processing of image using the combination of the techniques:
                                      
      -SSR (Single Scale Retinex)
      -Gamma reduction
      -Histogram Equalization
      
The input file is same as above ,i.e, psr.jpg

The output(ssrtogrtohe).jpg file is the Output of the ssrtogrtohe.py 

As we can see the improvement of the enhancing of shadowed regions.

So we want to use combination CNN models for tranning a AI model.

 like 
      
      RetinexNet model for SSR. 
      Efficent-UNet model for gamma correction.
      and applying histogram equalization.
      
As the values of sigma in SSR and gamma in Gamma Reduction varies for different images.
So that it gives a better output.

Lets see about the techniques and models used in this project:

# SSR (Single Scale Retinex):
SSR aims to correct illumination and enhance color consistency in images, making them appear more natural and visually appealing.

## Mechanism:

It operates by decomposing an image into its illumination and reflectance components.

The process typically involves calculating the logarithm of the input image and applying a spatial filter (like a Gaussian filter) to estimate the illumination.

The final output is obtained by normalizing the reflectance component, often by scaling it to enhance contrast.

## Advantages:

### Improves Detail: 
SSR enhances the visibility of details in both bright and dark areas of an image.

### Color Consistency: 
It reduces color artifacts that can arise from uneven lighting.

### Applications: 
SSR is commonly used in fields like medical imaging, remote sensing, and photography where enhancing visibility and color accuracy is crucial.

## Limitations:

### Single Scale: 
As the name implies, SSR uses a single scale for the filtering process, which may not effectively handle images with varying illumination levels across different scales.

# Gamma Reduction:

Gamma Reduction is a technique used in image processing to adjust the brightness of an image by altering its gamma value, which affects the luminance levels.

## Applications:

### Low-Light Images: 
Useful for enhancing details in poorly lit images.

### Contrast Improvement: 
Can help in improving the overall contrast and visibility of features in images.

### Pre-processing for Other Techniques: 
Often used as a preprocessing step before applying other image enhancement techniques or machine learning models.

## Considerations:

### Over-Enhancement Risk: 
Over-applying gamma reduction can lead to loss of detail in bright regions or introduce artifacts.

### Subjective Quality: 
The effectiveness can be subjective, as it depends on the specific image content and viewer perception.
    
# Histogram Equalization:

Histogram Equalization is an image enhancement technique used to improve the contrast of an image. Here’s a brief overview:

## Benefits:

### Improved Contrast: 
Enhances the visibility of features in both bright and dark regions of an image.

### Dynamic Range Utilization: 
Makes full use of the available intensity range, improving overall image quality.

### Applications: 
Commonly used in various fields such as medical imaging, satellite imagery, and photography, particularly in situations where the original image has low contrast.


## Limitations:

### Noise Amplification: 
Histogram equalization can sometimes amplify noise in uniform areas of the image.

### Loss of Detail: 
In cases where the histogram is very peaky, the enhancement might lead to loss of details in certain regions.

### Color Images: 
Standard histogram equalization is typically applied to grayscale images; for color images, it can be more complex, requiring adjustments in each channel or converting to a different color space.

# Combination of SSR Gamma Reduction and Histogram Equalization:

Combining Single Scale Retinex (SSR), gamma correction, and histogram equalization can lead to significant improvements in image quality and perceived Signal-to-Noise Ratio (SNR). Here’s how these techniques work together:

# Combined Effects 

## Single Scale Retinex (SSR):

### Illumination Normalization: 
SSR helps to separate illumination from reflectance, improving the visibility of details in the image by reducing the effects of uneven lighting.

### Enhanced Contrast: 
By enhancing the reflectance, SSR can make features more distinct against the background.

## Gamma Correction:

### Brightness Adjustment: 
Applying gamma correction with a value less than 1 brightens darker areas, making details more visible.

### Contrast Improvement: 
This adjustment redistributes pixel values, which helps enhance the overall image contrast.

## Histogram Equalization:

### Dynamic Range Adjustment: 
Histogram equalization redistributes the intensity values across the entire range, improving the contrast and visibility of features in both light and dark regions.

### Noise Reduction: 
By stretching the histogram, it can reduce the impact of noise by enhancing the overall structure of the image.

## Benefits of the Combination

### Improved Visibility: 
The synergy of SSR, gamma correction, and histogram equalization can significantly enhance the visibility of details in both bright and dark areas, making the image more informative.

### Enhanced Perceived SNR: 
The combination helps reduce the visibility of noise, particularly in shadowed areas, improving the perceived SNR by making the signal more prominent against the noise.

### Better Detail Recovery: 
Utilizing all three methods together can recover details that may be lost due to poor lighting or noise, leading to a more visually appealing result.

## Considerations:

### Sequential Application: 
The order of applying these techniques can impact the results. A common approach is to first apply SSR, then gamma correction, and finally histogram equalization.

### Parameter Tuning: 
Each technique has parameters that may require tuning to achieve optimal results without introducing artifacts or losing important information.

### Computational Complexity: 
The combined approach can increase computational requirements, so efficiency may be a consideration depending on the application.

3 REtinexNet:
RetinexNet is a deep learning model designed to address the challenges of image enhancement, particularly in terms of improving visibility and color consistency in images that suffer from poor lighting or high dynamic range. The model is inspired by the Retinex theory, which emphasizes the importance of illumination and reflectance in visual perception.

## Key Features
### Illumination Correction:

RetinexNet aims to separate the illumination component from the reflectance component of an image. This separation helps in correcting lighting variations, leading to clearer and more visually appealing images.

### Deep Learning Architecture:

The network typically consists of multiple convolutional layers that learn to capture spatial and contextual features from the input images. The architecture is designed to learn the optimal way to enhance images based on training data.

### Multi-Scale Processing:

RetinexNet often incorporates multi-scale features, allowing it to process information at different resolutions. This capability helps in effectively enhancing details that might be missed at a single scale.

### End-to-End Learning:

The model is trained in an end-to-end manner, meaning that it learns to enhance images directly from the raw input to the desired output, without requiring manual tuning of parameters.

## Applications:

RetinexNet is particularly useful in applications such as:

### Medical Imaging: 
Enhancing the visibility of anatomical structures.
### Remote Sensing: 
Improving satellite images taken under varying lighting conditions.
### Low-Light Image Enhancement: 
Correcting images captured in poor lighting scenarios.

## Advantages
### Improved Visual Quality: 
It significantly enhances the visibility of details in images, making them more useful for analysis.
### Color Consistency: 
By correcting illumination variations, it ensures that the colors in the images are more consistent and true to life.
###Flexibility: 
Applicable across various domains where image quality is critical.

# Efficent-UNET:
Efficient U-Net is a variant of the traditional U-Net architecture that combines the strengths of both U-Net and EfficientNet. It is designed for image segmentation tasks while optimizing for efficiency, making it particularly suitable for applications with limited computational resources.

## Key Features
### Backbone Architecture:

Efficient U-Net uses EfficientNet as its backbone, which is known for its excellent performance and efficiency. EfficientNet employs a compound scaling method to balance network depth, width, and resolution, leading to improved accuracy with fewer parameters.

### U-Net Structure:

It retains the encoder-decoder structure of U-Net, which consists of downsampling (encoder) and upsampling (decoder) paths. This architecture allows the model to capture context and spatial information effectively.

### Skip Connections:

Like traditional U-Net, Efficient U-Net incorporates skip connections that link corresponding layers in the encoder and decoder. These connections help preserve spatial information, enhancing segmentation accuracy.

### Multi-Scale Feature Extraction:

The model leverages EfficientNet’s ability to capture multi-scale features, allowing it to perform well on images with varying resolutions and details.
Lightweight Design:

Efficient U-Net is optimized for speed and efficiency, making it suitable for real-time applications. Its design allows for fast inference without significantly compromising segmentation quality.

## Advantages
### Reduced Computational Load: 
Efficient U-Net requires fewer resources compared to standard U-Net, making it suitable for deployment on devices with limited processing power.
### High Accuracy: 
By utilizing the efficient backbone, the model maintains high accuracy while being computationally efficient.
### Scalability: 
It can be easily scaled up or down based on the requirements of the task and available resources.

# Combination of RetinexNet and Efficent-UNet:
Combining RetinexNet and Efficient U-Net can create a powerful framework for image enhancement and segmentation, especially for challenging tasks like analyzing Permanently Shadowed Regions (PSR). 

## Image Enhancement with RetinexNet:

### Process:
Input images are fed into RetinexNet, which performs illumination correction and detail enhancement.
The output is a more visually consistent and clear image, suitable for segmentation.

## Segmentation with Efficient U-Net:

## Purpose: 
Use Efficient U-Net to perform semantic segmentation on the enhanced images.

## Process:
The output from RetinexNet is then fed into the Efficient U-Net model.
Efficient U-Net, leveraging its lightweight architecture and efficient feature extraction, accurately segments the regions of interest in the enhanced image.

## Benefits of the Combination
### Improved Input Quality:

The enhanced images produced by RetinexNet allow Efficient U-Net to operate on higher-quality data, leading to better segmentation performance.
### Detail Preservation:

RetinexNet enhances the visibility of fine details that might be critical for accurate segmentation, especially in PSR images where features may be obscured by shadow.

## Efficiency:

Efficient U-Net is designed for quick inference, making the combination suitable for real-time applications where rapid processing is essential.

### Robustness to Variability:

The combination is effective in handling variability in lighting conditions typical of PSR images, ensuring that segmentation remains accurate even in challenging scenarios.
Implementation Steps

# Combination of processing Techniques:
The combination of Single Scale Retinex (SSR), gamma reduction, and histogram equalization, paired with CNN models like RetinexNet and Efficient U-Net, provides a comprehensive approach to enhancing images of Permanently Shadowed Regions (PSR) on celestial bodies.

## 1. Preprocessing Techniques
### Single Scale Retinex (SSR):

#### Purpose: 
Enhance illumination and normalize colors, vital for revealing details in low-light conditions common in PSR.
#### Process: 
SSR improves local contrast by reducing lighting variations, making features more visible in dark areas.

### Gamma Reduction:

#### Purpose: 
Adjust the brightness of the image to enhance visibility of shadowed regions.
#### Process: 
This technique increases the luminance of darker areas, helping to reveal critical features that might otherwise be lost.

### Histogram Equalization:

#### Purpose: 
Improve overall contrast across the image.
#### Process: 
This technique redistributes pixel intensity values, enhancing the visibility of features that are critical for analysis in shadowed regions.

## 2. CNN Models
### RetinexNet:

#### Role: 
Serves as the first deep learning model in the pipeline.
#### Function: 
After preprocessing, the enhanced image is fed into RetinexNet, which utilizes deep learning to refine illumination and extract important features. This model is focused on preserving natural color balance while addressing illumination inconsistencies.

### Efficient U-Net:

#### Role: 
Acts as the second model, focusing on segmentation and detail refinement.
#### Function: 
Efficient U-Net processes the feature maps produced by RetinexNet. Its architecture is optimized for efficiency, allowing for high-quality upsampling and refinement while maintaining critical details needed for accurate analysis of PSR.


## 3. Benefits for Analyzing PSR
### Enhanced Detail Recovery: 
The preprocessing steps help to improve the visibility of features critical for scientific analysis.
### Robust Feature Extraction: 
The combination of RetinexNet and Efficient U-Net ensures significant detail capture, facilitating accurate assessments of PSR.
### Computational Efficiency: 
Efficient U-Net is designed for optimized performance, making it suitable for processing large images typical of satellite data.


# Disadvantages
##Artifact Introduction:

Issue: Preprocessing techniques, particularly histogram equalization, can introduce artifacts or noise.
Impact: These artifacts can obscure important features in the image, leading to misinterpretations in scientific analyses.

## Computational Overhead:

Issue: The combination of multiple preprocessing steps and deep learning models increases computational requirements.
Impact: Longer processing times may hinder real-time applications, especially when dealing with large satellite images.
Parameter Sensitivity:

Issue: The effectiveness of preprocessing techniques depends on carefully chosen parameters (e.g., gamma values, histogram settings).
Impact: Suboptimal parameter choices can degrade image quality and reduce the effectiveness of subsequent analysis.

# Improvements:
## Adaptive Preprocessing Techniques:

Implement adaptive methods for SSR, gamma reduction, and histogram equalization that automatically adjust parameters based on the image's characteristics to minimize artifacts and optimize enhancements.

## Incorporate Multi-Scale Processing:

Utilize multi-scale Retinex techniques to capture features at various scales, improving detail recovery in different lighting conditions typical of PSR.

## Enhance Model Architecture:

Integrate attention mechanisms in the Efficient U-Net to allow the model to focus on important features in shadowed regions, enhancing feature extraction and reducing noise.
Consider using residual connections in RetinexNet to improve feature propagation and learning efficiency.

## Post-Processing Enhancements:

After model predictions, apply post-processing techniques like bilateral filtering or non-local means denoising to refine outputs and reduce any remaining artifacts.

## Implement Regularization Techniques:

Use techniques like dropout, batch normalization, or weight regularization in your models to enhance generalization and reduce overfitting.
