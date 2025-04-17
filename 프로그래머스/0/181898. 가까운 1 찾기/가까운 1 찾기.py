def solution(arr, idx):
    if 1 not in arr[idx:]:
        return -1
    return arr[idx:].index(1) + idx