from modules.fiutils import *

from skimage.transform import resize

# processing for celeba dataset
def drive_preprocess(img):

    re_size   = 512
    img       = resize(img, [re_size, re_size])
    return img