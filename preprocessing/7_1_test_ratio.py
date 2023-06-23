
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import os

path = 'E:\_palm\\test ratio\\'

images = os.listdir(path)
images.sort()


for image in images:
    img=io.imread(path+image)
    img[img<200]=0 
    print(image)
    print(np.count_nonzero(img))
    print(np.count_nonzero(img)/256**2)