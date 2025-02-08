class Node:
    def __init__(self,data:int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self,new_node:Node):
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
    def print_list(self):
        current = self.head
        while current:
            if current.next == None:
                print(current.data)
                break
            print(current.data,end=" ===> ")
            current = current.next
        print()

number = int(input("Enter a number:"))
list = LinkedList()

for i in range(number):
    data = int(input(f"\nEnter element {i+1}: "))
    node = Node(data)
    list.add(node)
print("\n\nThe Linked List:")
list.print_list()