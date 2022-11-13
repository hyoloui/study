# [3] -> [4]
# data, next
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data) -> None:
        self.head = Node(data)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        cur = self.head
        while cur.next is not None:

            cur = cur.next
            print("Cur is", cur.data)
        cur.next = Node(data)

    def print_all(self):
        print('hihi')
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

# node = Node(3)
# first_node = Node(4)
# node.next = first_node

# print(node.next.data)


linked_list = LinkedList(3)
# print(linked_list.head.next)

linked_list.append(4)
linked_list.append(5)
linked_list.print_all()
