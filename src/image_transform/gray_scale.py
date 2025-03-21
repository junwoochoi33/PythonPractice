from PIL import Image
import numpy as np


def gray_scale(image_path='../images/Doge.jpg'):

    img = Image.open(image_path).convert('RGB')

    img_arr = np.array(img)

    r_weight = 0.1 # 0.299
    g_weight = 0.1 # 0.587
    b_weight = 0.8 # 0.114

    gray_arr = (
        r_weight * img_arr[:, :, 0] +
        g_weight * img_arr[:, :, 1] +
        b_weight * img_arr[:, :, 2]
    ).astype(np.uint8)

    gray_img = Image.fromarray(gray_arr)

    gray_img.show()






