
def counting_sort(arr, exp):

    n = len(arr)

    count_arr = [0] * 10
    result_arr = [0] * n

    #  각 자릿수에 대한 카운트
    for i in range(n):
        idx = arr[i] // exp
        count_arr[idx % 10] += 1

    # 카운트를 누적하여 해당 자리에 들어갈 위치 계산
    for i in range(1, 10):
        count_arr[i] += count_arr[i-1]

    # 출력 배열에 정렬된 값 저장
    for i in range(n - 1, -1, -1):
        idx = arr[i] // exp
        count_arr[idx % 10] -= 1
        result_arr[count_arr[idx % 10]] = arr[i]

    return result_arr



def radix_sort(arr):

    max_val = max(arr)

    exp = 1
    while max_val // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10

    return arr