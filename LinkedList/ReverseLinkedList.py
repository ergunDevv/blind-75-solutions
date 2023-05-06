# QUESTION:
# 


def reverseLinkedList(head):
    previous,current= None,head

    while current:
        nextNode=current.next
        current.next=previous
        previous=current
        current=nextNode
    return previous
