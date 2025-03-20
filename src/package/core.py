from src.sort.radix_sort import radix_sort


def start():
    print("Application started!")

    arr = [10, 7, 8, 9, 1, 5]
    # 테스트
    print(radix_sort(arr))
