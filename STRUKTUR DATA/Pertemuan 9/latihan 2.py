class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def tambah_belakang(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        print("none")

    def hapus_depan(self):
        if self.head is None:
            print("double linked list kosong")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def hapus_data(self, data):
        current_node = self.head

        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                return
            current_node = current_node.next
        print(f"Data {data} tidak ditemukan.")

dll = DoublyLinkedList()
dll.tambah_belakang(10)
dll.tambah_belakang(20)
dll.tambah_belakang(30)
dll.display()