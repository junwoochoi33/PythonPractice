import numpy as np
from PIL import Image, ImageFilter


def detect_depth(image_path='../images/Doge.jpg'):

    # 이미지 열기 및 흑백 변환 (명암차 분석을 위해 Grayscale 사용)
    img = Image.open(image_path).convert('L')

    # 이미지를 numpy 배열로 변환
    img_arr = np.array(img, dtype=np.float32)

    # Sobel 필터를 사용하여 엣지 검출
    sobel_x = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])

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

    grad_x = convolve2d(img_arr, sobel_x)
    grad_y = convolve2d(img_arr, sobel_y)

    # Gradient Magnitude 계산 (엣지 강도)
    depth_map = np.sqrt(grad_x**2 + grad_y**2)
    depth_map = (depth_map / np.max(depth_map) * 255).astype(np.uint8) # 정규화

    Image.fromarray(depth_map).show()
