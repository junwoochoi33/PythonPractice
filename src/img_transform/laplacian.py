from PIL import Image

def laplacian(image_path='../images/Doge.jpg'):

    laplacian_kernel = [
        [1, 1, 1],
        [1, -8, 1],
        [1, 1, 1]
    ]

    # 이미지 불러오기
    img = Image.open(image_path).convert('L') # 그레이스케일로 변환

    # 이미지를 2D 리스트로 반환
    image_data = list(img.getdata())
    image_width, image_height = img.size
    image_2d = [image_data[i * image_width: (i+1) * image_width] for i in range(image_height)]

    # 커널의 크기
    kernel_height = len(laplacian_kernel)
    kernel_width = len(laplacian_kernel[0])

    # 컨볼루션 결과를 저장핧 배열 (유효 영역 크기)
    result_height = image_height - kernel_height + 1
    result_width = image_width - kernel_width + 1
    result = [[0] * result_width for _ in range(result_height)]

    # 슬라이딩 윈도우를 이용한 컨볼루션 연산
    for i in range(result_height):
        for j in range(result_width):
            conv_value = 0
            # 커널과 해당 이미지 부분의 곱셈 후 연산
            for ki in range(kernel_height):
                for kj in range(kernel_width):
                    # 인덱스가 이미지 범위를 벗어나지 않도록 보장
                    if 0 <= i + ki < image_height and 0 <= j + kj < image_width:
                        conv_value += image_2d[i + ki][j + kj] * laplacian_kernel[ki][kj]
            result[i][j] = conv_value

    result_image = Image.new('L', (result_width, result_height))
    result_image.putdata([item for sublist in result for item in sublist])
    result_image.show()
