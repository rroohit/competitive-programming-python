from read_inputs.ListNode import ListNode


# Solved
def detectCycle(head: ListNode) -> ListNode:
    if head is None:
        return None

    if head.next is None:
        return None

    mapNodes = set()

    while head:
        if head in mapNodes:
            return head

        mapNodes.add(head)
        head = head.next

    return None


# Initialize a linked list with values [3, 2, 0, -4]
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

isCycle = detectCycle(node1)
if isCycle:
    print("List has cycle in it at value => ", isCycle.val)
else:
    print("No cycle in list")
