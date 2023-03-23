class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def reverse_linked_list(head: ListNode) -> ListNode:
    if head.next:
        yield from reverse_linked_list(head.next)
    yield head.value

# Create a singly linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Reverse the list
new_head = reverse_linked_list(head)
print(list(new_head)) 
# The new list should be: 5 -> 4 -> 3 -> 2 -> 1
