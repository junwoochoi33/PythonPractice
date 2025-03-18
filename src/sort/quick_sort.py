
def quick_sort(arr):
    """
    퀵 정렬 (Quick Sort) 알고리즘

    리스트에서 피벗을 고르고, 그 피벗을 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽에 배치하여
    정렬된 리스트를 얻는 알고리즘입니다.
    시간 복잡도: O(n log n) (평균 경우), O(n^2) (최악의 경우)

    :param arr: 정렬할 리스트
    :return: 정렬된 리스트
    """
    if len(arr) <= 1: # 리스트의 길이가 1 이하이면 이미 정렬됨
        return arr

    pivot = arr[len(arr) // 2] # 피벗을 리스트의 중간값으로 설정
    left = [x for x in arr if x < pivot] # 피벗보다 작은 값
    middle = [x for x in arr if x == pivot] # 피벗과 같은 값
    right = [x for x in arr if x > pivot] # 피벗보다 큰 값

    return quick_sort(left) + middle + quick_sort(right)
