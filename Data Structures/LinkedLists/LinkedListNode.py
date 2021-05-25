class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, arr):
        self.head = None
        self.insert_all(arr, len(arr))
        self.len = 0

    def insert_all(self, arr, n):
        self.len = n
        temp = None
        for i in range(len(arr)):
            if i == 0:
                self.head = Node(arr[i])
                temp = self.head
                continue
            node = Node(arr[i])
            temp.next = node
            temp = node

    def remove_item(self, data, all_occurences):
        temp = self.head
        pre = temp
        while temp:
            if temp == data:
                self.len -= 1
                pre.next = temp.next
                temp = temp.next
                if not all_occurences:
                    break
            else:
                temp = temp.next

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next



