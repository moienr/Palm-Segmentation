from unittest.mock import patch
import numpy as np
import matplotlib.pyplot as plt
from patchify import patchify
from skimage import io
import os

path = 'E:\_palm\dataset_v2\masks_binary\\'
opath = 'E:\_palm\dataset_v2\patched\patched_masks\\'
files = os.listdir(path)
files.sort()


for file in files:
    img=io.imread(path+file)
    print(img.shape) #sanity check to see if masks are the same size as images
    
    patches = patchify(img,(256,256),step=256-32)
    print(patches.shape)
    
    for i in range(patches.shape[0]):
        for j in range(patches.shape[1]):
            patch = patches[i,j,:,:]
            io.imsave(opath+ file.split('.')[0] + '_r'+ str(i).zfill(2) + '_c' + str(j).zfill(2) + '.jpg', patch)
    
    
    # io.imsave(opath + file.split('.')[0] + '.jpg',x)