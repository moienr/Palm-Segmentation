import os
m_wp_ipath = 'E:\_palm\dataset_v2\patched_has_tree\w_palm\masks\\' #with palm
i_wp_ipath = 'E:\_palm\dataset_v2\patched_has_tree\w_palm\images\\'

m_tst_path = 'E:\_palm\dataset_v2\patched_has_tree\w_palm\\test_images\masks\\'
i_tst_path = 'E:\_palm\dataset_v2\patched_has_tree\w_palm\\test_images\images\\'

images = os.listdir(i_wp_ipath)
masks = os.listdir(m_wp_ipath)

i=1
for img,msk in zip(images,masks):
    if i%10 ==0:
        os.rename(i_wp_ipath+img, i_tst_path+img)
        os.rename(m_wp_ipath+msk, m_tst_path+msk)

    i += 1

