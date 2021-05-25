from LinkedListNode import LinkedList


class DeleteMiddleNode:
    def __init__(self, ll):
        self.node = ll.head

    def delete_middle_using_two_pointers(self, node):
        node.data = node.next.data
        temp = node.next
        node.next = temp.next


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    linked_list = LinkedList(arr)
    ob = DeleteMiddleNode(linked_list)
    node = linked_list.head.next.next.next.next
    ob.delete_middle_using_two_pointers(node)
    linked_list.print()