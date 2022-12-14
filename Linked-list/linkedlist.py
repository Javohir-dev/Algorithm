class Node:
  """Tugun (node) objecti"""
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  """Linked list objecti"""
  def __init__(self):
    self.head = None

  def printList(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next

  def push(self, new_data):
    """List boshiga tugun qo'shish"""
    # Yangi node yaratish
    new_node = Node(new_data)
    # List boshini keyingi o'ringasuramiz
    new_node.next = self.head
    # Yangi nodeni list boshiga qo'yamiz
    self.head = new_node

  def inserAfter(self, prev_node, new_data):
    """Biror tugundan so'ng tugun qo'shish"""
    if prev_node is None:
      print("Tugun mavjud emas")
      return
    # Yangi tugun qo'shamiz
    new_node = Node(new_data)
    # Yangi tugunni keyingi tugunga bog'lash
    new_node.next = prev_node.next
    # Avvalgi tugun yangi tugunga bog'laymiz
    prev_node.next = new_node

  def append(self, new_data):
    """List oxiriga tugun qo'shish"""
    # Yangi tugun yaratamiz
    new_node = Node(new_data)
    # List bo'sh emasligini tekshiramiz
    if self.head is None:
      # Bo'sh bo'lsa yangi tugun list boshiga qo'shamiz
      self.head = new_node
      return
    # Aks holda List oxiriga boramiz
    last = self.head
    while last.next:
      last = last.next
    last.next = new_node
  def deleteNode(self, key):
    """List qiymatini o'chirish"""
    # List boshini topib olamiz
    temp = self.head
    # Birinchi tugunni tekshiramiz
    if (temp and temp.data == key):
      self.head = temp.next
      temp = Node
      return
    # Aks holda boshqa tugunlarni qarab chiqamiz
    while temp:
      if temp.data == key:
        break
      prev = temp
      temp = temp.next
    # Agar qiymat qopilmasa
    if temp == Node:
      return
    # Tugunni Listdan o'chiramiz
    prev.next = temp.next
    temp = Node