# # Algorithm

# def hisobla():
#     son1 = int(input("1-sonni kiriting: "))
#     son2 = int(input("2-sonni kiriting: "))
#     summa = son1 + son2
#     return summa


# # print(hisobla())

# # Katta son topish


# def eng_katta(a, b, c):
#     print(a, b, c)
#     if a > b:
#         if a > c:
#             javob = f"eng katta son `{a}`."
#         else:
#             javob = f"eng katta son `{c}`."
#     elif a < b:
#         if b > c:
#             javob = f"eng katta son `{b}`."
#         else:
#             javob = f"eng katta son `{c}`."

#     return javob


# # print(eng_katta(120, 100, 99))


# # N faktorial


def faktoriallar(N):
    faktorial = 1
    for i in range(1, N + 1):
        faktorial *= i
    return faktorial


son = int(input("Son kiriting: "))
print(faktoriallar(son))
