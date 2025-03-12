from PIL import Image

def scaling(image_path='../images/Doge.jpg', scale=1.5):

    # 이미지 열기
    img = Image.open(image_path).convert('RGB')
    w, h = img.size

    # 새로운 크기 계산
    new_w = int(w * scale)
    new_h = int(h * scale)

    # 새로운 이미지 생성
    new_img = Image.new('RGB', (new_w, new_h), (0, 0, 0))

    # 이미지 변환: 픽셀 단위로 보간법 적용
    for y in range(new_h):
        for x in range(new_w):
            # 원본 이미지에서 변환된 좌표 계산
            src_x = x / scale
            src_y = y / scale

            # Bilinear interpolation을 사용해 색상 계산
            color = bilinear_interpolation(src_x, src_y, img)

            new_img.putpixel((x, y), color)

    # 변환된 이미지 띄우기
    new_img.show()


def bilinear_interpolation(x, y, img):

    x1, y1 = int(x), int(y) # 정수형으로 형변환
    x2, y2 = min(x1 + 1, img.width - 1), min(y1 + 1, img.height - 1)

    # 4개의 근처 픽셀 값 가져오기
    c11 = img.getpixel((x1, y1))
    c12 = img.getpixel((x1, y2))
    c21 = img.getpixel((x2, y1))
    c22 = img.getpixel((x2, y2))

    # 각 채널에 대해 보간법 적용 (R, G, B 채널 각각)
    r1 = (x2 - x) * c11[0] + (x - x1) * c21[0]
    r2 = (x2 - x) * c12[0] + (x - x1) * c22[0]
    g1 = (x2 - x) * c11[1] + (x - x1) * c21[1]
    g2 = (x2 - x) * c12[1] + (x - x1) * c22[1]
    b1 = (x2 - x) * c11[2] + (x - x1) * c21[2]
    b2 = (x2 - x) * c12[2] + (x - x1) * c22[2]

    # 최종 R, G, B 값을 y 방향으로 보간
    r = (y2 - y) * r1 + (y - y1) * r2
    g = (y2 - y) * g1 + (y - y1) * g2
    b = (y2 - y) * b1 + (y - y1) * b2

    return int(r), int(g), int(b)