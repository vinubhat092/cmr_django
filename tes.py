class Node:
    def __init__(self,data):
        self.data = data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head = None

    def inserAtBeginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            temp1 = curr.next
            curr.next = prev
            prev = curr
            curr = temp1
        # self.head = prev
        return prev

    def print(self):           #utility function to print the output
        if self.head is None:
            print("linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr +=str(itr.data) + '--->'
            itr = itr.next
        print(llstr) 

if __name__ == '__main__':
    o1 = LinkedList()
    o1.head = Node(1)
    o1.head.next = Node(1)
    o1.head.next.next = Node(3)
    o1.reverse()
    o1.print()


