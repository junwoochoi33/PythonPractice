
def quick_sort_2(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_2(arr, low, pivot_index - 1)
        quick_sort_2(arr, pivot_index + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high): # pivot 전까지
        if arr[j] <= pivot: # pivot보다 작으면 i번째에 삽입
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # i번째 방 바로 다음에 pivot 삽입
    return i + 1

