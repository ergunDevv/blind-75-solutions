# QUESTION:
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Iterative Solution
def reverseLinkedList(head):
    previous,current= None,head

    while current:
        nextNode=current.next
        current.next=previous
        previous=current
        current=nextNode
    return previous

# Recursive Solution
# def recursiveReverseLinkedList(head):
