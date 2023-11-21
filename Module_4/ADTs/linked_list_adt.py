class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        # this method checks if the linked list is empty by examining the head attribute
        return self.head is None
    
    def insert(self, data):
        # insert an element/node at a specified position (end of linked list)
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        # remove an element/node from a specified position
        if not self.is_empty():
            if self.head.data == data:
                self.head = self.head.next
            else:
                current = self.head
                while current.next:
                    if current.next.data == data:
                        current.next = current.next.next
                        return
                    current = current.next

    def get(self, index):
        # retrieve an element from a specified position
        if index < 0:
            raise IndexError("Invalid index")
        count = 0
        current = self.head
        while current:
            if count == index:
                return current.data
            count +=1
            current = current.next
        raise IndexError("Index out of range")
    
linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.insert(40)

print(linked_list.get(0))
print(linked_list.get(1))

linked_list.delete(30)

print(linked_list.get(2))
print(linked_list.is_empty())


# output --> 
    # 10
    # 20
    # 40
    # False
