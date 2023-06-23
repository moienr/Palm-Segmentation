import os



#I used this script to rename the first 300 file the original folder as img1.png to img301.png
# path = 'E:\_palm\dataset_v2\mask\\'
# files = os.listdir(path)
# for file in files:
#         print(file[17:21])
#         os.rename(os.path.join(path, file), os.path.join(path, ''.join([file.split('.')[0], '.tiff'])))
        

path = 'E:\_palm\dataset_v2\img\\'
files = os.listdir(path)
for file in files:
        print(file[17:21])
        os.rename(os.path.join(path, file), os.path.join(path, ''.join([file[17:21], '.jpg'])))