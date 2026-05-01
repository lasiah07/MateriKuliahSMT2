class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    # ===== BASIC =====
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack kosong!")
        value = self.head.value
        self.head = self.head.next
        self.count -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack kosong!")
        return self.head.value

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.count

    # ===== TAMBAHAN =====
    def clear(self):
        self.head = None
        self.count = 0

    def to_list(self):
        data = []
        current = self.head
        while current:
            data.append(current.value)
            current = current.next
        return data

    def contains(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


# ===== FITUR =====

def cek_kurung(text):
    stack = StackLinkedList()
    pasangan = {')': '(', '}': '{', ']': '['}

    for char in text:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty() or stack.peek() != pasangan[char]:
                return False, stack.to_list()
            stack.pop()

    return stack.is_empty(), stack.to_list()


def balik_string(text):
    stack = StackLinkedList()

    for huruf in text:
        stack.push(huruf)

    hasil = ""
    while not stack.is_empty():
        hasil += stack.pop()

    return hasil