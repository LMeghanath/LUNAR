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
 like RetinexNet model for SSR. 
      UNet model for gamma correction.
      and applying histogram equalization.
      
As the values of sigma in SSR and gamma in Gamma Reduction varies for different images.
So that it gives a better output.

Lets see about the techniques and models used in this project:
SSR (Single Scale Retinex):
    
