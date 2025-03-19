def heap_sort(arr):
    n = len(arr)

    # 최대 힙 구성
    for i in range(n // 2 - 1, -1, -1): # 리프가 아닌 부모 노드들을 역순으로 heapify
        heapify(arr, n, i)

    # 힙에서 요소 하나씩 꺼내 정렬
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 루트(최댓값)와 마지막 요소 교환
        heapify(arr, i, 0)  # 줄어든 힙에 대해 다시 힙 속성 유지

    return arr  # 정렬된 배열 반환

def heapify(arr, n, i):
    largest = i  # 부모 노드
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 스왑
        heapify(arr, n, largest)  # 재귀적으로 힙 속성 유지
