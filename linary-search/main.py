def linary_search(list, item):
    i = 1
    while item > 0:
        line = list[i]
        if line == item:
            return line
        else:
            i += 1
    return None

myList = list(range(1, 100))
print(linary_search(myList, 19))
