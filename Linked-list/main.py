from linkedlist import Node, LinkedList

## linked-list yaratamiz
llist = LinkedList()

## Uchta node (tugun) yaratamiz
llist.head = Node("Dushanba")
tuesday = Node("Seshanba")
wednesday = Node("Chorshanba")

## Tugunlarni bog'laymiz
llist.head.next = tuesday
tuesday.next = wednesday

# print(llist.head.next.data)
# # -> Seshanba
# print(llist.head.next.next.data)
# # -> Chorshanba

## linkedListni consolega chiqarib ko'ramiz
# llist.printList()

## List boshiga yangi tugun qo'shamiz
llist.push('Yakshanba')
# llist.printList()

## List o'rtasiga yangi element qo'shamiz
llist.inserAfter(llist.head.next, "Dushanba Kechasi")
# llist.printList()
# # -> Yakshanba
# # -> Dushanba
# # -> Dushanba Kechasi
# # -> Seshanba
# # -> Chorshanba

## List oxiriga element qo'shamiz
llist.append('Payshanba')
# llist.printList()
# # -> Yakshanba
# # -> Dushanba
# # -> Dushanba Kechasi
# # -> Seshanba
# # -> Chorshanba
# # -> Payshanba
# ! Time line: (14:47) of link: (https://youtu.be/IjP7eU316O0)