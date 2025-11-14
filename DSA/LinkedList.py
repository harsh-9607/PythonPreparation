# Node class
class Node:
    def __init__(self, data):
        self.data = data  # store data
        self.next = None  # reference to the next node

class LinkedList:
    def __init__(self):
        self.head=None
        self.last=None
    def append(self,data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            self.last= newnode
            return
        self.last.next = newnode
        self.last = newnode

    def prepend(self,data):
        newnode = Node(data)
        newnode.next= self.head
        self.head= newnode
    def delete(self,key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        prev.next = current.next
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("none", end="")
        print("")

        

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(4)
ll.display()  # Output: 5 -> 10 -> 20 -> 30 -> None

ll.delete(20)
ll.display()  # Output: 5 -> 10 -> 30 -> None
   
ll.delete(10)
ll.display()