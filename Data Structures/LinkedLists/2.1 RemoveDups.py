class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class RemoveDups:
    def __init__(self):
        self.linked_list = None

    def remove_dups_using_brute_force(self):
        temp = self.linked_list
        while temp:
            pre = temp
            temp2 = temp.next
            while temp2:
                if temp.data == temp2.data:
                    pre.next = temp2.next
                    temp2 = temp2.next
                else:
                    pre = temp2
                    temp2 = temp2.next
            temp = temp.next

    def remove_dups_using_hash(self):
        hash_table = dict()
        temp = self.linked_list
        pre = temp
        while temp:
            if temp.data in hash_table:
                pre.next = temp.next
            else:
                hash_table[temp.data] = 1
                pre = temp
            temp = temp.next


if __name__ == '__main__':
    head = Node(0)
    arr = [1,1,1,1,1,2,2,4,4,4,1,1,2,3,6,7,4,8]
    temp = head
    for i in range(len(arr)):
        node = Node(arr[i])
        temp.next = node
        temp = node
    ob = RemoveDups()
    ob.linked_list = head.next
    ob.remove_dups_using_brute_force()
    # ob.remove_dups_using_hash()
    temp = ob.linked_list
    while temp:
        print(temp.data)
        temp = temp.next


