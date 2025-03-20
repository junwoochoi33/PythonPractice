
def counting_sort(arr):

    n = len(arr)
    min_val = min(arr)
    max_val = max(arr)

    count_arr = [0] * (max_val - min_val + 1)
    result_arr = [0] * n

    # 각 값에 대한 등작 횟수를 셈
    for num in arr:
        idx = num - min_val
        count_arr[idx] += 1

    # 각 계수 배열에 누적 합을 더하여 위치를 계산
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # 출력 배열 작성
    for num in reversed(arr): # 같은 값이 여러 개 있을 경우 기존의 순서를 보장하기 위함 (정렬의 안정성)
        idx = num - min_val
        count_arr[idx] -= 1
        result_arr[count_arr[idx]] = num

    return result_arr
