"""
Berilgan son raqamlarini ekranga chiqaring.
Misol uchun, print_digits(154) chaqirilganda, quyidagilar ekranga chiqarishi kerak:
4
5
1
"""
def print_digits(num: int) -> None:
    """
    Kodni bu yerda yozing.
    """
    num_string = str(num)
    num_list = list(num_string)
    num_list.reverse()
    reversed_number = ''.join(num_list)
    reversed_number_list = list(reversed_number)
    for i in reversed_number_list:
        print(i)

def upper_case(first_name):
    name_uppered = first_name.title()

    return name_uppered

enter_name = input("Enter Your full name:\n>>>")
print(upper_case(enter_name))