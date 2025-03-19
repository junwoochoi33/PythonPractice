from src.sort.quick_sort_2 import quick_sort_2


def start():
    print("Application started!")

    arr = [10, 7, 8, 9, 1, 5]
    # 테스트
    print(quick_sort_2(arr, 0, len(arr) - 1))
