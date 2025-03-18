import numpy as np
from PIL import Image, ImageFilter

from src.image_transform.laplacian import laplacian


def detect_depth(image_path='../images/Eiffle.png'):

    # 1. Grayscale로 변환
    img = Image.open(image_path).convert('L')
    img_arr = np.array(img, dtype=np.float32)

    # 2. Gaussian Blur 적용
    blurred = img.filter(ImageFilter.GaussianBlur(5))
    blurred_arr = np.array(blurred, dtype=np.float32)

    # 3. 원본과 블러된 이미지 차이 계산
    depth_map = np.abs(img_arr - blurred_arr)

    # 4. Laplacian 필터 적용
    laplacian_kernel = np.array([
        [1, 1, 1],
        [1, -8, 1],
        [1, 1, 1]
    ])

    def convolve2d(image, kernel):
        h, w = image.shape
        kh, kw = kernel.shape
        pad_h, pad_w = kh // 2, kw // 2
        padded_img = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), 'constant', constant_values=0)
        result = np.zeros_like(image)

        for i in range(h):
            for j in range(w):
                result[i, j] = np.sum(padded_img[i:i+kh, j:j+kw] * kernel)

        return result

    laplacian = convolve2d(img_arr, laplacian_kernel)

    # 5. 두 결과를 결합하여 깊이 맵 생서
    combined_depth = depth_map + np.abs(laplacian)

    # 6. 후처리
    # 1) 정규화 (0~255 범위로 변환)
    combined_depth = (combined_depth / combined_depth.max() * 255).astype(np.uint8) # 정규화
    # 2) Gaussian Blur 적용
    depth_image = Image.fromarray(combined_depth)
    smoothed_depth = depth_image.filter(ImageFilter.GaussianBlur(radius=3))
    # 3) Gamma Correction
    gamma = 1.1
    depth_array = np.array(smoothed_depth, dtype=np.float32) / 255.0
    depth_array = np.power(depth_array, gamma) * 255.0
    depth_array = depth_array.astype(np.uint8)

    Image.fromarray(depth_array).show()
