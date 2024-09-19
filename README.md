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
      UNet model for gamma correction.
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

###Single Scale: 
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

###Enhanced Contrast: 
By enhancing the reflectance, SSR can make features more distinct against the background.

## Gamma Correction:

###Brightness Adjustment: 
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

###Enhanced Perceived SNR: 
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

