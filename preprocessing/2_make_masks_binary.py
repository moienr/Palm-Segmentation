from skimage import io
import matplotlib.pyplot as plt
import os
import tifffile
import numpy as np
# so mask from apeer.com are 0,1,2 which 1 and 2 represent tow diffrent kind of palm, but in this work we just want to find 
# any palms, so we turn 2s into ones.

path = 'E:\_palm\dataset_v2\mask\\'
opath = 'E:\_palm\dataset_v2\masks_binary\\'
files = os.listdir(path)
files.sort()


for file in files:
    x=tifffile.imread(path+file)
    print(x.shape) #sanity check to see if masks are the same size as images
    
    x[x>0] = 255
    print(np.max(x))
    
    io.imsave(opath + file.split('.')[0] + '.jpg',x)
    


