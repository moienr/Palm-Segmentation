from matplotlib import image
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import os
import random

N_IMAGES  = 5 #number of images and their corresponding images to plot

m_path = 'E:\_palm\dataset_v2\patched_has_tree\w_palm\masks\\'
i_path = 'E:\_palm\dataset_v2\patched_has_tree\w_palm\images\\'

images = os.listdir(i_path)
images.sort()

masks = os.listdir(m_path)
masks.sort()


images =np.array(images)
masks =np.array(masks)
# print(images)
idx = np.random.choice(np.arange(len(images)), N_IMAGES, replace=False)
i_sample = images[idx]
m_sample = masks[idx]

x = [i_sample,m_sample]

for i in x:
    print(i)


print(x)

fig, ax = plt.subplots(2, N_IMAGES)
k = 0 
t = 0
for i in range(2):
    for j in range(N_IMAGES):
        if i==0:
            img = io.imread(i_path+x[i][j])
        else:
            img = io.imread(m_path+x[i][j])
         
        im = ax[i, j].imshow(img)
        
        if i==0 :
            ax[i, j].set_title('IMG ' + x[i][j])
        else:
            ax[i, j].set_title('MSK ' + x[i][j])
        # plt.colorbar(im, ax=ax[i, j])
plt.show()
