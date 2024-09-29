# LUNAR
Enhancement of psr images.

We don't have the sufficent data ,i.e, image dataset to train the model at present.So we did the remaing processing of it.
In future we will make a data set for normal low light images and apply it to LLNet, if the data of PSR regions is confidential.

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


