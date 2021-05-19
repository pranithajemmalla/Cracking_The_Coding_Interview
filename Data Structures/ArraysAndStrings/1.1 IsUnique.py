# Problem Statement :
# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional
# data structures

class IsUnique:
    def __init__(self):
        self.input_string = None

    def using_brute_force(self):
        for i in range(len(self.input_string)):
            for j in range(i+1, len(self.input_string)):
                if self.input_string[i] == self.input_string[j]:
                    return False
        return True

    def using_array_indices(self):
        hash_table = []
        for i in range(26):
            hash_table.append(0)
        for i in range(0, len(self.input_string)):
            if hash_table[ord(self.input_string[i]) - ord('a')] == 0:
                hash_table[ord(self.input_string[i]) - ord('a')] = 1
            else:
                return False
        return True

    def using_dict(self):
        hash_dict = dict()
        for s in self.input_string:
            if s in hash_dict:
                return False
            else:
                hash_dict[s] = 1
        return True

    def using_bitvector(self):
        checker = 0
        for s in self.input_string:
            bit_index = ord(s) - ord('a')
            if (checker & (1 << bit_index)) > 0:
                return False
            checker = checker | (1 << bit_index)
        return True

    def using_sort(self):
        sorted_string = "".join(sorted(self.input_string))
        for i in range(1, len(sorted_string)):
            if sorted_string[i-1] == sorted_string[i]:
                return False
        return True


if __name__ == '__main__':
    isUniqueObj = IsUnique()
    inputStr = input()

    if len(inputStr) > 128:
        print(False)

    isUniqueObj.input_string = inputStr
    print(isUniqueObj.using_brute_force())
    print(isUniqueObj.using_array_indices())
    print(isUniqueObj.using_dict())
    print(isUniqueObj.using_bitvector())
    print(isUniqueObj.using_sort())





