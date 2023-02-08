"""
Berilgan son raqamlariga teskari son qaytaring.
Misol uchun:
reverse_digits(154) => 451
reverse_digits(710) => 17
"""
def reverse_digits(num: int) -> int:
    """
    Kodni bu yerda yozing.
    """
    num_string = str(num)
    num_list = list(num_string)
    while '0' in num_list:
        if '0' in num_list:
            num_list.remove('0')


    num_list.reverse()
    reversed_number = ''.join(num_list)

    return reversed_number