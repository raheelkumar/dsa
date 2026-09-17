class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

    # initialize to empty list
    def __init__(self):
            self.head = None
            self.tail = None
            self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end = '')
            if temp.next is not None:
                print(' --> ', end = '')
            temp = temp.next
        print()

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            self.prepend(value)

        elif index == self.length:
            self.append(value)

        else:
            i=0
            pointer = self.head
            while i != index-1:
                pointer = pointer.next
                i+=1
            new_node.next = pointer.next
            pointer.next = new_node
            self.length += 1

    def pop(self):
        if self.head == None:
            print('Nothing to pop, Linked List is empty.')
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            pre = self.head
            temp = self.head.next
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            return temp.value
            

if __name__ == "__main__":
    my_linked_list = LinkedList()
    my_linked_list.append(4)
    my_linked_list.print_list()
    my_linked_list.append(6)
    my_linked_list.print_list()
    my_linked_list.prepend(3)
    my_linked_list.print_list()
    my_linked_list.insert(2,5)
    my_linked_list.print_list()
    my_linked_list.insert(0,2)
    my_linked_list.print_list()
    my_linked_list.pop()
    my_linked_list.print_list()