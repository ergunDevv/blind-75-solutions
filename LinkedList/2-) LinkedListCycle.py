# QUESTION :
# Given head, the head of a linked list, determine if the linked list has a cycle in it.There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.Return true if there is a cycle in the linked list. Otherwise, return false.


# Solution:
def linkedListCycle(head):
    # Defining two pointers
    slow, fast = head, head
    # If fast pointer is none break the while loop and return false because linked list is not a cycle.
    while fast and fast.next:
        # Shifting fast pointer by 2
        fast = fast.next.next
        # Shifting slow pointer by 1
        slow = slow.next
        # If at some point fast pointer and slow pointer is same node that means linked list is cycle list
        # If not fast pointer will equal to none and break the while loop
        if fast == slow:
            return True
    return False
