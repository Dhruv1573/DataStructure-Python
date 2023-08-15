class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None
    def insertNodeAtTail(self,data):
        newNode=Node(data)
        if self.head:
            current=self.head
            while current.next:
                current=current.next
            current.next=newNode
        else:
            self.head=newNode

    def getMiddleNode(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
        pass
    def printLinkedList(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next

if __name__=="__main__":
    head=Node()
    LL=LinkedList()
    LL.insertNodeAtTail(1)
    LL.insertNodeAtTail(2)
    LL.insertNodeAtTail(5)
    LL.insertNodeAtTail(9)
    LL.insertNodeAtTail(10)
    LL.printLinkedList()
    print("Middle Node is",LL.getMiddleNode().data)
