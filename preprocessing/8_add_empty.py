import os
m_wp_ipath = 'E:\_palm\dataset_v2\patched_has_tree\wo_palm\masks\\' #with palm
i_wp_ipath = 'E:\_palm\dataset_v2\patched_has_tree\wo_palm\images\\'

m_o_path = 'E:\_palm\_final_with_empties\\train\masks\\'
i_o_path = 'E:\_palm\_final_with_empties\\train\images\\'

images = os.listdir(i_wp_ipath)
masks = os.listdir(m_wp_ipath)

i=1
for img,msk in zip(images,masks):
    if i%30 ==0:
        os.rename(i_wp_ipath+img, i_o_path+img)
        os.rename(m_wp_ipath+msk, m_o_path+msk)

    i += 1

