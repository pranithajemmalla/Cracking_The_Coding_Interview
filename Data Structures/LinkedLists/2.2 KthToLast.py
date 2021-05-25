from LinkedListNode import LinkedList


class KthToLast:
    def __init__(self, linked_list, n, k):
        self.linked_list = linked_list
        self.head = self.linked_list.head if self.linked_list else None
        self.k = k
        self.n = n
        self.res = None

    def kth_to_last_iterative(self):
        fast_ptr = slow_ptr = temp = self.head
        count = 1
        while fast_ptr and fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next and fast_ptr.next.next
            count += 1

        self.n = count * 2

        if not fast_ptr.next:
            self.n -= 1

        if self.n - self.k + 1 <= 0:
            return None

        if self.n - self.k + 1 < count:
            temp = self.head
            count = self.n - self.k
        else:
            temp = slow_ptr
            count = int(self.n / 2) - self.k + 1

        while count:
            temp = temp.next
            count -= 1
        return temp.data

    def kth_to_last_recursive(self, head, count, k):
        if head:
            ret_val = 1 + self.kth_to_last_recursive(head.next, count + 1, k)
            if ret_val == k:
                self.res = head.data
            return ret_val
        else:
            return 0

    def using_kth_to_last_recursive(self):
        self.kth_to_last_recursive(self.head, 0, self.k)
        return self.res


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    linked_list = LinkedList(arr)
    ob = KthToLast(linked_list, None, 6)
    print(ob.kth_to_last_iterative())
    print(ob.using_kth_to_last_recursive())
