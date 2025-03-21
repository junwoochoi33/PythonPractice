from PIL import Image, ImageFilter
import numpy as np
from scipy.ndimage import gaussian_filter

def map_depth(img_left_path='../images/stereo_img_1.jpg', img_right_path='../images/stereo_img_2.jpg'):

    print("map_depth: start")

    img_left = np.array(Image.open(img_left_path).convert('L'), dtype=np.float32)
    img_right = np.array(Image.open(img_right_path).convert('L'), dtype=np.float32)

    focal_length = 800
    baseline = 0.1

    depth_map = compute_depth(compute_disparity(img_left, img_right, window_size=5, max_disp=64), focal_length, baseline)

    depth_map_normalized = np.uint8(255 * (depth_map / np.max(depth_map)))

    depth_image = Image.fromarray(depth_map_normalized)

    print("map_depth: done")

    depth_image.show()


def compute_disparity(img_left, img_right, window_size=5, max_disp=64):

    print("compute_disparity: start")

    height, width = img_left.shape
    disparity_map = np.zeros_like(img_left)

    half_window = window_size // 2

    for y in range(half_window, height - half_window):
        for x in range(half_window, width - half_window):
            best_offset = 0
            min_ssd = float('inf')

            for offset in range(max_disp):
                if x - offset - half_window < 0:
                    continue

                ssd = np.sum((img_left[y - half_window:y + half_window + 1, x - half_window:x + half_window + 1] -
                              img_right[y - half_window:y + half_window + 1,
                              x - offset - half_window:x - offset + half_window + 1]) ** 2)
                if ssd < min_ssd:
                    min_ssd = ssd
                    best_offset = offset

            disparity_map[y, x] = best_offset

    print("compute_disparity: done")

    return disparity_map


def compute_depth(disparity_map, focal_length, baseline):
    with np.errstate(divide='ignore', invalid='ignore'):
        depth_map = (focal_length * baseline) / (disparity_map + 1e-5)  # Avoid division by zero
    return depth_map
