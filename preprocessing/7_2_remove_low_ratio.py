import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import os

m_ipath = 'E:\_palm\dataset_v2\patched_has_tree\w_palm\\augmented\masks\\' #with palm
i_ipath = 'E:\_palm\dataset_v2\patched_has_tree\w_palm\\augmented\images\\'



images = os.listdir(i_ipath)
masks = os.listdir(m_ipath)

i=1
for image,mask in zip(images,masks):
    img = io.imread(i_ipath+image)
    msk = io.imread(m_ipath+mask)
    
    msk[msk<200]=0 
    
    if (np.count_nonzero(msk)/256**2) <= 0.01:
        os.remove(i_ipath+image)
        os.remove(m_ipath+mask)
        
    


