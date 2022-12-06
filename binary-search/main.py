def binary_search(list, item):
    low = 0
    i = 1
    hight = len(list)-1
    while low <= hight:
        print(i)
        i += 1
        mid = (low + hight)//2
        guess = list[mid]
        if guess == item:
            return guess
        if guess > item:
            hight = mid - 1
        else:
            low = mid + 1

    return None

myList = list(range(1, 2000))
print(binary_search(myList,1999))
