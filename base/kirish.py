def big(a, b, c):
    """Kiritilgan sonlarning eng kattasini qaytaruvchi algorithm"""
    if a>b:
        if a>c:
            return f"{a}"
        else:
            return f"{c}"
    elif b>c:
        return f"{b}"
    else:
        return f"{c}"
    
def faktoriallar(N):
    faktorial = 1
    i = 1
    while i != N+1:
        faktorial *= i
        i += 1

    return faktorial


if __name__ == '__main__':
    print(faktoriallar(5))
    print(faktoriallar(6))
    print(faktoriallar(8))