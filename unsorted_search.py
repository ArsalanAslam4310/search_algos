from random import randint


def linear_search(list_of_numbers, target):
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] == target:
            return i


def front_back_search(lis, target):
    front = 0
    back = len(lis)-1

    while front <= back:
        if lis[front] == target:
            return front
        elif lis[back] == target:
            return back
        front += 1
        back -= 1
    return -1


list_of_numbers = [randint(0, 100) for _ in range(10000000)]
print("search started")
print(front_back_search(list_of_numbers, 9))
