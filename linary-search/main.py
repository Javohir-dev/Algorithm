def linary_search(list, item):
    for n in range(len(list)):
        # print(n)
        if n == item:
            return n
    return None

myList = list(range(1, 100))
print(linary_search(myList, 19))
