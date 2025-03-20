def heapify(arr, n, i):
    largest = i  # 루트를 가장 큰 값으로 설정
    left = 2 * i + 1  # 왼쪽 자식
    right = 2 * i + 2  # 오른쪽 자식

    # 왼쪽 자식이 루트보다 크면 largest 갱신
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 largest보다 크면 largest 갱신
    if right < n and arr[right] > arr[largest]:
        largest = right

    # largest가 루트가 아니면 교환 후 재귀적으로 heapify 호출
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest) # arr[i]의 값을 계속 largest로 재귀적으로 전달

def heap_sort(arr):
    n = len(arr)

    # 1. 최대 힙 생성
    for i in range(n // 2 - 1, -1, -1): # 배열의 마지막 부모 노드부터 루트 노드까지 역순으로 heapify 수행
        heapify(arr, n, i)

    # 2. 하나씩 요소를 제거하며 정렬 수행
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 최댓값을 배열의 끝으로 이동, 지속적으로 최댓값을 맨 뒤로 보내고 그 전까지 heapify
        heapify(arr, i, 0)  # 줄어든 힙 크기에 대해 heapify 수행, largest를 계속 0로 설정해서 재귀적으로 전달

    return arr

