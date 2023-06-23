#Define a function to perform additional preprocessing after datagen.
#For example, scale images, convert masks to categorical, etc. 
def preprocess_data(img, mask):
    img = img/255
    mask[mask>=200] = 255
    mask[mask<200] = 0
    mask = mask/255

      
    return (img,mask)

#Define the generator.
#We are not doing any rotation or zoom to make sure mask values are not interpolated.
#It is important to keep pixel values in mask as 0, 1, 2, 3, .....
from tensorflow.keras.preprocessing.image import ImageDataGenerator
def trainGenerator(train_img_path, train_mask_path, batch_size, seed):

# we didnt use this augmentation part sicce we augmented our data hardcopy way using my own scripts
#     img_data_gen_args = dict(horizontal_flip=True,  
#                       vertical_flip=False,
#                       fill_mode='reflect')
    
#     image_datagen = ImageDataGenerator(**img_data_gen_args)
#     mask_datagen = ImageDataGenerator(**img_data_gen_args)
        
    image_datagen = ImageDataGenerator()
    mask_datagen = ImageDataGenerator()

    
    image_generator = image_datagen.flow_from_directory(
        train_img_path,
        class_mode = None,
        batch_size = batch_size,
        seed = seed)
    
    mask_generator = mask_datagen.flow_from_directory(
        train_mask_path,
        class_mode = None,
        color_mode = 'grayscale',
        batch_size = batch_size,
        seed = seed)
    
    train_generator = zip(image_generator, mask_generator)
    
    for (img, mask) in train_generator:
        img, mask = preprocess_data(img, mask)
        yield (img, mask)