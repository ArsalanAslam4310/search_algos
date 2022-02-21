from random import randint


def binary_search(lis, target):
    front = 0
    mid = 0
    back = len(lis)-1

    while front <= back:
        mid = (front+back)//2
        if lis[mid] == target:
            return mid
        elif lis[mid] < target:
            front = mid+1
        else:
            back = mid-1
    return -1


unsorted_list = [randint(0, 10) for _ in range(100000000)]
sorted_list = sorted(unsorted_list)
print("search started")
print(binary_search(sorted_list, 3))
