from LinkedListNode import LinkedList

class Partition:
    def __init__(self, ll):
        self.head = ll.head

    def part_using_swap(self, x):
        first = self.head
        second = self.head.next
        while second:
            if first.data < x <= second.data or (first.data < x and second.data < x):
                first = first.next
                second = second.next
            elif first.data >= x > second.data:
                first.data, second.data = second.data, first.data
                first = first.next
                second = second.next
            elif first.data >= x:
                second = second.next


if __name__ == '__main__':
    arr = [3,5,8,5,10,2,1]
    linked_list = LinkedList(arr)
    pobj = Partition(linked_list)
    pobj.part_using_swap(5)
    linked_list.print()