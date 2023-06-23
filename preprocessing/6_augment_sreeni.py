

#https://youtu.be/k4TqxHteJ7s
#https://youtu.be/mwN2GGA4mqo
"""
@author: Sreenivas Bhattiprolu
"""

import numpy as np
from matplotlib import pyplot as plt
from skimage.transform import AffineTransform, warp
from skimage import io, img_as_ubyte
import random
import os
from scipy.ndimage import rotate

images_to_generate=4000
seed_for_random = 42

#Define functions for each operation
#Define seed for random to keep the transformation same for image and mask

# Make sure the order of the spline interpolation is 0, default is 3. 
#With interpolation, the pixel values get messed up.
def rotation(image, mask):
    
    angle= random.randint(-180,180)
    r_img = rotate(image, angle, mode='reflect', reshape=False, order=0)
    r_msk = rotate(mask, angle, mode='reflect', reshape=False, order=0)
    return r_img,r_msk

def h_flip(image, mask):
    hflipped_img= np.fliplr(image)
    hflipped_msk= np.fliplr(mask)
    return  hflipped_img,hflipped_msk

def v_flip(image, mask):
    vflipped_img= np.flipud(image)
    vflipped_msk= np.flipud(mask)
    return vflipped_img,vflipped_msk

def v_transl(image, mask):
    n_pixels = random.randint(-64,64)
    vtranslated_img = np.roll(image, n_pixels, axis=0)
    vtranslated_msk = np.roll(mask, n_pixels, axis=0)
    return vtranslated_img,vtranslated_msk

def h_transl(image, mask):
    n_pixels = random.randint(-64,64)
    htranslated_img = np.roll(image, n_pixels, axis=1)
    htranslated_msk = np.roll(mask, n_pixels, axis=1)
    return htranslated_img,htranslated_msk



transformations = {'rotate': rotation,
                      'horizontal flip': h_flip, 
                      'vertical flip': v_flip,
                   'vertical shift': v_transl,
                   'horizontal shift': h_transl
                 }                #use dictionary to store names of functions 

images_path="E:\_palm\dataset_v2\patched_has_tree\w_palm\images\\" #path to original images
masks_path = "E:\_palm\dataset_v2\patched_has_tree\w_palm\masks\\"
img_augmented_path="E:\_palm\dataset_v2\patched_has_tree\w_palm\\augmented\images\\" # path to store aumented images
msk_augmented_path="E:\_palm\dataset_v2\patched_has_tree\w_palm\\augmented\masks\\" # path to store aumented images
images=[] # to store paths of images from folder
masks=[]

for im in os.listdir(images_path):  # read image name from folder and append its path into "images" array     
    images.append(os.path.join(images_path,im))

for msk in os.listdir(masks_path):  # read image name from folder and append its path into "images" array     
    masks.append(os.path.join(masks_path,msk))


i=1   # variable to iterate till images_to_generate

print(len(images))

while i<=images_to_generate: 
    number = random.randint(0, len(images)-1)  #PIck a number to select an image & mask
    print(number)
    image = images[number]
    mask = masks[number]
    #print(image, mask)
    #image=random.choice(images) #Randomly select an image name
    original_image = io.imread(image)
    original_mask = io.imread(mask)
    transformed_image = None
    transformed_mask = None
#     print(i)
    n = 0       #variable to iterate till number of transformation to apply
    transformation_count = random.randint(1, len(transformations)) #choose random number of transformation to apply on the image
    
    while n <= transformation_count:
        key = random.choice(list(transformations)) #randomly choosing method to call
          #Generate seed to supply transformation functions. 
        transformed_image,transformed_mask = transformations[key](original_image, original_mask)
        
        n = n + 1
        
    new_image_path= "%s/aug_img_%s.jpg" %(img_augmented_path, str(i).zfill(4))
    new_mask_path = "%s/aug_msk_%s.jpg" %(msk_augmented_path, str(i).zfill(4))   #Do not save as JPG
    io.imsave(new_image_path, transformed_image)
    io.imsave(new_mask_path, transformed_mask)
    i =i+1
    