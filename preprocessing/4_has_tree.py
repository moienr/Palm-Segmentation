from unittest.mock import patch
import numpy as np
import matplotlib.pyplot as plt
from patchify import patchify
from skimage import io
import os

m_path = 'E:\_palm\dataset_v2\patched\patched_masks\\'
i_path = 'E:\_palm\dataset_v2\patched\patched_images\\'

m_wp_opath = 'E:\_palm\dataset_v2\patched_has_tree\w_palm\masks\\' #with palm
i_wp_opath = 'E:\_palm\dataset_v2\patched_has_tree\w_palm\images\\'

m_wop_opath = 'E:\_palm\dataset_v2\patched_has_tree\wo_palm\masks\\' #witouth palm
i_wop_opath = 'E:\_palm\dataset_v2\patched_has_tree\wo_palm\images\\'

images = os.listdir(i_path)
images.sort()

masks = os.listdir(m_path)
masks.sort()

for image,mask in zip(images,masks):
    img = io.imread(i_path+image)
    msk = io.imread(m_path+mask)
    
    if np.max(msk)>0:
        io.imsave(i_wp_opath+image,img)
        io.imsave(m_wp_opath+mask,msk)
    else:
        io.imsave(i_wop_opath+image,img)
        io.imsave(m_wop_opath+mask,msk)

