class Node:
    def __init__(self,data=None):
        self.next=None
        self.data=data

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtTail(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        tmp_head=self.head
        while tmp_head.next:
            tmp_head=tmp_head.next
        tmp_head.next=newNode
    def reverseLL(self):
        curr=self.head
        prev=None
        while curr:
            tmp_node=curr.next
            curr.next=prev
            prev=curr
            curr=tmp_node
        return prev
    def printLinkedList(self,newHead=None):
        if newHead is None:
            current=self.head
        else:
            current=newHead
        while current:
            print(current.data,end=" ")
            current=current.next
if __name__=="__main__":
    LL=LinkedList()
    LL.insertAtTail(1)
    LL.insertAtTail(3)
    LL.insertAtTail(9)
    LL.insertAtTail(15)
    LL.insertAtTail(20)
    LL.printLinkedList()
    print("\nReversed LinkedList is")
    LL.printLinkedList(LL.reverseLL())





