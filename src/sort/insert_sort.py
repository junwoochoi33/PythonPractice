
def insert_sort(arr):
    """
    삽입 정렬 (Insertion Sort) 알고리즘

    리스트를 순차적으로 탐색하며, 각 원소를 정렬된 부분에 삽입합니다.
    시간 복잡도: O(n^2)

    :param arr: 정렬할 리스트
    :return: 정렬된 리스트
    """
    for i in range(1, len(arr)): # 두 번째 요소부터 시작
        key = arr[i] # 현재 원소를 key에 저장
        j = i - 1 # key의 이전 원소 인덱스

        # key가 arr[j]보다 작으면, a[j]의 값을 a[j+1]로, 즉 한 칸 뒤로 밀어냄
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # key를 알맞은 위치에 삽입
        arr[j + 1] = key

    return arr