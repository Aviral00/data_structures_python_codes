class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next


if __name__ == '__main__':
    list1 = LinkedList()
    list1.head = Node(1)
    second = Node(2)
    list1.head.next = second
    second.next = Node(3)
    list1.print_list()



