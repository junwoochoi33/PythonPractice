
def merge_sort(arr):
    """
    병합 정렬 (Merge Sort) 알고리즘

    리스트를 반으로 나눈 후, 각각을 재귀적으로 정렬한 후 병합합니다.
    시간 복잡도: O(n log n)

    :param arr: 정렬할 리스트
    :return: 정렬된 리스트
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """
    두 정렬된 리스트를 병합하는 함수

    :param left: 정렬된 왼쪽 리스트
    :param right: 정렬된 오른쪽 리스트
    :return: 병합된 정렬 리스트
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result