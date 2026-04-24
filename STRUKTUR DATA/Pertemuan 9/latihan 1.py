class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlyLinkedList:
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

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        print("none")

    def hapus_depan(self):
        if self.head is None:
            print("single linked list kosong")
            return
        self.head = self.head.next

    def hapus_data(self, data):
        current_node = self.head
        previous_node = None

        while current_node:
            if current_node.data == data:
                if previous_node is None:
                    self.head = current_node.next
                else:
                    previous_node
                return
            previous_node = current_node
            current_node = current_node.next
        print(f"Data {data} tidak ditemukan.")

sll = singlyLinkedList()
sll.tambah_belakang(10)
sll.tambah_belakang(20)
sll.tambah_belakang(30)
sll.display()
sll.hapus_depan()
sll.hapus_data(21)
print("isi Single Linked List:")
sll.display()